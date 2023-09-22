import random

amount = int(input('which amount? '))

# test = "0123456789"
test = "#" * amount
print(test)

random_number = random.randrange(len(test))
print(random_number)

temp_list = list(test)

temp_list[random_number] = "*"

test = "".join(temp_list)

print(test)

print('*' * 40)

for i in range(amount):
    print(test)

print('*' * 40)




