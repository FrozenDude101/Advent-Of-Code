from sys import path
path.append("../..")

from AoC import *

def run(data):

    houses = [(0,0)]
    pos = [0,0]
    pos2 = [0,0]
    turn = 0

    for char in data:

        if turn == 0:

            if char == "^": pos[1] -= 1
            if char == "v": pos[1] += 1
            if char == "<": pos[0] -= 1
            if char == ">": pos[0] += 1

            if tuple(pos) not in houses:
                houses.append(tuple(pos))
                
        if turn == 1:

            if char == "^": pos2[1] -= 1
            if char == "v": pos2[1] += 1
            if char == "<": pos2[0] -= 1
            if char == ">": pos2[0] += 1

            if tuple(pos2) not in houses:
                houses.append(tuple(pos2))

        turn = not turn


    return len(houses)
        

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
