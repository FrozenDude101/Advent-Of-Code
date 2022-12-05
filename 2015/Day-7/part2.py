from sys import path
path.append("../..")

from AoC import *

import hashlib

def format(line):

    data = {}
    line = line.split(" -> ")

    data["out"] = line[1]
    line = line[0].split(" ")

    if len(line) == 1:
        data["in"] = [line[0]]
        data["op"] = None
    else:
        if "AND" in line or "OR" in line:
            data["in"] = [line[0], line[2]]
            data["op"] = line[1]
        elif "NOT" in line:
            data["op"] = line[0]
            data["in"] = [line[1]]
        else:
            data["in"] = [line[0]]
            data["op"] = line[1]
            data["op2"] = int(line[2])

    return data

def makeWireDict(wires):

    ret = {}

    for wire in wires:
        ret[wire["out"]] = wire

    return ret

def makeRequirements(wires):

    ret = {}

    for wire in wires:
        ret[wire["out"]] = wire["in"]

    return ret

def solveWires(reqs, wires, target):

    global wireValues
    if target in wireValues: return wireValues[target]

    try:
        return int(target)
    except ValueError:
        pass

    print(target)

    wire = wires[target]

    if wire["op"] == None:
        val = (solveWires(reqs, wires, reqs[target][0])) % 65536

    elif wire["op"] == "AND":
        val = (solveWires(reqs, wires, wire["in"][0]) & solveWires(reqs, wires, wire["in"][1])) % 65536
    
    elif wire["op"] == "OR":
        val = (solveWires(reqs, wires, wire["in"][0]) | solveWires(reqs, wires, wire["in"][1])) % 65536

    elif wire["op"] == "LSHIFT":
        val = (solveWires(reqs, wires, wire["in"][0]) << wire["op2"]) % 65536
    
    elif wire["op"] == "RSHIFT":
        val = (solveWires(reqs, wires, wire["in"][0]) >> wire["op2"]) % 65536
    
    elif wire["op"] == "NOT":
        val = (~ solveWires(reqs, wires, wire["in"][0])) % 65536

    wireValues[target] = val
    return val

def run(data):

    data = splitOn(data, "\n")
    data = list(map(format, data))

    wires = makeWireDict(data)
    requirements = makeRequirements(data)

    global wireValues

    wireValues = {}
    value = solveWires(requirements, wires, "a")

    requirements["b"] = [value]
    
    wireValues = {}
    value = solveWires(requirements, wires, "a")

    return value

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
