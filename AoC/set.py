from .equality import isFunction


def setIter(iter):

    if isFunction(iter):
        return set(iter())

    return set(iter)


def setRange(start, end):

    return set(range(start, end+1))