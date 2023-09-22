import random

print("Give 6 numbers between 1 and 49 (every number only once!): ")
n_1 = int(input("number 1: "))
n_2 = int(input("number 2: "))
n_3 = int(input("number 3: "))
n_4 = int(input("number 4: "))
n_5 = int(input("number 5: "))
n_6 = int(input("number 6: "))

list_numbers = [n_1, n_2, n_3, n_4, n_5, n_6]

print(list_numbers)

list_randoms = []
amount = 6

for i in range(amount):
    random_number = random.randint(1, 49)
    if random_number not in list_randoms:
        list_randoms.append(random_number)
    else:
        amount += 1
        continue

print(list_randoms)

list_of_same = []

for each_number in list_randoms:
    if each_number in list_numbers:
        list_of_same.append(each_number)

right_numbers = len(list_of_same)

if right_numbers < 6:
    print("You had", right_numbers, "right numbers:", list_of_same)
else:
    print("Wow, every number you chose was correct! You win!")
