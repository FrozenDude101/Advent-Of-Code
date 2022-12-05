from sys import path
path.append("../..")

from AoC import *

def run(data):

    data = splitOn(data, "\n")

    allChars = 0
    stringChars = 0
    for line in data:
        allChars += len(line)
        line = line[1:-1]

        i = 0
        while i < len(line):
            stringChars += 1
            if line[i] == "\\":
                if line[i+1] == "\"" or line[i+1] == "\\":
                    i += 1
                else:
                    i += 3
            i += 1

    return allChars - stringChars

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
