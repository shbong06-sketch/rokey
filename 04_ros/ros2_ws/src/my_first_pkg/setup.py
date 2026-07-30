from setuptools import find_packages, setup
import os
from glob import glob
# os -> os.listdir('어떤 위치')
# *.py 검색

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),    # shre/my_first_pkg/launch/*.py
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shbong',
    maintainer_email='shbong@gmail.com',
    description='TODO: ROS2 practice',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = my_first_pkg.talker:main',
            'listener = my_first_pkg.listener:main',
            'battery_pub = my_first_pkg.battery_pub:main',
            'battery_sub = my_first_pkg.battery_sub:main',
            'speed_pub = my_first_pkg.speed_pub:main',
            'speed_sub = my_first_pkg.speed_sub:main',
            'add_server = my_first_pkg.add_server:main',
            'add_client = my_first_pkg.add_client:main',
            'mul_server = my_first_pkg.mul_server:main',
            'mul_client = my_first_pkg.mul_client:main',
            'greeter = my_first_pkg.greeter:main',
            'blocking = my_first_pkg.blocking:main',
            'blocking_fixed = my_first_pkg.blocking_fixed:main',
            'count_server = my_first_pkg.count_server:main',
            'countdown_server = my_first_pkg.countdown_server:main',
            'count_client = my_first_pkg.count_client:main',
            'argument_node = my_first_pkg.argument_node:main',
            'operator_node = my_first_pkg.operator_node:main',
            'game_server = my_first_pkg.game_server:main',
            'player = my_first_pkg.player:main',
            "game_server_improvement = my_first_pkg.game_server_improvement:main",
            'player_improvement = my_first_pkg.player_improvement:main',
            'map_publisher = my_first_pkg.map_publisher:main',
            'map_subscription = my_first_pkg.map_subscription:main',
            'sensor_publisher = my_first_pkg.sensor_publisher:main',
            'heavy_pub = my_first_pkg.heavy_pub:main',
        ],
    },
)
