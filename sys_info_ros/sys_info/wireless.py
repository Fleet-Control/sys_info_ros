# regex to parse wireless network
import re
from pathlib import Path
try:
    import gi
    gi.require_version('NM', '1.0')
    from gi.repository import NM
    nmc = NM.Client.new(None)
    devs = nmc.get_devices()
    NETWORK_MANAGER = True
except ImportError:
    NETWORK_MANAGER = False
except ValueError:
    NETWORK_MANAGER = False


def get_wifi_strength_nm():
    global devs
    for device in devs:
        if device.get_device_type() != NM.DeviceType.WIFI:
            continue
        for ap in device.get_access_points():
            return float(ap.get_strength())
    return 0.0


def get_wifi_strength_proc():
    # this only works on ubuntu
    if not Path('/proc/net/wireless').exists():
        return float(0.0)
    with open('/proc/net/wireless', 'r', encoding='utf-8') as fd:
        text = fd.read()
        text = text.split('\n')
        if len(text[2]) < 1:
            return -1
        first_line = re.sub(r'[\s\|]{2,}', ' ', text[1]).split(' ')
        sec_line = re.sub(r'[\s\|]{2,}', ' ', text[2]).split(' ')
        index = first_line.index('link')
        wifi_strength = sec_line[index]
        return float(wifi_strength)


def get_wifi_strength():
    if NETWORK_MANAGER:
        return get_wifi_strength_nm()
    else:
        return get_wifi_strength_proc()


if __name__ == '__main__':
    print(get_wifi_strength())
