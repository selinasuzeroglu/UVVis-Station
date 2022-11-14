from zaber_motion import Units, Library
from zaber_motion.ascii import Connection

import serial
import time


Library.enable_device_db_store()

with Connection.open_serial_port("COM7") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    device_v = device_list[0]  # h = horizontal
    device_h = device_list[1]  # v = vertical

    axis_h = device_h.get_axis(1)  # get axis (1 out of 1) for device_v
    axis_v = device_v.get_axis(1)  # get axis (1 out of 1) for device_h


    def place_on(h, v):
        axis_h.move_relative(h, Units.LENGTH_MILLIMETRES)
        axis_v.move_relative(v, Units.LENGTH_MILLIMETRES)

    def place_off():
        axis_v.home(wait_until_idle=False)
        axis_h.home(wait_until_idle=False)

#checking is device 1 is homed three times
    #1
    if axis_v.is_homed():
        pass
    else:
        axis_v.home()
    #2
    if axis_v.is_homed():
        pass
    else:
    axis_v.home()
    #3
    if axis_v.is_homed():
        pass
    else:
        axis_v.home()

# checking is device 2 is homed three times
    #1
    if axis_h.is_homed():
        pass
    else:
        axis_h.home()
    #2
    if axis_h.is_homed():
        pass
    else:
        axis_h.home()
    #3
    if axis_h.is_homed():
        pass
    else:
        axis_h.home()


#placing sample in desired position
    place_on(100, 100)



#checking position three times
    #1
    if place_on(100,100):
        pass
    else:
        place_on(100, 100)
    #2
    if place_on(100, 100):
        pass
    else:
        place_on(100, 100)
    #3
    if place_on(100, 100):
        pass
    else:
        place_on(100, 100)




ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        if decoded_bytes == float(0.0):
            print("Sample Holder in Position")
            # initialize measurement start
        else:
            print("Sample Holder NOT in Position")

    except:
        print("Interrupt")
        break


ser.close()

#   place_off()