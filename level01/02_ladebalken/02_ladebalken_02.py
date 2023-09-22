state = int(input("enter state "))
status = int(state / 10)

for i in range(status, 11, 1):
    print("[" + ("#" * i) + (" " * (10 - i)) + "]", (i * 10), "%")

