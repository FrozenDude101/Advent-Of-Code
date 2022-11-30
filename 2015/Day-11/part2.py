from sys import path
path.append("../..")

from AoC import *

def validPass(password):

    mustHave = [chr(i) + chr(i+1) + chr(i+2) for i in range(ord("a"), ord("x")+1)]
    notAllowed = "iol"
    pairs = [chr(i) + chr(i) for i in range(ord("a"), ord("z")+1)]

    for must in mustHave:
        if must in password: break
    else:
        return False

    for cant in notAllowed:
        if cant in password: return False

    for pair in pairs:
        if pair in password:
            password = password.replace(pair, ".", 1)
            break
    else:
        return False
    
    for pair in pairs:
        if pair in password:
            password = password.replace(pair, ".", 1)
            break
    else:
        return False

    return True

def incrementPass(password):

    password = list(password)
    password.reverse()

    for i in range(len(password)):
        if password[i] == "z":
            password[i] = "a"
            continue

        password[i] = chr(ord(password[i]) + 1)
        break

    password.reverse()
    return "".join(password)

def run(data):

    data = splitOn(data, "\n")[0]

    while not validPass(data):
        data = incrementPass(data)
    data = incrementPass(data)
    i 
    while not validPass(data):
        data = incrementPass(data)

    return data

with open("input.txt") as f:
    data = f.read()

ret = run(data)
print(ret)
