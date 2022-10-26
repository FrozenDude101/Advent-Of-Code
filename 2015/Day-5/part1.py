from sys import path
path.append("../..")

from AoC import *

import hashlib

def run(data):

    data = splitOn(data, "\n")

    badStrings = ["ab", "cd", "pq", "xy"]
    duplicates = [c + c for c in "abcdefghijklmnopqrstuvwxyz"]

    niceCount = 0
    for word in data:

        cont = False
        for bad in badStrings:
            if bad in word:
                cont = True
                break
        if cont: continue

        cont = True
        for dupe in duplicates:
            if dupe in word:
                cont = False
                break
        if cont: continue

        vowels = 0
        for char in word:
            if char in ["a", "e", "i", "o", "u"]:
                vowels += 1
        if vowels < 3: continue

        niceCount += 1

    return niceCount

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
