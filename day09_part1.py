import sys
import copy

with open(sys.argv[1]) as f:
    data = f.read()

is_data = True

current_id = 0

decoded_fs = []

for pos in data:
    if is_data:
        for i in range(int(pos)):
            decoded_fs.append(current_id)
        current_id+=1
    else:
        for i in range(int(pos)):
            decoded_fs.append(-1)
    is_data=not is_data

last_data_pos = len(decoded_fs)-1
first_empty_pos = 0

def find_last_data_block(fs):
    for i in range(last_data_pos,-1,-1):
        if fs[i]!=-1:
            # print(first_empty_pos,fs[i],i)
            return fs[i], i
    return -100, -1

print(decoded_fs.index(-1))

while first_empty_pos<last_data_pos:
    first_empty_pos = decoded_fs.index(-1)
    last_data_block, last_data_pos = find_last_data_block(decoded_fs)
    if (first_empty_pos<last_data_pos):
        decoded_fs[first_empty_pos]=last_data_block
        decoded_fs[last_data_pos]=-1

checksum = 0 
for pos, value in enumerate(decoded_fs):
    if value!=-1:
        checksum+=pos*value

print(checksum)