class Hamster:

    def __init__(self, default_energy=100):
        self.energy = default_energy
        self.energy_max = default_energy

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
        energy_refillable = self.energy_max - self.energy
        if food <= energy_refillable:
            self.energy += food
        else:
            self.energy = self.energy_max


hamski = Hamster(200)
hamski.run()
hamski.run(2)
hamski.run(300)
print(hamski.energy)
hamski.eat(300)
hamski.eat(150)
print(hamski.energy)
hamski.run(25)

print(hamski)
