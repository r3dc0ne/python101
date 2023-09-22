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


def function_loop(amount, what, for_or_back):
    if what == horizontal_middle_part:
        if for_or_back == "for":
            for quantity in range(amount):
                print(what, end="")
                time.sleep(0.5)
        else:
            for quantity in range(amount):
                print("\b" * len(what) + what, end="")
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

function_loop(length, horizontal_middle_part, "for")

print(upper_corner_right)
# time.sleep(0.5)


keep_running = True

while keep_running:
    function_loop(height, ((length + 1) * " " + vertical_middle_part), "for")
    print((length + 1) * " " + lower_corner_right, end="")
    function_loop(length, horizontal_middle_part, "back")

    print(upper_corner_left)
    time.sleep(1)



    print(vertical_middle_part)
    time.sleep(1)

    print(lower_corner_left + length * horizontal_middle_part + upper_corner_right)
    time.sleep(1)
