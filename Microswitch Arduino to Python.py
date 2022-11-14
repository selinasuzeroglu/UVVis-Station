import serial
import time

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)
while 1:
    line = ser.readline()
    string = line.decode('latin-1')
    print(string)


ser.close()
