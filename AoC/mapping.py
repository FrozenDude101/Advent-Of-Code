from AoC.equality import isArray


def splitOn(value, splitChar):

    if isArray(value):
        return list(map(lambda val: splitOn(val, splitChar), value))

    return value.split(splitChar)

def toInts(values):

    if isArray(values[0]):
        return list(map(toInts, values))

    return list(map(int, values))