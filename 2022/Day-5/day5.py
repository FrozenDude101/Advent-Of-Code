from sys import path as sys_path
sys_path.append("../..")

from AoC import *

def moveCrates(stacks, i0, i1, n):

    for i in range(n):
        n = stacks[i0].pop()
        stacks[i1].append(n)

def moveCrates2(stacks, i0, i1, n):

    toMove = stacks[i0][-n:]
    for i in range(n):
        n = stacks[i0].pop()
    stacks[i1].extend(toMove)
    

class Challenge_2022_5(Challenge):

    def parse(self, data):

        data = splitOn(data, "\n\n")
        
        stacks = data[0]
        stacks = splitOn(stacks, "\n")
        stacks = mapAll(stacks, list)
        
        moves = data[1]
        moves = splitOn(moves, "\n")
        moves = mapAll(mapAll(moves, lambda l: splitMultiple(
            l,
            ["move ", " from ", " to "],
            left = False,
        )), int)

        return (stacks, moves)

    def part1(self, data):
        stacks = data[0]
        moves = data[1]

        for move in moves:
            moveCrates(stacks, move[1]-1, move[2]-1, move[0])

        ret = ""
        for stack in stacks:
            ret += stack[-1]

        return ret

    def part2(self, data):
        stacks = data[0]
        moves = data[1]

        for move in moves:
            moveCrates2(stacks, move[1]-1, move[2]-1, move[0])

        ret = ""
        for stack in stacks:
            ret += stack[-1]

        return ret

c = Challenge_2022_5(2022, 5)
c.addTestCase("test1.txt", "CMZ", "MCD")
c.runChallenge("input.txt")
