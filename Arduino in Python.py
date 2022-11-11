import pyfirmata
import time

board = pyfirmata.Arduino('COM6')

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[53].mode = pyfirmata.INPUT

while True:
    sw = board.digital[53].read()
    if sw is True:
        print("good")
    else:
        print("bad")
    time.sleep(0.1)