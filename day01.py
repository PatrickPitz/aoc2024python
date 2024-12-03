from util.aoc_loader import AocLoader

aoc = AocLoader(1)
aoc_data = aoc.load_data()

# Part 1
listA, listB = [], []
for line in aoc_data.splitlines():
    listA.append(int(line.split('   ')[0]))
    listB.append(int(line.split('   ')[1]))

listA.sort()
listB.sort()
distance = 0
for i in range(len(listA)):
    distance += abs(listA[i] - listB[i])

print(distance)

# Part 2
occurrences = {}
similar = 0
for element in listB:
    occurrences[element] = occurrences.get(element, 0) + 1

print(occurrences)

for element in listA:
    similar += element * occurrences.get(element, 0)

print(similar)
