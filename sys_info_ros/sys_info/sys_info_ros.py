from netifaces import AF_INET, ifaddresses, interfaces

import rclpy
from rclpy.node import Node

from sys_msgs.msg import NetworkAddress, NetworkDevice
from sys_msgs.srv import NetworkInfo, SystemInfo


# TODO: detailed WiFi information by parsing /proc/net/wireless
# TODO: Information about active I2C, GPIO etc. for Raspberry pi
# TODO: current temperatures from sensors service (if available)
# TODO: running processes, used memory and disc space
# TODO: special rpi information like undervoltage information or temperatures


def get_network_info(ignore_virtual_devices: bool = True):
    """Get network configuration for all devices on the machine as dict.

    uses the system netifaces-class provided as buildin python module.
    """
    netconfig = {}
    for interface in interfaces():
        if ignore_virtual_devices and (
                interface == 'lo'
                or interface.startswith('virbr')
                or interface.startswith('br-')
                or interface.startswith('docker')):
            continue
        ifaddr = ifaddresses(interface)
        if AF_INET in ifaddr:
            netconfig[interface] = ifaddr[AF_INET]
    return netconfig


def get_system_info(ignore_virtual_devices: bool = True):
    """Return system information as simple dict."""
    sysinfo = {
        'network': get_network_info(ignore_virtual_devices)
    }
    return sysinfo


def net_info_to_msg(net_info: dict) -> list[NetworkDevice]:
    devices = []
    for dev_name, dev_addr in net_info.items():
        addresses = []
        for ip_data in dev_addr:
            addresses.append(NetworkAddress(**ip_data))
        devices.append(NetworkDevice(
            name=dev_name,
            addr=addresses
        ))
    return devices


def sys_info_to_msg(sys_info: dict, response: SystemInfo):
    response.network_devices = net_info_to_msg(sys_info['network'])


class SysNode(Node):
    def __init__(self):
        super().__init__('sys_info')
        # Network information service
        self.net_srv = self.create_service(
            NetworkInfo, 'net_info', self.get_network_info)
        # System information service
        # self.system_srv = self.create_service(
        #    NetworkInfo, 'sys_info', self.get_system_info)
        self.get_logger().info('System information service ready.')

    def get_network_info(self, request, response):
        net_info = get_network_info(True)
        response.devices = net_info_to_msg(net_info)
        return response

    def get_system_info(self, request, response):
        sys_info = get_system_info(True)
        sys_info_to_msg(sys_info, response)
        return response


def main(args=None):
    rclpy.init(args=args)
    nn = SysNode()
    rclpy.spin(nn)
    nn.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
