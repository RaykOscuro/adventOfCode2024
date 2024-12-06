import sys

with open(sys.argv[1]) as f:
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

def get_sublevels(levels):
    sublevels=[]
    for i in range(len(levels)):
        sublevels.append(levels[0:i]+levels[i+1:])
    return sublevels

safe_count = 0
        
for levels in data:
    safe = False
    for sublevel in get_sublevels(levels):
        if is_safe(sublevel):
            safe_count+=1
            break
        
print(safe_count)