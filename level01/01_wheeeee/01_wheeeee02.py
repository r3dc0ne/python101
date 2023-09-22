# 2)

amount = int(input("enter MAX "))

for i in range(amount + 1):
    print("#" * i)
for i in range(amount):
    j = amount - 1 - i
    print("#" * j)

