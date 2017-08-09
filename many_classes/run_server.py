"""
This module can be used to launch a Tango Device Server with two Device
Classes:

* `DeviceOne`
* `DeviceTwo`

If you want to launch it just as a Python script, you'll have to add a
Device Server called `run_server` to your Tango Database. It would look like
that:

>>> python run_server.py test

In production-ready applications, it's strongly advised to include the `main`
method of this module as an `entry_point` in a `setup.py` script.

>>> setup(
>>> (...)
>>> entry_points={'console_scripts':['AggregateDS ='
>>>                                  'your_package.run_server:main']}
>>> (...)
>>> )

In such a case, you would have to define `AggregateDS` Device Server in your
Tango Database.
"""

from many_classes.device_one import DeviceOne
from many_classes.device_two import DeviceTwo
from tango.server import run


def main(args=None, **kwargs):
    return run((DeviceOne, DeviceTwo), args=args,
               **kwargs)

if __name__ == '__main__':
    main()
