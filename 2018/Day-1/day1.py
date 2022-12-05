from sys import path as sys_path
sys_path.append("../..")

from AoC import *

class Challenge_2018_1(Challenge):

    def parse(self, data):
        data = splitOn(data, "\n")
        data = mapAll(data, int)
        return data

    def part1(self, data):
        return sum(data)

    def part2(self, data):

        freq = 0
        seenFreqs = {}
        i = 0
        while freq not in seenFreqs:
            seenFreqs[freq] = True
            freq += data[i%len(data)]
            i += 1
        return freq

c = Challenge_2018_1(2018, 1)
c.addTestCase("test1.txt", 3, 2)
c.addTestCase("test2.txt", 3, None)
c.addTestCase("test3.txt", 0, None)
c.addTestCase("test4.txt", -6, None)
c.addTestCase("test5.txt", None, 0)
c.addTestCase("test6.txt", None, 10)
c.addTestCase("test7.txt", None, 5)
c.addTestCase("test8.txt", None, 14)
c.runChallenge("input.txt")
