from zaber_motion import Units, Library
from zaber_motion.ascii import Connection
from Microswitch_InProcess_Connection import Microswitch

Library.enable_device_db_store()

with Connection.open_serial_port("COM7") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    device_v = device_list[0]  # h = horizontal
    device_h = device_list[1]  # v = vertical

    axis_h = device_h.get_axis(1)  # get axis (1 out of 1) for device_v
    axis_v = device_v.get_axis(1)  # get axis (1 out of 1) for device_h


    def place_on_sample(h, v):
        axis_h.move_relative(h, Units.LENGTH_MILLIMETRES)
        axis_v.move_relative(v, Units.LENGTH_MILLIMETRES)

    def place_off_sample():
        axis_v.home(wait_until_idle=False)
        axis_h.home(wait_until_idle=False)


    attempts_axis = 0
    while attempts_axis < 3:
        try:
            axis_v.home()
            axis_h.home()
            break
        except:
            axis_v.is_homed()
            axis_h.is_homed()
            print("Axes are homed")
            break

    attempts = 0
    while attempts < 3:
        try:
            place_on_sample(2, 2)
            break
        except:
            print("Sample is placed")
            break

    connection.close()
    Microswitch()