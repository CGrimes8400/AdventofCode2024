fileInput = open("Day01Input.txt", "r")

currentLine = ""

listLeft = []
listRight = []

for currentLine in fileInput:
    print(currentLine)
    listLeft.append(int(currentLine.split("   ")[0]))
    listRight.append(int(currentLine.split("   ")[1]))

listLeft.sort()
listRight.sort()

currentIndex = 0
totalSimilar = 0

# while currentIndex < len(listLeft):
#     totalDistance += abs(listLeft[currentIndex] - listRight[currentIndex])
#     currentIndex += 1
for leftItem in listLeft:
    currentcount = 0
    for rightItem in listRight:
        if leftItem == rightItem:
            currentcount += 1
    totalSimilar += currentcount * leftItem
    
fileInput.close()

print(totalSimilar)
    

