import time


def main(data):

    data = data.split(",")
    data = list(map(int, data))

    data[1] = 12
    data[2] = 2

    for i in range(0, len(data), 4):

        op = data[i]

        if op == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]

        elif op == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]

        elif op == 99:
            break

    return data[0]


data = None
with open("input.txt", "r") as file:
    data = file.read()

t0 = time.time()
result = main(data)
t1 = time.time()

print("Time Taken:\n\t{}ms\n\nOutput:\n\t{}".format((t1-t0) * 1000, result))