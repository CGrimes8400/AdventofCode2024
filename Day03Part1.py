import re 

fileInput = open("Day03Input.txt", "r")

totalCount = 0

for currentLine in fileInput:
    lineCount = re.findall("mul\(\d+,\d+\)", currentLine)
    for multiple in lineCount:
        firstVal = re.findall("\d+", multiple)[0]
        secondVal = re.findall("\d+", multiple)[1]
        totalCount += int(firstVal) * int(secondVal)
print(totalCount)