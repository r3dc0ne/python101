import random

messages = \
    ["No one is perfect - that’s why pencils have erasers. - Wolfgang Riebe",
     "Have no fear of perfection - you'll never reach it. - Salvador Dali",
     "The tallest mountain started as a stone. - One Punch Man Intro",
     "Make it work. Make it nice. Make it fast. Always obey this order! - kiraa",
     "A good programmer is someone who always looks both ways before crossing a one-way street. – Doug Linder",
     "If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger W. Dijkstra"]

random_message1 = random.choice(messages)
print(random_message1)

messages.remove(random_message1)
random_message2 = random.choice(messages)
print(random_message2)

# und so weiter
# aber dann stehen die alle untereinander und werden nicht immer neu generiert beim run