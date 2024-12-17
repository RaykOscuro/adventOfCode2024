import sys
import copy
import time

start_time = time.time()

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    gridData = []
    tempData = []
    currentPos = [-1, -1]
    for x in range(len(data[0])):
        tempData.append([])
    for y in range(len(data)):
        gridData.append(tempData.copy())
    for i, x in enumerate(data):
        for j, char in enumerate(x):
            if char == "^":
                currentPos = [i, j]
            gridData[i][j] = {
                "type": "." if char == "^" else char,
                "visited": (
                    {0: True, 1: False, 2: False, 3: False}
                    if char == "^"
                    else {0: False, 1: False, 2: False, 3: False}
                ),
                "og_visit": True if char =="^" else False
            }


startPos = [0,0]
currentDir = 0
startPos[0] = currentPos[0]
startPos[1] = currentPos[1]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

while True:
    maybePos = [currentPos[0]+directions[currentDir][0],currentPos[1]+directions[currentDir][1]]
    if maybePos[0] < 0 or maybePos[0] >= len(gridData) or maybePos[1] < 0 or maybePos[1] >= len(gridData[0]):
        break
    if gridData[maybePos[0]][maybePos[1]]["type"]=="#":
        currentDir+=1
        if currentDir==4:
            currentDir=0
    else:
        currentPos[0]=maybePos[0] 
        currentPos[1]=maybePos[1]
        gridData[maybePos[0]][maybePos[1]]["og_visit"]=True

def runTheLoop(theGrid):
    currentPos[0] = startPos[0]
    currentPos[1] = startPos[1]
    currentDir = 0
    while True:
        maybePos = [
            currentPos[0] + directions[currentDir][0],
            currentPos[1] + directions[currentDir][1],
        ]
        if (
            maybePos[0] < 0
            or maybePos[0] >= len(theGrid)
            or maybePos[1] < 0
            or maybePos[1] >= len(theGrid[0])
        ):
            return 0
        if theGrid[maybePos[0]][maybePos[1]]["type"] == "#":
            currentDir += 1
            if currentDir == 4:
                currentDir = 0
        else:
            currentPos[0] = maybePos[0]
            currentPos[1] = maybePos[1]
            # print(currentPos)
            if theGrid[maybePos[0]][maybePos[1]]["visited"][currentDir]:
                return 1
            else:
                theGrid[maybePos[0]][maybePos[1]]["visited"][currentDir] = True


totalLoops = 0
for i in range(len(gridData)):
    for j in range(len(gridData[0])):
        if gridData[i][j]["type"] == "." and gridData[i][j]["og_visit"] and (i != startPos[0] or j != startPos[1]):
            gridData[i][j]["type"] = "#"
            previous = totalLoops
            totalLoops += runTheLoop(gridData)
            # if (previous < totalLoops):
            #     print(i,j)
            gridData[i][j]["type"] = "."
            for v in range(len(gridData)):
                for w in range(len(gridData[0])):
                    gridData[v][w]["visited"] = (
                        {0: True, 1: False, 2: False, 3: False}
                        if char == "^"
                        else {0: False, 1: False, 2: False, 3: False}
                    )
print(totalLoops)
    # print(gridData[i])
# print(totalLoops)
print("--- %s seconds ---" % (time.time() - start_time))
