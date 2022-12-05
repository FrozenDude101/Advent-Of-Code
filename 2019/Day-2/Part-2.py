import time


def main(data):

    data = data.split(",")
    data = list(map(int, data))

    data2 = [data[i] for i in range(len(data))]

    for k in range(100):
        for j in range(100):

            data = [data2[i] for i in range(len(data2))]

            data[1] = k
            data[2] = j

            for i in range(0, len(data), 4):

                try:

                    op = data[i]

                    if op == 1:
                        data[data[i+3]] = data[data[i+1]] + data[data[i+2]]

                    elif op == 2:
                        data[data[i+3]] = data[data[i+1]] * data[data[i+2]]

                    elif op == 99:
                        break   
                except:
                    continue

            if (data[0] == 19690720):
                print(k, j, k*100 + j)

    return data[0]


data = None
with open("input.txt", "r") as file:
    data = file.read()

t0 = time.time()
result = main(data)
t1 = time.time()

print("Time Taken:\n\t{}ms\n\nOutput:\n\t{}".format((t1-t0) * 1000, result))