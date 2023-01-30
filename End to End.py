import os
import pandas as pd
import numpy as np

def burnoutToapogeeFunct(df):
    chunk = []
    for row in range(1, len(df)):
        if df[row][7] == 0:
            chunk.append(list(df[row]))
        if df[row][22] < df[row-1][22]:
            break
    return chunk

def single_study():
    return "Ok"


def large_study():
    return "Ok"


def view_study():

    directory = "C:/Users/jtkin/Documents/RASAero II"
    csv_files = []
    for file in os.listdir(directory):
        split = list(os.path.splitext(file))
        if split[1] == '.CSV':
            csv_files.append(file)

    looking = True
    while looking:
        keyword = input("Enter a search keyword: ")
        searchlist = []
        num = 0
        for i in range(0, len(csv_files)):
            if keyword in csv_files[i]:
                num = num + 1
                searchlist.append(csv_files[i])
                print(num, " - ", csv_files[i])
        further = input("Refine further? (Y/N)")
        if further == "Y":
            csv_files = searchlist
            continue
        else:
            looking = False

    selection = int(input("Type the number of your selection. "))
    filename = os.path.join(directory, csv_files[selection])
    df = pd.read_csv(filename)
    header = []
    for col in df.columns:
        header.append(col)

    df = np.array(df)
    region = input("Enter (BA) for burnout to apogee region or press enter for entire flight.")
    if region == "BA":
        important = burnoutToapogeeFunct(np.array(df))
    else:
        important = []
        for i in range(1, len(df)):
            for j in range(0, len(df[i])):
                important.append(df[i][j])

    dictionary_setup = []
    for i in range(0, 3):
        for j in range(0, 3):
            temp = important[i][j]
            print(temp)
            #dictionary_setup.append()
    print(dictionary_setup)
    input()



    return


ex = False

while ex == False:
    print("What would you like to do? Type the index of the option below and press Enter.")
    print("1 - Large Study")
    print("2 - Single Study")
    print("3 - View Results")
    print("4 - Exit the Program")
    userinput = "3" #input("Make a Selection: ")

    if userinput == "1":
        large_study()
        print("Process Complete")
        print("")
    elif userinput == "2":
        single_study()
        print("Process Complete")
        print("")


    elif userinput == "3":

        view_study()
        print("Process Complete")
        print("")
    elif userinput == "4":
        ex = True
    else:
        print("")
        print("Invalid input. Please type either 1, 2, 3, or 4.")
        print("")
        print("")
        continue
