# read the input data
with open('day02_input.txt') as f:
    data = f.read().splitlines()
    for i, x in enumerate(data):
        data[i] = x.split(' ')
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

def is_safe(levels):
    if levels[1]>levels[0]:
        increasing = True
    else:
        increasing = False
    for i in range(len(levels)-1):
        if abs(levels[i]-levels[i+1])>3 or abs(levels[i]-levels[i+1])==0:
             return False
        if increasing and levels[i]>levels[i+1]:
            return False
        if not increasing and levels[i]<levels[i+1]:
            return False
    return True

safe_count = 0
        
for levels in data:
    if is_safe(levels):
        safe_count+=1
        
print(safe_count)