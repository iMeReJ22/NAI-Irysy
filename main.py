import math
import sys

# k = 20
# trainSet = "train.txt"
# testSet = "test.txt"
test2Set = "test2.txt"


if len(sys.argv) < 4:
    print("Not enough arguments.")
    exit(-1)

k = int(sys.argv[1])
trainSet = sys.argv[2]
testSet = sys.argv[3]

# klasa irys
class Iris:
    def reset(self):
        self.distance = float("inf")

    def setType(self, typeN):
        match typeN:
            case 0:
                self.type = "setosa"
            case 1:
                self.type = "versicolor"
            case 2:
                self.type = "virginica"

    def __init__(self, line):
        parts = line.split(",")
        self.a = float(parts[0])
        self.b = float(parts[1])
        self.c = float(parts[2])
        self.d = float(parts[3])
        if len(parts) == 5:
            self.type = parts[4].split("-")[1]
            self.type = self.type.replace("\n", "")
        else:
            self.type = "TBD"
        self.lastDistance = float("inf")

    def __str__(self):
        return f"[A:{self.a}, B:{self.b}, C:{self.c}, D:{self.d}]\ttype: {self.type}"


# metoda do liczenia odleglosci 2 wektorów
def findVectorDistance(iris1, iris2):
    return math.sqrt(
        pow(iris1.a - iris2.a, 2) + pow(iris1.b - iris2.b, 2) + pow(iris1.c - iris2.c, 2) + pow(iris1.d - iris2.d, 2))


def classificateIris(tmp, irisList):
    # liczenie odległości do innych irysow(train) dla tego irysa(test)
    for trainIris in irisList:
        # trainIris.reset()
        trainIris.lastDistance = findVectorDistance(trainIris, tmp)

    # wyciąganie top k najbliższych irysów
    sortedIrisList = sorted(irisList, key=lambda x: x.lastDistance, reverse=False)[:k]
    # zliczanie typów (setosa, versicolor, virginica)
    types = (0, 0, 0)
    types = list(types)
    for iris in sortedIrisList:
        match iris.type:
            case "setosa":
                types[0] += 1
            case "versicolor":
                types[1] += 1
            case "virginica":
                types[2] += 1
            case _:
                print(f"{iris.type} does not match anything")
    tmp.setType(types.index(max(types)))
    del types

    print(tmp)


# otwieranie plików
trainFile = open(trainSet, "r")
testFile = open(testSet, "r")
test2File = open(test2Set, "r")

# dodawanie wszystkich irysów testowych jako obiekty
irisList = list()
for line in trainFile:
    irisList.append(Iris(line))

# dodawanie wszystkich irysów do sprawdzenia jako obiegkty
toTestIrisList = list()
for line in testFile:
    toTestIrisList.append(Iris(line))

test2List = list()
for line in test2File:
    test2List.append(Iris(line))

print("After assigning: ")
for tmp in toTestIrisList:
    classificateIris(tmp, irisList)

i = 0
good = 0
for iris in test2List:
    if iris.type == toTestIrisList[i].type:
        good += 1
    i += 1

accuracy = good / i * 100

print(f"Celność dla k: {k} to {accuracy}%")



dalej = True
while dalej:
    try:
        uInput = input("Czy chcesz sprawdzić własny irys? (t/n)\n")
        if uInput != "n" and uInput != "t":
            raise Exception("Invalid input.")
        if uInput == "n":
            dalej = False
        else:
            uInput = input(f"Czy chcesz zmienić k? (teraz: {k}) (t/n)")
            if uInput != "n" and uInput != "t":
                raise Exception("Invalid input.")
            if(uInput == "t"):
                k = int(input("Podaj nowe k: "))
            a = float(input("Podaj dane dla nowego wektora:\nA: "))
            b = float(input("B: "))
            c = float(input("C: "))
            d = float(input("D: "))
            line = a.__str__() + "," + b.__str__() + "," + c.__str__() + "," + d.__str__()
            tmpIris = Iris(line)
            classificateIris(tmpIris, irisList)
    except Exception:
        print("Invalid input try again.")

print("Thank for using this exceptional, top of the line, the best in the world AI ;)")
