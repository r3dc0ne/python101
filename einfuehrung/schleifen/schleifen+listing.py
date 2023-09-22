
anzahl = 5

omgichweissnichtmehrweiter = anzahl * "+"


for i in range(anzahl):
    print(omgichweissnichtmehrweiter)



print(len(omgichweissnichtmehrweiter))

templist = list(omgichweissnichtmehrweiter)

print(templist)



test = [omgichweissnichtmehrweiter]
# test = [anzahl * "*"]

manuel = anzahl * test
print(manuel)

#templist2 = list(manuel)
#print(templist2)

for i in range(anzahl):
    print(manuel[i])

print(20 * "*")

list_of_plus = []
for i in range(anzahl):
    list_of_plus.append(list(manuel[i]))

print(list_of_plus)
list_of_plus[3][1] = "A"
print(list_of_plus)
