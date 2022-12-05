from sys import path
path.append("../..")

from AoC import *

def parse(data):
    return grouped(data, int)

def main(data):
    data = parse(data)

    data = list(map(sum, data))
    data.sort()
    
    return data[-1] + data[-2] + data[-3]

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
print(result)
