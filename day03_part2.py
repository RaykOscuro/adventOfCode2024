import sys
import re

with open(sys.argv[1]) as f:
    data = f.read()

print(len(data))

while data.find('don\'t()') != -1:
    firstDont = data.find('don\'t()')
    firstDo = data.find('do()', firstDont)
    data = data[0:firstDont] + data[firstDo:]

print(len(data))

mulStrings = re.findall(r'mul\([0-9]+,[0-9]+\)', data)

def multiplier(mulString):
    return int(mulString[4:-1].split(',')[0])*int(mulString[4:-1].split(',')[1])

sumOfMul = 0
for mulString in mulStrings:
    sumOfMul += (multiplier(mulString))
    
print(sumOfMul)