from .equality import isArray


def mapAll(value, func):

    if (isArray(value)):
        return list(map(lambda val: mapAll(val, func), value))

    return func(value)


def splitOn(value, splitChar):

    if isArray(value):
        return list(map(lambda val: splitOn(val, splitChar), value))

    if splitChar == "": return list(value)
    return value.split(splitChar)


def splitMultiple(value, splits, types = None):

    value = [None, value]
    ret = []

    for i in range(len(splits)):
        value = value[1].split(splits[i])
        if types != None and len(types) > i:
            ret.append(types[i](value[0]))
        else:
            ret.append(value[0])

    return ret


def grouped(value, type = None):

    ret = splitOn(splitOn(value, "\n\n"), "\n")

    if type is not None:
        ret = mapAll(ret, type)

    return ret


def groupN(iter, groupSize):

    ret = []
    for i in range(0, len(iter), groupSize):
        ret.append(iter[i:i+groupSize])

    return ret