from tango import DevState
from tango.server import Device, attribute, DeviceMeta


class DeviceTwo(Device):
    """
    The second of the sample Device Classes.
    It only has one read-only string attribute.
    """
    __metaclass__ = DeviceMeta

    @attribute(dtype=str)
    def some_other_attribute(self):
        return "Whatever"

    def init_device(self):
        self.set_state(DevState.ON)
        self.set_status("Device 2 on")
