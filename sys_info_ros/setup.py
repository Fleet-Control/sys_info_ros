from setuptools import setup

package_name = 'sys_info_ros'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    requires=['netifaces'],
    zip_safe=True,
    maintainer='Andreas Bresser',
    maintainer_email='andreas.bresser@dfki.de',
    description='ROS 2 System information publication node',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sys_info_ros = sys_info_ros.sys_info_ros:main'
        ],
    },
)
