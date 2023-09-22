import random


def choice_of_the_day(_messages):
    messages_temp = _messages.copy()

    for i in range(6):
        username = input("username: ")
        print("good morning", username)
        remove = random.choice(messages_temp)
        print(remove)
        messages_temp.remove(remove)


messages = \
    ["No one is perfect - that’s why pencils have erasers. - Wolfgang Riebe",
     "Have no fear of perfection - you'll never reach it. - Salvador Dali",
     "The tallest mountain started as a stone. - One Punch Man Intro",
     "Make it work. Make it nice. Make it fast. Always obey this order! - kiraa",
     "A good programmer is someone who always looks both ways before crossing a one-way street. – Doug Linder",
     "If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger W. Dijkstra"]


#for i in range(2):
#    choice_of_the_day(messages)

#choice_of_the_day(messages)
#print("#" * 32)
#choice_of_the_day(messages)

keeprunning = True
while keeprunning:
    choice_of_the_day(messages)

