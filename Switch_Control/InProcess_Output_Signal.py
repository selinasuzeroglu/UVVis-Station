import serial
import time


def fire_signal():

    InProcessOutput = serial.Serial('COM6', 9600, timeout=1) #change in the future to fitting port
    time.sleep(2)
    InProcessOutput.flushInput()

    while True:
        try:
            Micro_bytes = InProcessOutput.readline()
            decoded_bytes = float(Micro_bytes[0:len(Micro_bytes)-2].decode("utf-8"))
            if decoded_bytes == float(0.0):
                print("Measurement started")
                #break
            else:
                print("Measurement didn't start")

        except:
            print("Interrupt")
            break

    InProcessOutput.close()
