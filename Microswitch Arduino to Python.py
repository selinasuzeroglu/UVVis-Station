
import serial
import time


ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        if decoded_bytes == float(0.0):
            print("Sample Holder in Position")
        else:
            print("Sample Holder NOT in Position")

    except:
        print("Interrupt")
        break


ser.close()