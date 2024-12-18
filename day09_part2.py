import sys
import copy

with open(sys.argv[1]) as f:
    data = f.read()

is_data = True

current_id = 0

data_sizes=[]
space_sizes=[]

decoded_fs = []

for pos in data:
    if is_data:
        data_sizes.append(int(pos))
        # for i in range(int(pos)):
        #     decoded_fs.append(current_id)
        # current_id+=1
    else:
        space_sizes.append(int(pos))
    #     for i in range(int(pos)):
    #         decoded_fs.append(-1)
    is_data=not is_data

is_data = True

instructions = {}

for id in range(len(data_sizes)-1,-1,-1):
    current_size=data_sizes[id]
    for j, space in enumerate(space_sizes):
        if j>=id:
            # print("data block ",id,"goes nowhere :(")
            break
        if space >= current_size:
            space_sizes[j] -= current_size
            # print("data block ",id,"goes into space ", j)
            if j not in instructions.keys():
                instructions.update({j:[id]})
            else:
                instructions[j].append(id)
            break

handled_positions=[]
additional_space={}

for pos_pos, pos in enumerate(data):
    if is_data:
        for i in range(int(pos)):
            decoded_fs.append(-1 if int(pos_pos)//2 in handled_positions else current_id)
        current_id+=1
    elif not is_data:
        remaining_space = int(pos)
        if(pos_pos in additional_space.keys()):
            remaining_space
        # print(pos_pos, pos)
        space_index = (pos_pos-1)//2
        # print(space_index)
        if space_index in instructions.keys():
            for id in instructions[space_index]:
                handled_positions.append(id)
                current_data = int(data[id*2])
                for i in range(current_data):
                    decoded_fs.append(id)
                remaining_space-=current_data
        for i in range(remaining_space):
            decoded_fs.append(-1)
    # print(decoded_fs)
    is_data=not is_data

#1313165
# [0]
# [0, 2, 1, -1]
# [0, 2, 1, -1]
# [0, 2, 1, -1, -1, -1, -1, -1]
# [0, 2, 1, -1, -1, -1, -1, -1]
# [0, 2, 1, -1, -1, -1, -1, -1, 3, 3, 3, 3, 3, -1]
# [0, 2, 1, -1, -1, -1, -1, -1, 3, 3, 3, 3, 3, -1]
print(instructions)

# print(decoded_fs)

checksum = 0 
for pos, value in enumerate(decoded_fs):
    if value!=-1:
        # print(pos,value)
        checksum+=pos*value

print(checksum)