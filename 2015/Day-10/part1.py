from sys import path
path.append("../..")

from AoC import *

def iterate(data):

    i = 0
    l = len(data)
    ret = ""
    while i < l:
        char = data[i]
        count = 0
        while i<l and data[i] == char:
            count += 1
            i += 1
        ret += str(count) + char
    return ret
        
def run(data):

    data = splitOn(data, "\n")[0]

    for i in range(1000):
        data = iterate(data)
        print(data)

    return len(data)

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
