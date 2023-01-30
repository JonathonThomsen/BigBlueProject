import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

def burnoutToapogeeFunct(df):
    chunk = []
    for row in range(1, len(df)):
        if df[row][7] == 0:
            chunk.append(list(df[row]))
        if df[row][22] < df[row-1][22]:
            break

    return chunk
def deployTimefunct(opData):
    cutoffrow = 0
    row = 1
    while cutoffrow == 0:
        if opData[row][22] > 10000:
            cutoffrow = opData[row]
            break
        else:
            row = row+1
    bestTime = cutoffrow[0] - opData[0][0]
    return bestTime


def plot(important):
    print("File Name: ", file)
    print("What would you like to plot?")
    print("Insert index for x values: ")
    x = int(input())
    print("Insert Index for y values: ")
    y = int(input())

    xs = [important[i][x] for i in range(1, len(important))]
    ys = [important[i][y] for i in range(1, len(important))]

    plt.plot(xs, ys)
    plt.xlabel(header[x])
    plt.ylabel(header[y])
    plt.show()


#path = "C:\Users\jtkin\Documents\Python\Experimental\For Python"

directory = "C:/Users/jtkin/Documents/RASAero II"
bigblock = []
for file in os.listdir(directory):
    split = os.path.splitext(file)
    need = split[1]
    #print(need)

    if need == '.CSV':
        f =os.path.join(directory, file)
        df = pd.read_csv(f)

        print(file)
        #print("Skip? Type y for Yes")
        skip = "n"
        first = file + ","
        info = [first]
        if skip == "y":
            continue
        else:
            header = []
            for col in df.columns:
                header.append(col)

            package = [header]
            important = burnoutToapogeeFunct(np.array(df))
            important = list(important)
            important.insert(0, header)


            #for i in range(0, len(header)):
                #print(header[i], "is index", i)

            burnalt = important[1][22]
            take1 = 22
            element = []
            for i in range(1, len(important)):
                element.append(important[i][take1])

            print(file)



            apogee = element.index(max(element))

            element2 = []
            take = 0
            for i in range(1, len(important)):
                element2.append(important[i][take])

            element3 = []
            take = 18
            for i in range(1, len(important)):
                element3.append(important[i][take])

            opttime = 0
            for i in range(1, len(element)):
                if element[i] - 10000 >0:
                    opttime = i
                    break

            vels = []
            for i in range(1, len(important)):
                vels.append(important[i][18])




            burnout = element3.index(max(element3))
            timer = element2[apogee] - element2[burnout]
            timer2 = element2[opttime]-element2[burnout]
            vb = max(vels)
            #print("")
            #print("Maximum of ", header[take1], "for", file, "is", max(element))
            #print("Time from Burnout to Apogee: ", timer)
            #print("Time from Burnout to 10,000 ft: ", timer2)
            #print("")
            print("")
            info.append(str(max(element)) + ",")
            info.append(str(timer) + ",")
            info.append(str(timer2) + ",")
            info.append(str(vb) + ",")
            info.append(burnalt)
            bigblock.append(info)

#bigblock = np.array(bigblock)
print(bigblock)
with open('DataCSV.csv', 'w') as f:
    for i in range(0, len(bigblock)):
        for j in range(0, len(bigblock[i])):
            f.write(str(bigblock[i][j]))
        f.write('\n')




