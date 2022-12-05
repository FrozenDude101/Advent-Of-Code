from sys import path
path.append("../..")

from AoC import *

def parse(data):

    data = splitOn(data, "\n")
    data = splitOn(data, ",")
    data = splitOn(data, "-")
    data = mapAll(data, int)

    return data

def main(data):
    data = parse(data)

    t = 0
    for pair in data:
        e1 = pair[0]
        e2 = pair[1]

        r1 = [i for i in range(e1[0], e1[1]+1)]
        r2 = [i for i in range(e2[0], e2[1]+1)]

        for r in r1:
            if r in r2:
                t += 1
                break
        
    return t

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
copy(result)
print(result)
