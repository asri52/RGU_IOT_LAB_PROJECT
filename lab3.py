from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.show_letter("J")

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    if x == -1:
        sense.set_rotation(90)
    elif y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    elif x == 1:
        sense.set_rotation(270)

    print("x={0}, y={1}, z={2}".format(x, y, z))
