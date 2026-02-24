import datetime

import psutil


def get_uptime():
    uptime = f'{datetime.now() - datetime.fromtimestamp(psutil.boot_time())}'
    return uptime.split('.')[0]


def get_cpu_count():
    return psutil.cpu_count()


def get_cpu_freq():
    freq = psutil.cpu_freq()
    return (freq.current, freq.min, freq.max)


def get_cpu_percent():
    return psutil.cpu_percent()


def get_mem():
    return (psutil.virtual_memory().percent, psutil.virtual_memory().used)


def get_disk_usage():
    usage = psutil.disk_usage("/")
    return usage.used / usage.total * 100


# TODO: psutil.disk_partitions
# TODO: psutil.disk_io_counters
# TODO: sensors_battery
# TODO: sensors_fans
# TODO: sensors_temperatures
# TODO: swap_memory
# TODO: virtual_memory
