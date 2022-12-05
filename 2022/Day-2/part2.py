from sys import path
path.append("../..")

from AoC import *

def parse(data):
    data = splitOn(splitOn(data, "\n"), " ")
    return data

def score(p1, p2):

    if p1 == "A":       #rock
        if p2 == "X":
            return 0 + 3
        if p2 == "Y":
            return 3 + 1
        if p2 == "Z":
            return 6 + 2
    if p1 == "B":       #paper
        if p2 == "X":
            return 0 + 1
        if p2 == "Y":
            return 3 + 2
        if p2 == "Z":
            return 6 + 3
    if p1 == "C":       #scissors
        if p2 == "X":
            return 0 + 2
        if p2 == "Y":
            return 3 + 3
        if p2 == "Z":
            return 6 + 1

def main(data):
    data = parse(data)

    return sum(map(lambda s: score(*s), data))

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
copy(result)
print(result)
