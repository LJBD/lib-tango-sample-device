from random import random

from tango import DevState
from tango.server import Device, attribute, DeviceMeta


class DeviceOne(Device):
    __metaclass__ = DeviceMeta

    @attribute(dtype=float)
    def some_attribute(self):
        return random()

    def init_device(self):
        self.set_state(DevState.ON)
        self.set_status("Device 1 on")
