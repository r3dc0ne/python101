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


def function_loop(amount, what, h_v):
    if h_v == ORIENTATION_HORIZONTAL:
        for quantity in range(amount):
            print(what, end="")
            time.sleep(0.5)
    else:
        for quantity in range(amount):
            print(what)
            time.sleep(0.5)


horizontal_middle_part = "═"
vertical_middle_part = "║"
upper_corner_right = "╗"
upper_corner_left = "╔"
lower_corner_right = "╝"
lower_corner_left = "╚"

length = 10
# length = int(input("Length: "))
height = 2
# height = int(input("Height: "))

start = "╞"
end = "╡"

# first row
print(start, end="")
# time.sleep(0.5)

function_loop(length, horizontal_middle_part, ORIENTATION_HORIZONTAL)

keep_running = True

while keep_running:
    print(upper_corner_right)
    time.sleep(0.5)

    function_loop(height, ((length + 1) * " " + vertical_middle_part), ORIENTATION_VERTICAL)
    print((length + 1) * " " + lower_corner_right, end="")
    time.sleep(0.5)

    for i in range(length - 1):
        print("\r" + (length - (i + 1)) * " " + (i + 2) * horizontal_middle_part + lower_corner_right, end="")
        time.sleep(0.5)

    print("\r" + upper_corner_left + length * horizontal_middle_part + lower_corner_right)
    time.sleep(0.5)

    function_loop(height, vertical_middle_part, ORIENTATION_VERTICAL)
    print(lower_corner_left, end="")
    time.sleep(0.5)
    function_loop(length, horizontal_middle_part, ORIENTATION_HORIZONTAL)


