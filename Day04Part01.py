from enum import Enum


class XMAS(Enum):
    M = 1
    A = 2
    S = 3

global totalCount
totalCount = 0

global inputArray



def main():
    
    global inputArray
    fileInput = open("Day04Input.txt", "r")
    fileInputLines = fileInput.readlines()
    currentIndex = 0
    for currentLine in fileInputLines:
        inputArray[currentIndex] = list(currentLine)
        currentIndex += 1
    
    xLocation = 0
    yLocation = 0    
    for currentLine in inputArray:
        for currentChar in currentLine:
            if currentChar == 'X':
                checkXMAS(1, xLocation, yLocation, 0, 1)
                checkXMAS(1, xLocation, yLocation, 1, 1)
                checkXMAS(1, xLocation, yLocation, 1, 0)
                checkXMAS(1, xLocation, yLocation, 1, -1)
                checkXMAS(1, xLocation, yLocation, 0, -1)
                checkXMAS(1, xLocation, yLocation, -1, -1)
                checkXMAS(1, xLocation, yLocation, -1, 0)
                checkXMAS(1, xLocation, yLocation, -1, 1)
            xLocation += 1
        yLocation += 1

    print(totalCount)


def checkXMAS(nextLetter, xInput, yInput, xMod, yMod):
    global inputArray
    global totalCount
    newX = xInput+xMod
    newY = yInput+yMod
    if (inputArray[newX][newY] == XMAS(nextLetter)):
        if (nextLetter == XMAS(3)):
            totalCount += 1
        else:
            checkXMAS(XMAS(nextLetter+1), newX, newY, xMod, yMod)
    else:
        return
    

if __name__=="__main__":
    main()
    
