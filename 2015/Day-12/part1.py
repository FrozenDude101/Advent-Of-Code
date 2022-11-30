from sys import path
path.append("../..")

from AoC import *

import re

def getAllNumbers(data):

    return map(int, re.findall(r"-?\d+", data))

def run(data):

    nums = getAllNumbers(data)

    return sum(nums)

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
