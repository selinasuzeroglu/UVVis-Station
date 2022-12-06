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

#checking is device  is homed three times
attempts_v = 0
while attempts_v < 3:
    try:
        axis_v.home()
        break
    except:
        axis_v.is_homed()
        print("Axis 1 is homed")
        break

attempts_h = 0
while attempts_h < 3:
    try:
        axis_h.home()
        break
    except:
        axis_h.is_homed()
        print("Axis 2 is homed")
        break



position_place_on = place_on().get_position(Units.LENGTH_MILLIMETRES)

#placing sample in desired position
place_on(100, 100)

attempts = 0
while attempts < 3:
    try:
        place_on(100, 100)
        break
    except:
        print("Sample is placed")
        break




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