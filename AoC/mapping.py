from AoC.equality import isArray


def mapAll(value, func):

    if (isArray(value)):
        return list(map(lambda val: mapAll(val, func), value))

    return func(value)


def splitOn(value, splitChar):

    if isArray(value):
        return list(map(lambda val: splitOn(val, splitChar), value))

    return value.split(splitChar)