"""Information about the ROS 2 system."""
import os


def ros_id():
    """Get ROS_DOMAIN_ID from system variable."""
    if 'ROS_DOMAIN_ID' in os.environ:
        return os.environ['ROS_DOMAIN_ID']
    # All ROS 2 nodes use domain ID 0 by default
    return '0'


def get_ros_distro():
    """Get ROS_DISTRO from system variable."""
    if 'ROS_DISTRO' in os.environ:
        return os.environ['ROS_DISTRO']
    return ''  # unknown
