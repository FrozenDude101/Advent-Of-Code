from sys import path
path.append("../..")

from AoC import *

def run(data):

    houses = [(0,0)]
    pos = [0,0]

    for char in data:

        if char == "^": pos[1] -= 1
        if char == "v": pos[1] += 1
        if char == "<": pos[0] -= 1
        if char == ">": pos[0] += 1

        if tuple(pos) not in houses:
            houses.append(tuple(pos))

    return len(houses)
        

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
