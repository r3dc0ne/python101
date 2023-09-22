import random

# length = 3
length = int(input("Length: "))
# height = 3
height = int(input("Height: "))

product = length * height

random_position = random.randrange(product - 1)

print(random_position)

listi = []
for i in range(product):
    if i == random_position:
        listi.append("*")
    else:
        listi.append("#")

for i in range(0, len(listi), length):
    joined_string = ''.join(listi[i:i+length])
    print(joined_string)


