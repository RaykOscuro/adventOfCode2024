# read the input data
with open('day01_input.txt') as f:
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
similarity=0

for i in range(len(left_data)):
    temp_sim=0
    for j in range(len(right_data)):
        if left_data[i]==right_data[j]:
            temp_sim+=1
    similarity+=temp_sim*left_data[i]
    
print(similarity)