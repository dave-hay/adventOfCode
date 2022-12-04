"""
total score
rock A - Y paper
paper B - X rock
scissors C - Z scissors

loss-0
tie-3
win-6

x-1
y-2
z-3
"""

strategy = open('./input.txt')

total = 0

# create a graph opp x slf
# X=1, y=2, z=3
# a=1, b=2, c=3

# create graph / without piece used
mp = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

# convert to index
rosetta = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
# loop and get coordinates
for game in strategy:
    opp = rosetta[game[0]]
    slf = rosetta[game[2]]

    total += mp[opp - 1][slf - 1] + slf

print(total)
