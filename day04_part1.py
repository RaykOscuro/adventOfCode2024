import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

def findAllXMAS(row,col):
    xCount = 0
    if col <= len(data[0])-4:
        if data[row][col+1]=="M" and data[row][col+2]=="A" and data[row][col+3]=="S":
            xCount += 1
    if col >= 3:
        if data[row][col-1]=="M" and data[row][col-2]=="A" and data[row][col-3]=="S":
            xCount += 1
    if row <= len(data)-4:
        if data[row+1][col]=="M" and data[row+2][col]=="A" and data[row+3][col]=="S":
            xCount += 1
    if row >= 3:
        if data[row-1][col]=="M" and data[row-2][col]=="A" and data[row-3][col]=="S":
            xCount += 1
    if col <= len(data[0])-4 and row <= len(data)-4:
        if data[row+1][col+1]=="M" and data[row+2][col+2]=="A" and data[row+3][col+3]=="S":
            xCount += 1
    if col <= len(data[0])-4 and row >= 3:
        if data[row-1][col+1]=="M" and data[row-2][col+2]=="A" and data[row-3][col+3]=="S":
            xCount += 1
    if col >= 3 and row <= len(data)-4:
        if data[row+1][col-1]=="M" and data[row+2][col-2]=="A" and data[row+3][col-3]=="S":
            xCount += 1
    if col >= 3 and row >= 3:
        if data[row-1][col-1]=="M" and data[row-2][col-2]=="A" and data[row-3][col-3]=="S":
            xCount += 1
    return xCount

totalXCount = 0

for i,line in enumerate(data):
    for j, character in enumerate(line):
        if character == "X":
            totalXCount += findAllXMAS(i,j)
            
print(totalXCount)