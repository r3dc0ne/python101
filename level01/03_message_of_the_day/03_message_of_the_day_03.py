import random

messages = \
    ["No one is perfect - that’s why pencils have erasers. - Wolfgang Riebe",
     "Have no fear of perfection - you'll never reach it. - Salvador Dali",
     "The tallest mountain started as a stone. - One Punch Man Intro",
     "Make it work. Make it nice. Make it fast. Always obey this order! - kiraa",
     "A good programmer is someone who always looks both ways before crossing a one-way street. – Doug Linder",
     "If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger W. Dijkstra"]

messages_temp = messages.copy()

for i in range(6):
    username = input("username: ")
    print("good morning", username)
    remove = random.choice(messages)
    print(remove)
    messages.remove(remove)

messages_temp = messages.copy()

for i in range(2):
    username_ = input("username2: ")
    print("good morning", username_)
    remove2 = random.choice(messages_temp)
    print(remove2)
    messages_temp.remove(remove2)
