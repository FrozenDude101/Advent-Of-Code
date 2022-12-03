from sys import path
path.append("../..")

from AoC import *

def parse(data):
    return mapAll(list(data), int)

def main(data):
    data = parse(data)

    total = 0
    for i in range(0, len(data)):
        if data[i] == data[(i+len(data)//2) % len(data)]:
            total += data[i]
    
    return total

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
copy(result)
print(result)
