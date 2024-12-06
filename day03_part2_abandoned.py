import sys
import re

with open(sys.argv[1]) as f:
    data = f.read()

lastDo = data.rfind('do()')
lastDont = data.rfind('don\'t()')
firstDoAfterLastDont = data.find('do()', lastDont)

print(lastDo, lastDont, firstDoAfterLastDont)

if lastDont > lastDo:
    data = data[0:lastDont]

subStringsA = re.findall(r'^.*?don\'t\(\)', data)
subStringsB = re.findall(r'do\(\).*?don\'t\(\)', data)
subStringsC = [data[lastDo:]]

subStrings = subStringsA + subStringsB + subStringsC

print(subStringsA)
# print(subStringsB[0])
# print(subStringsB[1])
# print(subStringsB[2])
print(subStringsC)

data = ''.join(subStrings)

# for nonMulString in nonMulStrings:
#     newdata = data.replace(nonMulString, '')

# print(data,newdata)

mulStrings = re.findall(r'mul\([0-9]+,[0-9]+\)', data)

def multiplier(mulString):
    return int(mulString[4:-1].split(',')[0])*int(mulString[4:-1].split(',')[1])

sumOfMul = 0
for mulString in mulStrings:
    sumOfMul += (multiplier(mulString))
    
print(sumOfMul)