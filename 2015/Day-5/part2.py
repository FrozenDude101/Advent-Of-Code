from sys import path
path.append("../..")

from AoC import *

import hashlib

def run(data):

    data = splitOn(data, "\n")

    pairs = [a + b for a in "abcdefghijklmnopqrstuvwxyz" for b in "abcdefghijklmnopqrstuvwxyz"]
    duplicates = [a + b + a for a in "abcdefghijklmnopqrstuvwxyz" for b in "abcdefghijklmnopqrstuvwxyz"]
    

    niceCount = 0
    for word in data:

        cont = True
        for dupe in duplicates:
            if dupe in word:
                cont = False
                break
        if cont: continue

        cont = True
        for pair in pairs:
            if pair in word:
                word2 = word.replace(pair, "--", 1)
                if pair in word2:
                    cont = False
                    break
        if cont: continue
        
        niceCount += 1

    return niceCount

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
