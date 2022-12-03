from sys import path
path.append("../..")

from AoC import *

def parse(data):
    for i in range(1, 6):
        print("n = {}".format(i))
        print(groupN(data, i))
    return data

def main(data):
    data = parse([1,2,3,4,5,6])
    
    return data

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
copy([i for i in range(1000)])
print(result)
