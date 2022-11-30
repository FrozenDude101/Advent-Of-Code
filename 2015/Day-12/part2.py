from sys import path
path.append("../..")

from AoC import *

import json

def countTotal(data):

    if type(data) == list:
        return countList(data)
    elif type(data) == dict:
        return countDict(data)
    elif type(data) == str:
        return 0
    else:
        return data

def countList(data):

    return sum(map(countTotal, data))

def countDict(data):

    total = 0
    for key in data:
        if data[key] == "red": return 0
        total += countTotal(data[key])
    return total

def run(data):

    data = json.loads(data)

    return countTotal(data)

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
