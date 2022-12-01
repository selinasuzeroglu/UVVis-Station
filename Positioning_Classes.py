from zaber_motion import Units, Library
from zaber_motion.ascii import Connection

Library.enable_device_db_store()

with Connection.open_serial_port("COM7") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    device0 = device_list[0]
    device1 = device_list[1]

    axis_1 = device0.get_axis(1)  # get axis (1 out of 1) for device_v
    axis_2 = device1.get_axis(1)  # get axis (1 out of 1) for device_h

    retries = 0
    max_retries = 4


    class Axis:
        def __init__(self, axis, position=0):
            self.axis = axis
            self.position = position

        def __mul__(self):
            position = self.position * 8063.0
            return position

        def __eq__(self):
            return True if self.axis.get_position() == self.position * 8063.0 else False

        def place_on_sample(self):
            self.axis.move_absolute(self.position, Units.LENGTH_MILLIMETRES, wait_until_idle=True)

        def place_off_sample(self):
            self.axis.home(wait_until_idle=False)

        def park(self):
            self.axis.park()

        def unpark(self):
            self.axis.unpark()

    def homing():
        for i in range(0, 3):
            if connection.home_all(wait_until_idle=True):
                print("Axes are homed")
                break  # has to go
            else:
                connection.home_all(wait_until_idle=True)
                break  # has to go
    def placing(axes_posn):
        for i in range(0, 3):
            if all(axis.__eq__() is True for axis in axes_posn):
                for axis in axes_posn:
                    axis.park()
                print("Sample is placed")
            else:
                for axis in axes_posn:
                    axis.place_on_sample()
                    axis.park()


    #Define your axes and their 1st position:
    axis1_pos1 = Axis(axis_1, 20)
    axis2_pos1 = Axis(axis_2, 20)

    axes_pos1 = [axis1_pos1, axis2_pos1]  #creating lists of axes in their 1st position
    # other lists can follow with subsequent position: pos2, pos3, ...

    placing(axes_pos1)

    #unpark