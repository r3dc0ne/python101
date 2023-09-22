import random

test = '123456789'
print(test)

zu_ersetzen = random.choice(test)
print(zu_ersetzen)

ersatz = "*"
print(ersatz)

print(test.replace(zu_ersetzen, ersatz, 1))


print(40 * "_")


# test2 = "01234567890123456789"
test2 = "#########"
print(test2)

random_number = random.randrange(len(test2))
print(random_number)

temp_list = list(test2)

temp_list[random_number] = "*"

test2 = "".join(temp_list)

print(test2)


print(40 * "-")


amount = 4
hashtags = ['#' * amount]
second_random_number = random.randrange(len(hashtags))
temp_list_random_number = list(hashtags)
temp_list_random_number[second_random_number] = "*"
hashtags = "".join(temp_list_random_number)
print(hashtags)




