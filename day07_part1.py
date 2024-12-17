import sys
import copy

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    for i, x in enumerate(data):
        data[i] = x.split(': ')
        data[i][0] = int(data[i][0])
        data[i][1] = data[i][1].split(' ')
        for j, y in enumerate(data[i][1]):
            data[i][1][j] = int(data[i][1][j])

# print(data)

# def tryOperators(inputList, operatorList):
#     result = inputList.pop(0)
#     while len(operatorList)>0:
#         currentOperator=operatorList.pop(0)
#         if currentOperator == "*":
#             result *= inputList.pop(0)
#         else:
#             result += inputList.pop(0)
#     print(result)


# # for value in data[0][1]:
# #     operatorList.append("*")

# for testCase in data:
#     testValue = testCase[0]
#     inputList = testCase[1]
#     operatorList = []
#     for i in range(len(inputList)-1):
#         operatorList.append("*")
#     tryOperators(inputList,operatorList)

def doTheMath(result, inputList, testValue):
    # print(inputList)
    thing = inputList.pop(0) 
    resultA = result * thing
    resultB = result + thing
    if len(inputList)>0:
        return (doTheMath(resultA,copy.deepcopy(inputList),testValue)+doTheMath(resultB,copy.deepcopy(inputList),testValue))
    elif (resultA == testValue) or (resultB == testValue):
        return 1
    else:
        return 0
    
total = 0

for testCase in data:
    inputList = testCase[1]
    firstThing = inputList.pop(0)
    testValue = testCase[0]
    if doTheMath(firstThing,inputList,testValue)>0:
        total += testValue

print(total)