import UberHamster

uber_hamski = UberHamster.UberHamster("dorina")

uber_hamski.run()
# print(uber_hamski.energy)
uber_hamski.show_stats()

another_hamski = UberHamster.UberHamster("bison", 200)
another_hamski.run(2)
another_hamski.show_stats()

print("hamster counter: ", UberHamster.UberHamster.hamster_counter)
