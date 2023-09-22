import random

amount = 5  #int(input('which amount? '))
hashtags = '#' * amount

for i in range(amount):
    print(hashtags)


test = '#' * amount

random_number = random.randrange(len(test))
print(random_number)

temp_list = list(test)

temp_list[random_number] = "*"

test = "".join(temp_list)

print(test)


print(40 * "+")

random_number = random.randrange(len(hashtags))
print(random_number)

temp_list = list(hashtags)

temp_list[random_number] = "*"

hashtags = "".join(temp_list)

print(hashtags)
