import serial
import time
from SQL import fire_results


def fire_signal(product, result):
    InProcessOutput = serial.Serial('COM10', 9600, timeout=1)
    time.sleep(2)
    InProcessOutput.flushInput()
    time.sleep(2)
    while True:
        try:
            Micro_bytes = InProcessOutput.readline()
            decoded_bytes = float(Micro_bytes[0:len(Micro_bytes) - 2].decode("utf-8"))
            if decoded_bytes == float(0.0):
                time.sleep(30)
                fire_results(product, result)
                break
            else:
                print("Waiting for Measurement to start")

        except:
            print("Interrupt")
            break

    InProcessOutput.close()

#fire_signal('InProcess Test', 'Transmission')