# Funktionen

def awesome_function():
    print("coolio")


def ubercoolio(anzahl):
    print("coolio" * anzahl)


def multiply(zahl1, zahl2):
    print(zahl1 * zahl2)


def makepi(basis):
    print("basis", basis)
    calc = basis * 3.16
    return calc


awesome_function()

ubercoolio(3)
ubercoolio(7)

multiply(2, 3)

ergebnis = makepi(2)
print(ergebnis)

print(makepi(3))
