fileInput = open("Day01Input.txt", "r")

currentLine = ""

listLeft = []
listRight = []

for currentLine in fileInput:
    print(currentLine)
    listLeft.append(currentLine.split("   ")[0])
    listRight.append(currentLine.split("   ")[1])

listLeft.sort()
listRight.sort()

currentIndex = 0
totalDistance = 0

while currentIndex < len(listLeft):
    totalDistance += abs((int(listLeft[currentIndex]) - int(listRight[currentIndex])))
    currentIndex += 1
    
    
fileInput.close()

print(totalDistance)
    

