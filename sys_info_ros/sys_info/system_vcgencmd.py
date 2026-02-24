# Special system information for raspberry pi.
# vcgen-cmd for raspberry pi undervoltage/throtteling
try:
    from vcgencmd import Vcgencmd
    VCGENCMD = True
except ImportError:
    VCGENCMD = False


# https://www.raspberrypi.com/documentation/computers/os.html#vcgencmd
UNDERVOLTAGE_DETECTED = '0'
ARM_FREQ_CAPPED = '1'
CURRENTLY_THROTTLED = '2'
SOFT_TEMPERATURE_LIMIT = '3'
UNDERVOLTAGE_OCCURED = '16'
ARM_FREQ_CAPP_OCCURED = '17'
THROTTLING_OCCURED = '18'
SOFT_TEMPERATURE_LIMIT_OCCURED = '19'


def get_temp(vcgm: Vcgencmd):
    return float(vcgm.measure_temp())


def get_throttle_data(vcgm: Vcgencmd):
    return vcgm.get_throttled()['breakdown']


def setup():
    return Vcgencmd() if VCGENCMD else None


# TODO: measure_volts for more detailed CPU undervoltage issues
# TOCO: check modules e.g. with lsmod as subprocess if i2c_bcm2835 and i2c_dev or spi_bcm2835 are active