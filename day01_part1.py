import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    for i, x in enumerate(data):
        data[i] = x.split('   ')

left_data = []
right_data = []
for x in data:
    left_data.append(int(x[0]))
    right_data.append(int(x[1]))

left_data.sort()
right_data.sort()
difference=0

for i in range(len(left_data)):
    difference+=abs(left_data[i]-right_data[i])
    
print(difference)