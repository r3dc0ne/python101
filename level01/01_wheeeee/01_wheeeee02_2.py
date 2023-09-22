amount = int(input("enter MAX "))

for i in range(amount + 1):
    print("#" * i)
for i in reversed(range(amount)): #das ergibt Sinn
    print("#" * i)

