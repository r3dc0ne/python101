class UberHamster:
    hamster_counter = 0

    def __init__(self, name, default_energy=100):
        UberHamster.hamster_counter += 1

        self.name = name
        self.energy = default_energy
        self.energy_max = default_energy

        print("this is hamster number", UberHamster.hamster_counter)

    def run(self, distance=1):
        print(self.name, "is running", self.energy)

        if distance > self.energy:
            self.energy -= self.energy
        else:
            self.energy -= distance

        if self.energy <= 0:
            print(self.name, "has no energy left")
        else:
            print(self.name, "has", self.energy, "energy left")

    def eat(self, food=50):
        energy_refillable = self.energy_max - self.energy
        if food <= energy_refillable:
            self.energy += food
        else:
            self.energy = self.energy_max

    def show_stats(self):
        print("stats for", self.name)
        print("energy:", self.energy, "/", self.energy_max)


if __name__ == "__main__":
    print("Hamster!")
    test_hamster = UberHamster("anna")
    test_hamster.run()
    test_hamster.show_stats()
else:
    print("Hamster imported.")
