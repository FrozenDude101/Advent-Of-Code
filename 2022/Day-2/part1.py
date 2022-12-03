from sys import path
path.append("../..")

from AoC import *

def parse(data):
    data = splitOn(splitOn(data, "\n"), " ")
    return data

def score(p1, p2):

    if p1 == "A":       #rock
        if p2 == "X":
            return 1 + 3
        if p2 == "Y":
            return 2 + 6
        if p2 == "Z":
            return 3 + 0
    if p1 == "B":       #paper
        if p2 == "X":
            return 1 + 0
        if p2 == "Y":
            return 2 + 3
        if p2 == "Z":
            return 3 + 6
    if p1 == "C":       #scissors
        if p2 == "X":
            return 1 + 6
        if p2 == "Y":
            return 2 + 0
        if p2 == "Z":
            return 3 + 3

def main(data):
    data = parse(data)

    return sum(map(lambda s: score(*s), data))

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
print(result)
