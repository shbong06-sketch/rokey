# 트랙 + Turtlebot3-Waffle 띄우기 => launch.py 만들기

# 너는 ros2 Turtlebot3-waffle의 카메라를 이용하는 자율 주행 실습을 위한 월드 구성 담당자야.

# 참고 자료
- /opt/ros/jazzy/share/turtlebot3_gazebo/launch/turtlebot3_world.launch.py 참고해서 만들기

# 트랙 sdf 파일 만들기
- 트랙의 요구사항
    - 타원형을 기본으로 만들어줘.
    - 폭은 waffle 2대가 동시에 진행할 정도
    - 도로는 회색, 중앙선은 노란색, 양 옆으로는 하얀 실선으로 구성되고, 트랙 바깥은 초원 색깔로 해줘.

# 주의 사항
- 자체 검증을 통해서 world(track)/waffle이 잘 떠있는지 점검해서 진행.
- 확인이 필요한 사항이 있으면 질문해서 명확히 하고 진행.