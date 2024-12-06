import sys
import re

with open(sys.argv[1]) as f:
    data = f.read()
    
mulStrings = re.findall(r'mul\([0-9]+,[0-9]+\)', data)

def multiplier(mulString):
    return int(mulString[4:-1].split(',')[0])*int(mulString[4:-1].split(',')[1])

sumOfMul = 0
for mulString in mulStrings:
    sumOfMul += (multiplier(mulString))
    
print(sumOfMul)