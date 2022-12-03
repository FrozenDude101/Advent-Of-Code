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
    for i in range(0, len(data), 3):
        c1 = data[i]
        c2 = data[i+1]
        c3 = data[i+2]
        for c in c1[0] + c1[1]:
            if c not in c2[0] and c not in c2[1]: continue
            if c not in c3[0] and c not in c3[1]: continue
            total += priority(c)
            break

    return total

with open("input.txt", "r") as file:
    data = file.read()

result = main(data)
copy(result)
print(result)
