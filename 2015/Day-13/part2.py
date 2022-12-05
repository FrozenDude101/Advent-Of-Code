from sys import path
path.append("../..")

from AoC import *

def parse(data):

    ret = {}
    for line in data:
        print(line)
        if "gain" in line:
            line = line.split(" would gain ")
            sign = 1
        else:
            line = line.split(" would lose ")
            sign = -1
        a = line[0]
        line = line[1].split(" happiness units by sitting next to ")
        b = line[1][:-1]
        d = sign * int(line[0])

        if a not in ret:
            ret[a] = {}
        if b not in ret:
            ret[b] = {}
        ret[a][b] = d

    ret["Matt"] = {}
    for key in ret:
        ret[key]["Matt"] = 0
        ret["Matt"][key] = 0

    return ret

def resolvePathLength(graph, path):

    total = 0
    for i in range(-1, len(path)-1):
        total += graph[path[i]][path[i+1]]
        total += graph[path[i+1]][path[i]]
    return total

def getBestPath(graph, path):

    if len(graph) == len(path): return path

    bestPath = None
    for loc in graph:
        if loc in path: continue
        path2 = path.copy()
        path2.append(loc)
        path2 = getBestPath(graph, path2)

        if bestPath is None:
            bestPath = path2
        else:
            if resolvePathLength(graph, bestPath) < resolvePathLength(graph, path2):
                bestPath = path2

    return bestPath
            

def run(data):

    data = splitOn(data, "\n")
    if data[-1] == "": data = data[:-1]
    data = parse(data)

    path = getBestPath(data, [])
    print(path)

    return resolvePathLength(data, path)

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
