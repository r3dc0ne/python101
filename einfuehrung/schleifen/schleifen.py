# Schleifen

for i in range(10):
    print(i)

print("#" * 10)

for i in range(10):
    print(i)
    if i == 7:
        print("hi there", i)


print("*" * 10)

for i in range(10, -1, -1):
    print(i)

print("*" * 10)

for i in range(0, 23, 2):
    print(i)

keeprunning = True  # Klassen großschreiben, Funktionen klein
while keeprunning:
    print("lol")
    userinput = input("continue? y/N")
    if userinput == "" or userinput == "n":
        keeprunning = False

keeprunning = True
while keeprunning:
    #print("roffl")
    userinput = input("continue2? y/N")
    if userinput == "y":
        print("roffl")
    else:
        keeprunning = False

