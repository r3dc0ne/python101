amount = int(input("How many students you want to introduce? "))

list_with_dictionaries = []

for person in range(amount):
    name = input("Who? ")
    city = input("Where from? (city) ")
    country = input("Where from? (country) ")
    why_python = input("Why is he/she learning Python? ")
    new_dictionary = {"Name": name, "Hometown": city, "country": country, "why they learn python": why_python}

    list_with_dictionaries.append(new_dictionary)

print(list_with_dictionaries)
