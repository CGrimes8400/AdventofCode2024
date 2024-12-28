import re 



global totalCount
totalCount = 0
global readingMultiply
readingMultiply = True


def main():
    fileInput = open("Day03Input.txt", "r")
    fileInputString = fileInput.read()
    searchString(fileInputString)
    print(totalCount)

def searchString(inputString):
    print("Called Function")
    global readingMultiply
    global totalCount
    if (readingMultiply):
        nextDont = re.split("don't\(\)", inputString, 1)
        firstHalf = nextDont[0]
        print("First Half DO")
        print(firstHalf)
        lineCount = re.findall("mul\(\d+,\d+\)", firstHalf)
        for multiple in lineCount:
            firstVal = re.findall("\d+", multiple)[0]
            secondVal = re.findall("\d+", multiple)[1]
            totalCount += int(firstVal) * int(secondVal)
            print(totalCount)
        readingMultiply = False
        if len(nextDont) > 1:
            print(nextDont[1])
            searchString(nextDont[1])
    else:
        nextDo = re.split("do\(\)", inputString, 1)
        firstHalf = nextDo[0]
        print("First Half DONT")
        print(firstHalf)
        readingMultiply = True
        if len(nextDo) > 1:
            print(nextDo[1])
            searchString(nextDo[1])





if __name__=="__main__":
    main()
    


# Start with On, search for dont separate on that dont, parse first half, look into second half for do. repeat