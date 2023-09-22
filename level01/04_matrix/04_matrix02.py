import random


#Anzahl
amount = 5  #int(input("which amount? "))

#Reihe an Hashtags
hashtags = '#' * amount
print(hashtags)
hashtags_list = [hashtags]
print(hashtags_list)

#beliebige Nummer, die in der Reihe ersetzt werden soll
second_random_number = random.randrange(len(hashtags))
temp_list_random_number = list(hashtags)
hashtags = "".join(temp_list_random_number)
print(hashtags)
print(second_random_number)


#Temporäre Liste
temp_list = amount * hashtags_list
print(temp_list)

#Beliebige Nummer, die von der Liste ausgewählt werden soll
first_random_number = random.randrange(len(temp_list))
print(first_random_number)


print(40 * "_")


list_of_hashtags = []
for i in range(amount):
    list_of_hashtags.append(list(temp_list[i]))
list_of_hashtags[first_random_number][second_random_number] = "*"
print(list_of_hashtags)

#get_together = "".join(list_of_hashtags)
#print(get_together)

for inner_list in list_of_hashtags:
    get_together = "".join(inner_list)
    print(get_together)

print(20 * "=")

for i in range(amount):
    get_together = "".join(list_of_hashtags[i])
    print(get_together)
