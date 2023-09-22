import random


#Anzahl
width = 8  #int(input("which width? "))
height = 5  #int(input("which hight? "))


#Reihe an Hashtags
hashtags = '#' * width
hashtags_list = [hashtags]

#beliebige Nummer, die in der Reihe ersetzt werden soll
second_random_number = random.randrange(len(hashtags))
temp_list_random_number = list(hashtags)
hashtags = "".join(temp_list_random_number)


#Temporäre Liste
temp_list = height * hashtags_list

#Beliebige Nummer, die von der Liste ausgewählt werden soll
first_random_number = random.randrange(len(temp_list))


list_of_hashtags = []
for i in range(height):
    list_of_hashtags.append(list(temp_list[i]))
list_of_hashtags[first_random_number][second_random_number] = "*"


for i in range(height):
    get_together = "".join(list_of_hashtags[i])
    print(get_together)
