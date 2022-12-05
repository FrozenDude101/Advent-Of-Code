from sys import path
path.append("../..")

from AoC import *

def run(data):

    data = splitOn(data, "\n")

    allChars = 0
    stringChars = 0
    for line in data:
        allChars += len(line)
        stringChars += len(line) + 2
        stringChars += list(line).count("\"")
        stringChars += list(line).count("\\")

    return stringChars - allChars

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
