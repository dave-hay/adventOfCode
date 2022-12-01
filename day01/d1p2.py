import heapq

calories = open('./input1.txt')

chungusList = []
curChungus = 0

for cal in calories:
    if cal == '\n':
        chungusList.append(curChungus)
        curChungus = 0
    else:
        curChungus += int(cal)

lrg = heapq.nlargest(3, chungusList)
print(sum(lrg))
