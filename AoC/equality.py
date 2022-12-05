from types import FunctionType


def isArray(value):
    return isinstance(value, list)

def isDict(value):
    return isinstance(value, dict)

def isFunction(value):
    return isinstance(value, FunctionType)