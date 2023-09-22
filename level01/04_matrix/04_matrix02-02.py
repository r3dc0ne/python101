import random

amount = int(input("which amount? "))

hashtags = '#' * amount
hashtags_list = [hashtags]

second_random_number = random.randrange(len(hashtags))
temp_list_random_number = list(hashtags)
hashtags = "".join(temp_list_random_number)

temp_list = amount * hashtags_list

first_random_number = random.randrange(len(temp_list))


list_of_hashtags = []
for i in range(amount):
    list_of_hashtags.append(list(temp_list[i]))
list_of_hashtags[first_random_number][second_random_number] = "*"

for i in range(amount):
    get_together = "".join(list_of_hashtags[i])
    print(get_together)
