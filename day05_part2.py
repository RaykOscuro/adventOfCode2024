import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    rules = []
    updates = []
    first = True
    for x in data:
        if x == '':
            first = False
            continue
        if first:
            rules.append(x)
        else:
            updates.append(x)
    
    # for i, x in enumerate(rules):
        # rules[i] = x.split('|')
        # for j in range(len(rules[i])):
        #     rules[i][j] = int(rules[i][j])
    for i, x in enumerate(updates):
        updates[i] = updates[i].split(',')
        for j in range(len(updates[i])):
            updates[i][j] = int(updates[i][j])

middleSum=0

def updateSort(update):
    left = []
    right = []
    if len(update) == 0:
        return []
    currentElement = update[0]
    for compareElement in update[1:]:
        if f"{currentElement}|{compareElement}" in rules:
            right.append(compareElement)
        else:
            left.append(compareElement)
    return updateSort(left) + [currentElement] + updateSort(right)
    

for i, update in enumerate(updates):
    valid = True
    for rule in rules:
        rule = rule.split('|')
        rule[0]=int(rule[0])
        rule[1]=int(rule[1])
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0])>update.index(rule[1]):
                valid = False
                break
        if valid == False:
            break
                
    print(f"Update {i} {"" if valid else "in"}valid!")
    if not valid:
        update = updateSort(update)
        print(update)
        middleSum += update[(len(update)-1)//2]
        
print(middleSum)