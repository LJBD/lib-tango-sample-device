from random import random

from tango import DevState
from tango.server import Device, attribute, DeviceMeta


class DeviceOne(Device):
    """
    The first of the example Device Classes. Doesn't do much, only exposes
    one read-only float attribute.
    """
    __metaclass__ = DeviceMeta

    @attribute(dtype=float)
    def some_attribute(self):
        return random()

    def init_device(self):
        self.set_state(DevState.ON)
        self.set_status("Device 1 on")
