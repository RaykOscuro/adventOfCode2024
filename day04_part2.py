import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

def findAllX_MAS(row,col):
    xCount = 0
    if (1 <= col <= len(data[0])-2) and (1 <= row <= len(data)-2):
        if (data[row+1][col+1]=="M" and data[row-1][col-1]=="S") or (data[row+1][col+1]=="S" and data[row-1][col-1]=="M"):
            if (data[row-1][col+1]=="M" and data[row+1][col-1]=="S") or (data[row-1][col+1]=="S" and data[row+1][col-1]=="M"):
                xCount += 1
    return xCount

totalXCount = 0

for i,line in enumerate(data):
    for j, character in enumerate(line):
        if character == "A":
            totalXCount += findAllX_MAS(i,j)
            
print(totalXCount)