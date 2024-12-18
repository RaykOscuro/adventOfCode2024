import sys
import copy

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

antennas = {}

for i, line in enumerate(data):
    for j, character in enumerate(line):
        if character != ".":
            if not (character in antennas.keys()):
                antennas.update({character: [[i, j]]})
            else:
                antennas[character].append([i,j])
                
max_x=len(data[0])-1
max_y=len(data)-1

antinodes = []

def find_antinodes(antenna_locations):
    for i in range(len(antenna_locations)):
        for j in range(i+1,len(antenna_locations)):
            y_diff = antenna_locations[j][0]-antenna_locations[i][0]
            x_diff = antenna_locations[j][1]-antenna_locations[i][1]
            for n in range(50):
                antinode_1 = [antenna_locations[i][0]+n*y_diff,antenna_locations[i][1]+n*x_diff]
                antinode_2 = [antenna_locations[j][0]-n*y_diff,antenna_locations[j][1]-n*x_diff]
                if not (antinode_1[0]<0 or antinode_1[0]>max_y or antinode_1[1]<0 or antinode_1[1]>max_x):
                    antinode_1_str = str(antinode_1[0])+"_"+str(antinode_1[1])
                    if not (antinode_1_str in antinodes):
                        antinodes.append(antinode_1_str)
                if not (antinode_2 in antinodes or antinode_2[0]<0 or antinode_2[0]>max_y or antinode_2[1]<0 or antinode_2[1]>max_x):
                    antinode_2_str = str(antinode_2[0])+"_"+str(antinode_2[1])
                    if not (antinode_2_str in antinodes):
                        antinodes.append(str(antinode_2[0])+"_"+str(antinode_2[1]))
            
for key in antennas.keys():
    find_antinodes(antennas[key])
    
# print(antinodes)
print(len(antinodes))