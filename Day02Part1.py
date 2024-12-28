fileInput = open("Day02Input.txt", "r")

currentLine = ""
currentLineSplit = []
increaseDecrease = 0
prevItem = 0
firstItem = True
totalValid = 0

listLeft = []
listRight = []

for currentLine in fileInput:
    print(currentLine)
    currentLineSplit = currentLine.split(" ")
    prevItem = 0
    firstItem = True
    increaseDecrease = 0
    isValid = True
    for report in currentLineSplit:
        if firstItem:
            prevItem = int(report)
            firstItem = False
        else:
            if (prevItem < int(report) and increaseDecrease == 0):
                increaseDecrease = 1
            elif (prevItem > int(report) and increaseDecrease == 0):
                increaseDecrease = -1
            if increaseDecrease == 1:
                difference = int(report) - prevItem
                if (difference < 1 or difference > 3):
                    isValid = False
                    
            else:
                difference = prevItem - int(report)
                if (difference < 1 or difference > 3):
                    isValid = False
            prevItem = int(report)
    if (isValid):
        totalValid += 1
        
    
fileInput.close()

print(totalValid)