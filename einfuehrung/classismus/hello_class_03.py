class Hamster:

    def __init__(self, default_energy=100):
        self.energy = default_energy

    def run(self, distance=1):
        print("I am running", self.energy)

        if distance > self.energy:
            self.energy -= self.energy
        else:
            self.energy -= distance

        if self.energy <= 0:
            print("I have no energy left")
        else:
            print("I have", self.energy, "energy left")

    def eat(self, food=50):
        self.energy += food


hamski = Hamster(200)
hamski.run()
hamski.run(2)
hamski.run(300)
print(hamski.energy)
hamski.eat(100)
print(hamski.energy)
hamski.run(25)
