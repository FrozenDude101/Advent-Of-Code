from sys import path
path.append("../..")

from AoC import *

def parse(data):
    return mapAll(list(data), int)

def main(data):
    data = parse(data)

    total = 0
    for i in range(-1, len(data)-1):
        if data[i] == data[i+1]:
            total += data[i]
    
    return total

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
copy(result)
print(result)
