import time

import math


def fuel(mass):
    return math.floor(mass/3)-2

def main(data):

    data = data.split("\n")
    data = map(int, data)

    total = 0
    for mass in data:
        mass = fuel(mass)
        while mass > 0:
            total += mass
            mass = fuel(mass)

    return total

data = None
with open("input.txt", "r") as file:
    data = file.read()

t0 = time.time()
result = main(data)
t1 = time.time()

print("Time Taken:\n\t{}ms\n\nOutput:\n\t{}".format((t1-t0) * 1000, result))
