import random
import itertools
from time import sleep

lights = "Red Green Yellow".split()


def rg_timer():
    return random.randint(3, 7)


def main():
    light = itertools.cycle(lights)
    while True:
        start = next(light)
        if start == "Red":
            print("STOP you heathen!!! You have to wait for {} seconds.".format(rg_timer()))
            sleep(rg_timer())
        elif start == "Yellow":
            print("Use CAUTION Yellow light")
            sleep(1.5)
        elif start == "Green":
            print(
                "Go before the people behind you start to think you're texting. You have {} seconds".format(rg_timer()))
            sleep(rg_timer())


main()

# ------------------ Py Bites solution -----------------------------

from time import sleep
import itertools
import random

colours = 'Red Green Amber'.split()
rotation = itertools.cycle(colours)


def rg_timer():
    return random.randint(3, 7)


def light_rotation(rotation):
    for colour in rotation:
        if colour == 'Amber':
            print('Caution! The light is %s' % colour)
            sleep(3)
        elif colour == 'Red':
            print('STOP! The light is %s' % colour)
            sleep(rg_timer())
        else:
            print('Go! The light is %s' % colour)
            sleep(rg_timer())


if __name__ == '__main__':
    light_rotation(rotation)
