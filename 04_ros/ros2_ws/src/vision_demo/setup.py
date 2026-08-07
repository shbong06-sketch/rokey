import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'vision_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world') + glob('worlds/*.sdf')),
        (os.path.join('share', package_name, 'models', 'oval_track'), glob('models/oval_track/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shbong',
    maintainer_email='shbong06@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'camera_pub=vision_demo.camera_pub:main',
            'camera_sub=vision_demo.camera_sub:main',
            'lane_detector=vision_demo.lane_detector:main',
            'pc_pub=vision_demo.pc_pub:main',
            'pc_sub=vision_demo.pc_sub:main',
            'plane_split=vision_demo.plane_split:main',
        ],
    },
)
