"""
═    ║    ╒    ╓    ╔    ╕    ╖    ╗    ╘    ╙    ╚    ╛    ╜    ╝    ╞    ╟
╠    ╡    ╢    ╣    ╤    ╥    ╦    ╧    ╨    ╩    ╪    ╫    ╬
---------------------|
                     |
---------------------|
|
|---------------------|
                      |
----------------------|
oh und slow, ich will die schlange char-weise wandern sehen
"""

import time

ORIENTATION_HORIZONTAL = "h"
ORIENTATION_VERTICAL = "v"

HORIZONTAL_MIDDLE_PART = "═"
VERTICAL_MIDDLE_PART = "║"
UPPER_CORNER_RIGHT = "╗"
UPPER_CORNER_LEFT = "╔"
LOWER_CORNER_RIGHT = "╝"
LOWER_CORNER_LEFT = "╚"

START_CHAR = "╞"
END_CHAR = "╡"


def sleepy():
    return time.sleep(0.2)


def function_loop(amount, what, horizontal_or_vertical_orientation):
    if horizontal_or_vertical_orientation == ORIENTATION_HORIZONTAL:
        for quantity in range(amount):
            print(what, end="")
            sleepy()
    else:
        for quantity in range(amount):
            print(what)
            sleepy()


def middle_part():
    for amounts in range(loop_amount):
        print(UPPER_CORNER_RIGHT)
        sleepy()

        function_loop(height, ((length + 1) * " " + VERTICAL_MIDDLE_PART), ORIENTATION_VERTICAL)

        print((length + 1) * " " + LOWER_CORNER_RIGHT, end="")
        sleepy()

        for i in range(length - 1):
            print("\r" + (length - (i + 1)) * " " + (i + 2) * HORIZONTAL_MIDDLE_PART + LOWER_CORNER_RIGHT, end="")
            sleepy()

        print("\r" + UPPER_CORNER_LEFT + length * HORIZONTAL_MIDDLE_PART + LOWER_CORNER_RIGHT)
        sleepy()

        function_loop(height, VERTICAL_MIDDLE_PART, ORIENTATION_VERTICAL)

        print(LOWER_CORNER_LEFT, end="")
        sleepy()

        function_loop(length, HORIZONTAL_MIDDLE_PART, ORIENTATION_HORIZONTAL)


# length = 3
length = int(input("Length: "))
# height = 2
height = int(input("Height: "))
# loop_amount = 2
loop_amount = int(input("Amount of loops: "))


# first row
print(START_CHAR, end="")
sleepy()

function_loop(length, HORIZONTAL_MIDDLE_PART, ORIENTATION_HORIZONTAL)

# middle part
middle_part()

# end char
print(END_CHAR)




