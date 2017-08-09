from tango import DevState, DeviceProxy, EventType, utils
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
        print "DeviceTwo.init_device: entering..."
        d = DeviceProxy("sys/test/deviceone-01")
        try:
            id_ = d.subscribe_event("some_attribute",
                                    EventType.CHANGE_EVENT,
                                    utils.EventCallBack())
        except Exception, e:
            print e
        self.set_state(DevState.ON)
        self.set_status("Device 2 on")
