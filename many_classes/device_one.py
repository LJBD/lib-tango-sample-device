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
        print "DeviceOne.init_device: entering..."
        self.set_change_event("some_attribute", True, False)
        self.set_state(DevState.ON)
        self.set_status("Device 1 on")
