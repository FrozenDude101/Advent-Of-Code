from sys import path
path.append("../..")

import AoC

def run(data):

    floor = 0;
    i = 0;
    for char in data:
        if char == ")": floor -= 1
        if char == "(": floor += 1
        i += 1;
        if floor == -1:
            return i

    return floor

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
