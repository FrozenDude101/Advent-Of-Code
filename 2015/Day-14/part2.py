from sys import path
path.append("../..")

from AoC import *

class Reindeer():

    time = 0
    loc = 0
    isResting = False

    points = 0

    def __init__(self, name, speed, flyTime, restTime):

        self.name = name
        self.speed = speed
        self.flyTime = flyTime
        self.restTime = restTime

    def __str__(self):

        return "{}, s: {}, d: {}".format(self.name, self.isResting, self.loc)

    def increment(self, t=1):

        self.time += t
        if self.isResting:
            if self.time == self.restTime:
                self.isResting = False
                self.time = 0
        else:
            self.loc += self.speed
            if self.time == self.flyTime:
                self.isResting = True
                self.time = 0

def parse(data):

    return mapAll(data, lambda d: Reindeer(*splitMultiple(
        d,
        [" can fly ", " km/s for ", " seconds, but then must rest for ", " seconds."],
        [str, int, int, int]
    )))

def run(data):

    data = splitOn(data, "\n")
    if data[-1] == "": data = data[:-1]
    data = parse(data)

    for i in range(2503):
        for r in data:
            r.increment(1)

        data.sort(key = lambda r: r.loc)
        maxLoc = data[-1].loc
        for r in data:
            if r.loc == maxLoc:
                r.points += 1

    data.sort(key = lambda r: r.points)
    return data[-1].points

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
