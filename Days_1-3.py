import os
from datetime import datetime
from datetime import timedelta
import time
import winsound
import argparse
from gooey import Gooey


@Gooey
def main():
    parser = argparse.ArgumentParser(description='Pomodoro Timer')
    parser.add_argument("Minutes", type=int, help="Number of minutes you wish to study for")
    args = parser.parse_args()
    study = args.Minutes
    #study = input("How many minutes would you like to study for (in minutes)? : ")
    timer(study)
    playding()


def timer(study):
    end = datetime.now() + timedelta(minutes=study)
    while end > datetime.now():
        time.sleep(5)


def playding():
    filename = os.path.abspath(os.path.join('.', 'sounds', 'Air_Horn.wav'))
    winsound.PlaySound(filename, winsound.SND_FILENAME)


if __name__ == '__main__':
    main()

# Code from lecture
# from datetime import datetime
# from datetime import date
# from datetime import timedelta
#
# print(datetime.today())
# today = datetime.today()
# print(type(today))
# print("---------------")
# todaydate = date.today()
# print("{} is type {}".format(todaydate, type(todaydate)))
# print(todaydate.month)
# print(todaydate.year)
# print(todaydate.day)
# christmas = date(2018, 12, 25)
# print((christmas - todaydate).days)
# print(christmas - todaydate)
# if christmas is not todaydate:
#     print('Sorry there are still {} days until christmas'.format(christmas - todaydate))
# else:
#     print("Yay Christmas!")
# # ---------------------------------
# # Time Delta
# t = timedelta(days=4, hours=10)
# print(type(t))
# print(t.days)
# # cannot do t.hours
# print(t.seconds)
# print(t.seconds / 60 / 60)
# eta = timedelta(hours=6)
# today = datetime.today()
# print(today + eta)
# print(str(today + eta))
