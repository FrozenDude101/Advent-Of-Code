from sys import path
path.append("../..")

from AoC import *

def ribbon(lengths):
    lengths.sort()
    n1 = lengths[0]
    n2 = lengths[1]
    n3 = lengths[2]

    return n1*n2*n3 + 2*n1 + 2*n2

def run(data):
    data = splitOn(data, "\n")
    data = splitOn(data, "x")
    data = toInts(data)
    return sum(map(ribbon, data))

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
