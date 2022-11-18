import serial
import time
from SQL_in_Python import spectrum

def Microswitch():

    MicroSwitch = serial.Serial('COM6', 9600, timeout=1)
    InProcess = serial.Serial('COM9', 9600, timeout=1)
    time.sleep(2)
    MicroSwitch.flushInput()
    InProcess.flushInput()

    while True:
        try:
            Micro_bytes = MicroSwitch.readline()
            decoded_bytes = float(Micro_bytes[0:len(Micro_bytes)-2].decode("utf-8"))
            if decoded_bytes == float(0.0):
                InProcess.write((bytes([0])))
                print("ok")
               # print(spectrum)
               # break
            else:
                print("Sample Holder NOT in Position")

        except:
            print("Interrupt")
            break


    MicroSwitch.close()
    InProcess.close()