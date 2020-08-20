"""week 4 prac: quick pics
produces a lines based on user input which show, ordered unique (per line) random numbers as integers"""

import random

NUMBERS_PER_LINE = 6
MAX_NUMBER = 45
MIN_NUMBER = 1


def main():
    number_of_lines = int(input("how many quick picks? "))
    while number_of_lines < 1:
        print("invald amount of lines")
        number_of_lines = int(input("how many lines? "))
    for number in range(number_of_lines):
        quick_picks = []
        for number_2 in range(NUMBERS_PER_LINE):
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while random_number in quick_picks:
                random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_picks.append(random_number)
        quick_picks.sort()
        # print(quick_picks)
        # used answers to figure out how to convert to string
        print(" ".join("{:3}".format(number_print) for number_print in quick_picks))

main()
