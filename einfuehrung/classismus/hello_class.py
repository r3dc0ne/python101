class Hamster:

    def __init__(self):
        self.energy = 100

    def run(self):
        print("I am running", self.energy)
        self.energy -= 1
        print("I have", self.energy, "energy left")


hamski = Hamster()
hamski.run()
hamski.run()
print(hamski.energy)
