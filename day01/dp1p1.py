calories = open('./input1.txt')

bigChungus = float('-inf')
curChungus = 0
for cal in calories:
    if cal == '\n':
        bigChungus = max(bigChungus, curChungus)
        curChungus = 0
    else:
        curChungus += int(cal)

print(bigChungus)
