from sys import path
path.append("../..")

from AoC import *

def parse(data):
    return mapAll(splitOn(splitOn(data, "\n\n"), "\n"), int)

def main(data):
    data = parse(data)

    data = list(map(sum, data))
    data.sort()
    
    return data[-1]

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
print(result)
