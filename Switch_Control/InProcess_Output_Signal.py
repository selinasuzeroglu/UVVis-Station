import serial
import time


import serial
import time
from SQL import fire_results


def fire_signal():

    InProcessOutput = serial.Serial('COM6', 9600, timeout=1) #change in the future to fitting port
    time.sleep(2)
    InProcessOutput.flushInput()

    while True:
        try:
            Micro_bytes = InProcessOutput.readline()
            decoded_bytes = float(Micro_bytes[0:len(Micro_bytes)-2].decode("utf-8"))
            if decoded_bytes == float(0.0):
                #print("Measurement started")
                time.sleep(10)
                fire_results('test', 'Transmission')
                break
            else:
                print("Waiting for Measurement to start")

        except:
            print("Interrupt")
            break

    InProcessOutput.close()


#fire_signal('test', 'Transmission')