import math
import sys

k = 30
trainSet = "train"
testSet = "test"


# if len(sys.argv) < 3:
#     print("Not enough arguments.")
#     exit(-1)
#
# k = int(sys.argv[0])
# trainSet = sys.argv[1]
# testSet = sys.argv[2]

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
        else:
            self.type = "TBD"
        self.distance = float("inf")

    def __str__(self):
        return f"[A:{self.a}, B:{self.b}, C:{self.c}, D:{self.d}]\ttype: {self.type}"


# metoda do liczenia odleglosci 2 wektorów
def findVectorDistance(iris1, iris2):
    return math.sqrt(
        pow(iris1.a - iris2.a, 2) + pow(iris1.b - iris2.b, 2) + pow(iris1.c - iris2.c, 2) + pow(iris1.d - iris2.d, 2))


# otwieranie plików
trainFile = open(trainSet, "r")
testFile = open(testSet, "r")

# dodawanie wszystkich irysów testowych jako obiekty
irisList = list()
for line in trainFile:
    irisList.append(Iris(line))

# obszar testowy
tmp = Iris(testFile.readline())
print(f"Before:\n{tmp}")

# liczenie odległości do innych irysow(train) dla tego irysa(test)
for trainIris in irisList:
    trainIris.reset()
    trainIris.distance = findVectorDistance(trainIris, tmp)

sortedIrisList = sorted(irisList, key=lambda x: x.distance, reverse=False)[:k]
# zliczanie typów (setosa, versicolor, virginica)
types = (0, 0, 0)
for iris in sortedIrisList:
    match iris.type:
        case "setosa":
            types[0] += 1
        case "versicolor":
            types[1] += 1
        case "virginica":
            types[2] += 1

tmp.setType(types.index(max(types)))

print(f"After:\n{tmp}")


