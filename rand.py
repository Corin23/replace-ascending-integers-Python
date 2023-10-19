import random

randomlist = []
numbers = int (input("How many numbers do you want to generate?\n"))
minim = int(input("Lowest value:\n"))
maxim = int(input("Highest value:\n"))

for i in range(0, numbers):
    n = random.randint(minim,maxim)
    randomlist.append(n)



with open("in.txt", "w") as filein:
    for item in randomlist:
        filein.write("%d\n" % item)

filein.close()
