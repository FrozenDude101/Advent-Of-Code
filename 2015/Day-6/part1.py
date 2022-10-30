from sys import path
path.append("../..")

from AoC import *

import hashlib

def format(line):

    line = line.split(" ")

    ret = {}
    ret["action"] = line[0]
    ret["start"] = tuple(map(int, line[1].split(",")))
    ret["end"] = tuple(map(int, line[3].split(",")))

    return ret

def run(data):

    data = splitOn(data, "\n")
    data = list(map(lambda x: x.replace("turn ", ""), data))
    data = list(map(format, data))

    field = [[False for i in range(1000)] for j in range(1000)]

    for ins in data:
        print(ins)
        action = ins["action"]
        start = ins["start"]
        end = ins["end"]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                if action == "off":
                    field[i][j] = 0
                if action == "on":
                    field[i][j] = 1
                if action == "toggle":
                    field[i][j] = not field[i][j]

    on = 0
    for line in field:
        for light in line:
            if light:
                on += 1
    return on

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
