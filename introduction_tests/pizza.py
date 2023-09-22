toppings = ["tomatoes", "cheese", "olives", "paprika", "corn", "spinach", "garlic", "onions"]

pizza_composition = []

counter = len(toppings)

rounds = True

while rounds:
    for i in range(counter):
        user_topping = input("What do you want on your pizza? ")

        if user_topping in toppings:
            pizza_composition.append(user_topping)
            print("Great! This topping is available.")
            print("Your pizza is with: ", pizza_composition)
        else:
            print("We are sorry! This topping is not available.")  # TESTEN !!!

        more = input("Do you want to add more? (y/n) ")
        if more == "y":
            rounds = True
        else:
            print("Okay, your pizza will be with: ", pizza_composition)
            rounds = False


# aufgabe: rounds muss so auf false gesetzt werden, dass es sich nicht wiederholt
