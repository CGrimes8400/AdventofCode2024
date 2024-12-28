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
    #print(currentLine)
    currentLineSplit = currentLine.split(" ")
    prevItem = 0
    firstItem = True
    increaseDecrease = 0
    isInvalidCount = 0
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
                    isInvalidCount += 1
                else:
                    prevItem = int(report)
                    
            else:
                difference = prevItem - int(report)
                if (difference < 1 or difference > 3):
                    isInvalidCount += 1
                else:
                    prevItem = int(report)
            
    if (isInvalidCount < 2):
        totalValid += 1
    else:
        print(currentLine)
        
    
fileInput.close()

print(totalValid)