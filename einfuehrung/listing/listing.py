pets = ["hamster", "stirnlappenbasilisk", "katze"]

print(pets)

print(pets[1])
print(pets[0])

pets.append("sloth")

print(pets)

pets.insert(1, "dönertier")
print(pets)

print(len(pets))

# pets.remove("katze")
removed = pets.pop(3)
print(pets)
print(removed)

petcounter = len(pets)
print(petcounter)

print(len(pets))

print(pets[3])

if "dönertier" in pets:
    print("wehavedönertier")

if "sloth" not in pets:
    print("noslothhere")

print(pets)

pets[1] = "lurch"

print(pets)


get_together = "".join(pets)

print(get_together)


coordinates = [
    {'x': 1, 'y': 2},
    {'x': 4, 'y': 9},
]

coordinates2 = [
    [1, 2],
    [4, 9],
]
ä