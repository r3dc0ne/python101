amount = int(input("enter MAX "))

for i in range(amount):
    print("#" * (i + 1))
for i in range(amount, 0, -1):
    print("#" * (i - 1))

