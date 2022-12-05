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

        if e1[0] <= e2[0] and e1[1] >= e2[1]:
            t += 1
        elif e2[0] <= e1[0] and e2[1] >= e1[1]:
            t += 1
    return t

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
copy(result)
print(result)
