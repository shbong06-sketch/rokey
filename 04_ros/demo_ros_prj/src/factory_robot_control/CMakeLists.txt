cmake_minimum_required(VERSION 3.8)
project(factory_robot_control)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)

# 메시지/서비스 인터페이스 생성
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/BatteryStatus.msg"
  "srv/ChargeCommand.srv"
  DEPENDENCIES std_msgs builtin_interfaces
)

# Python 모듈 설치
install(
  DIRECTORY factory_robot_control/
  DESTINATION lib/python3.12/site-packages/factory_robot_control
  FILES_MATCHING PATTERN "*.py"
)

# 실행 파일 설치
install(PROGRAMS
  factory_robot_control/amr_node.py
  factory_robot_control/control_center_node.py
  factory_robot_control/dashboard_server.py
  factory_robot_control/utils.py
  DESTINATION lib/${PROJECT_NAME}
)

# 실행 파일 심볼릭 링크 생성 (확장자 없이 실행 가능하도록)
install(CODE "
  execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink
    amr_node.py
    \$ENV{DESTDIR}\${CMAKE_INSTALL_PREFIX}/lib/${PROJECT_NAME}/amr_node
  )
  execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink
    control_center_node.py
    \$ENV{DESTDIR}\${CMAKE_INSTALL_PREFIX}/lib/${PROJECT_NAME}/control_center_node
  )
  execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink
    dashboard_server.py
    \$ENV{DESTDIR}\${CMAKE_INSTALL_PREFIX}/lib/${PROJECT_NAME}/dashboard_server
  )
")

# 런치 파일 설치
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()
