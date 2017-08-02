from many_classes.device_one import DeviceOne
from many_classes.device_two import DeviceTwo
from tango.server import run


def main(args=None, **kwargs):
    return run({"DeviceOne": DeviceOne, "DeviceTwo": DeviceTwo}, args=args,
               **kwargs)

if __name__ == '__main__':
    main()
