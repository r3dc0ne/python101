state = int(input("enter state "))
print(state)

status = int(state / 10)

print(status)

print("[" + ("#" * status) + (" " * (10 - status)) + "]", state, "%")

