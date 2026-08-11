from setuptools import find_packages, setup

package_name = 'mission_worker_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shbong',
    maintainer_email='shbong06@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'mission_worker = mission_worker_pkg.mission_worker:main',
            'db_manager = mission_worker_pkg.db_manager:main',
        ],
    },
)
