def show_water(_inventory):
    print("my water:", _inventory["water"])


inventory = {"desert eagle": 1, ".45 magazines": 3, "water": 7}
print(inventory)

show_water(inventory)

inventory["water"] -= 1
show_water(inventory)

inventory["water"] = 9
show_water(inventory)

inventory["spoons"] = 3
print(inventory)
print("my spoons:", inventory["spoons"])

if "hamster" not in inventory:
    inventory.pop("desert eagle")
    inventory["hamster"] = 1

print(inventory)

