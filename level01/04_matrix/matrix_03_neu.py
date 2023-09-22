import random

# length = 10
length = int(input("Length: "))
# height = 4
height = int(input("Height: "))
# randoms = 4
randoms = int(input("Randoms: "))

product = length * height

list_of_randoms = []
for i in range(randoms):
    random_position = random.randrange(product - 1)
    if random_position in list_of_randoms:
        continue
    else:
        list_of_randoms.append(random_position)

# print(list_of_randoms)

listi = []
for i in range(product):
    if i in list_of_randoms:
        listi.append("*")
    else:
        listi.append("#")

for i in range(0, len(listi), length):
    joined_string = ''.join(listi[i:i+length])
    print(joined_string)

