from sys import path
path.append("../..")

from AoC import *

def parse(data):
    data = splitOn(data, "\n")
    for i in range(len(data)):
        data[i] = (data[i][:len(data[i])//2], data[i][len(data[i])//2:])
    return data

def priority(char):
    if ord(char) >= ord("a"):
        return ord(char) - ord("a") + 1
    else:
        return ord(char) - ord("A") + 1 + 26

def main(data):
    data = parse(data)

    total = 0
    for item in data:
        for char in item[0]:
            if char in item[1]:
                total += priority(char)
                break

    return total

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
copy(result)
print(result)
