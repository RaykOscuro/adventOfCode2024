import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    gridData = []
    tempData = []
    currentPos = [-1,-1]
    for x in range(len(data[0])):
        tempData.append([])
    for y in range(len(data)):
        gridData.append(tempData.copy())
    for i, x in enumerate(data):
        for j, char in enumerate(x):
            if char == "^":
                currentPos = [i,j]
            gridData[i][j] = {"type": "." if char == "^" else char, "visited": [0,1] if char == "^" else False}

directions = [[-1,0],[0,1], [1,0], [0,-1]]
currentDir = 0

# print(currentPos)
# print(gridData[currentPos[0]][currentPos[1]]["type"]=='.')

while True:
    maybePos = [currentPos[0]+directions[currentDir][0],currentPos[1]+directions[currentDir][1]]
    if maybePos[0] < 0 or maybePos[0] >= len(gridData) or maybePos[1] < 0 or maybePos[1] >= len(gridData[0]):
        break
    if gridData[maybePos[0]][maybePos[1]]["type"]=="#":
        # print("boop")
        currentDir+=1
        if currentDir==4:
            currentDir=0
    else:
        currentPos[0]=maybePos[0] 
        currentPos[1]=maybePos[1]
        # print("hello!")
        gridData[maybePos[0]][maybePos[1]]["visited"]=True

# print(gridData)

total=0

for x in gridData:
    for y in x:
        # print(y)
        if y["visited"]==True:
            total+=1
            
print(total)