# ohne dynamische Eingabe
print("[###       ] 30 %")

print(" ")

# mit dynamischer Eingabe mit ganzen Zahlen zwischen 1 und 10
status = int(input("enter number between 1 and 10: ")) # enter number between 1 and 10 (for 10 to 100 %)
print("[" + ("#" * status) + (" " * (10 - status)) + "]", (status * 10), "%")

print(" ")


print(status / 10)



