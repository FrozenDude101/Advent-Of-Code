from sys import path
path.append("../..")

from AoC import *

import hashlib

def run(data):

    i = 0
    while True:
        hashText = hashlib.md5((data + str(i)).encode("utf-8")).hexdigest()
        if hashText[0:6] == "000000":
            break
        i+=1

    return i

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
