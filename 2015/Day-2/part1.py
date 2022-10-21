from sys import path
path.append("../..")

from AoC import *

def sa(lengths):
    x = lengths[0]
    y = lengths[1]
    z = lengths[2]
    return 2*x*y + 2*x*z + 2*y*z + min(x*y, x*z, y*z)

def run(data):
    data = splitOn(data, "\n")
    data = splitOn(data, "x")
    data = toInts(data)
    return sum(map(sa, data))

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
