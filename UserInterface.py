import tkinter as tk
import os
import random
from tkinter import filedialog
from PIL import Image, ImageTk

def color(regime):
    themes = True
    if themes==True:
        if regime == "p":
            return "#770077"
        elif regime == "s":
            return "#007700"
        elif regime == "t":
            return "#042315"


    red = int(100 * random.random())
    if red < 10:
        red = 10 + red
    print(red)
    green = int(100 * random.random())
    if green < 10:
        green = 10 + green
    print(green)
    blue = int(100 * random.random())
    if blue < 10:
        blue = 10 + blue
    print(blue)

    num = "#" + str(red)+str(green)+str(blue)
    return num
def multichoice(startx, starty, options):
    def selection():
        choice = [options[i] for i in list.curselection()]
        print("yay!")
        return choice
    list = tk.Listbox(parent, selectmode="multiple", bg= color("s"), height=len(options), font=('Times, 8'))
    list.place(x=startx + 150, y=starty)
    for op in range(len(options)):
        list.insert(tk.END, options[op])
        list.itemconfig(op)

    select = tk.Button(parent, text="Continue", bg=color("t"), command=selection)
    select.place(x=startx + 275, y=starty)
def singlechoice(startx, starty, options):

    list = tk.Listbox(parent, selectmode="single", bg= color("s"), height=len(options), font=('Times, 8'))
    list.place(x=startx + 150, y=starty)
    for op in range(len(options)):
        list.insert(tk.END, options[op])
        list.itemconfig(op)
    return list

def step1(startx, starty):
    def selection():
        choice = list.get(tk.ANCHOR)
        step2(startx, starty + 100, choice)
        return choice

    tk.Label(parent, text="Choose an Option: ", bg=color("s")).place(x=startx, y=starty)
    options = ["View Data", "Variable Study", "Deceleration"]
    list = tk.Listbox(parent, selectmode="single", bg= color("s"), height=len(options), font=('Times, 8'))
    list.place(x=startx + 150, y=starty)
    for op in range(len(options)):
        list.insert(tk.END, options[op])
        list.itemconfig(op)

    select = tk.Button(parent, text="Continue", bg=color("t"), command=selection)
    select.place(x=startx + 275, y=starty)


def step2(startx, starty, program):

    def browseFiles():
        def confirm():
            step3(startx, starty+100, program, filename)
        filename = tk.filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=((".CSV",
                                                          "*.csv*"),
                                                         ("all files",
                                                          "*.*")))
        path = tk.Entry(parent, bg=color("s"), width=50)
        path.insert(tk.END, filename)
        path.place(x=startx + 150, y=starty+50)
        confirm = tk.Button(parent, bg=color("t"), text="Load File", command=confirm)
        confirm.place(x=startx + 150, y=starty+75)



    tk.Label(parent, bg=color("s"), text="Select a file: ").place(x=startx, y=starty)
    checkfile = tk.Button(parent, bg=color("t"), text="Browse", command= browseFiles)
    checkfile.place(x=startx + 150, y=starty)
def flightregimes(startx, starty, choice):
    def selection():
        choice = [options[i] for i in list.curselection()]
        print("yay!")
        return choice
    options = ["Takeoff to Burnout", "Burnout to Apogee", "Apogee to Landing"]
    list = tk.Listbox(parent, selectmode="multiple", bg= color("s"), height=len(options), font=('Times, 8'))
    list.place(x=startx + 150, y=starty)
    for op in range(len(options)):
        list.insert(tk.END, options[op])
        list.itemconfig(op)

    select = tk.Button(parent, text="Continue", bg=color("t"), command=selection)
    select.place(x=startx + 275, y=starty)

def dropdownY(startx, starty, choice):
    def selection():
        choice = dropdownX.get(tk.ANCHOR)
        flightregimes(startx, starty + 100, choice)
    tk.Label(parent, text="Y-Axis Variable: ", bg=color("t"),
             font=('Times, 10')).place(x=startx, y=starty + 175)
    options = ["Gopher", "Snail", "Rabbit"]
    dropdownX = tk.Listbox(parent, selectmode="single", bg=color("s"), height=len(options), font=('Times, 8'))
    dropdownX.place(x=startx + 150, y=starty+175)
    for op in range(len(options)):
        dropdownX.insert(tk.END, options[op])
        dropdownX.itemconfig(op)

    select = tk.Button(parent, text="Continue", bg=color("t"), command=selection)
    select.place(x=startx + 275, y=starty+175)

def maxesmins(startx, starty):
    def confirm():
        floor = minval.get()
        ceiling = maxval.get()
        step = intval.get()
        print(floor)
        print(ceiling)
        print(step)
    tk.Label(parent, text="Enter Minimum Value: ", bg=color("t"),
             font=('Times, 10')).place(x=startx, y=starty + 100)
    minval = tk.Entry(parent, bg=color("s"), width=50)
    minval.place(x=startx + 150, y=starty + 100)

    tk.Label(parent, text="Enter Maximum Value: ", bg=color("t"),
             font=('Times, 10')).place(x=startx, y=starty + 125)
    maxval = tk.Entry(parent, bg=color("s"), width=50)
    maxval.place(x=startx + 150, y=starty + 125)
    tk.Label(parent, text="Enter Interval: ", bg=color("t"),
             font=('Times, 10')).place(x=startx, y=starty + 150)
    intval = tk.Entry(parent, bg=color("s"), width=50)
    intval.place(x=startx + 150, y=starty + 150)
    confirm = tk.Button(parent, bg=color("t"), text="Execute", command=confirm)
    confirm.place(x=startx + 150, y=starty + 175)



def step3(startx, starty, program, filename):

    if program == "View Data":
        def selection():
            choice = dropdownX.get(tk.ANCHOR)
            dropdownY(startx, starty + 100, choice)
        tk.Label(parent, text="Data Viewer. ", bg=color("t"),
                 font=('Times, 10')).place(x=startx, y=starty)

        tk.Label(parent, text="X-Axis Variable: ", bg=color("t"),
                 font=('Times, 10')).place(x=startx, y=starty+25)

        options = ["Gopher", "Snail", "Rabbit"]
        dropdownX = tk.Listbox(parent, selectmode="single", bg=color("s"), height=len(options), font=('Times, 8'))
        dropdownX.place(x=startx + 150, y=starty+25)
        for op in range(len(options)):
            dropdownX.insert(tk.END, options[op])
            dropdownX.itemconfig(op)

        select = tk.Button(parent, text="Continue", bg=color("t"), command=selection)
        select.place(x=startx + 275, y=starty)















    elif program == "Variable Study":
        tk.Label(parent, text="Variable Study. ", bg=color("t"),
                 font=('Times, 10')).place(x=startx, y=starty)
        tk.Label(parent, text="What is to be varied?", bg=color("t"),
                 font=('Times, 10')).place(x=startx, y=starty+25)
        options = ["Weight", "Crosswind", "Motor"]
        choice = 0

        def selection():
            choice = [options[i] for i in list.curselection()]
            print("yay!")
            maxesmins(startx, starty+25)
            return choice

        list = tk.Listbox(parent, selectmode="multiple", bg=color("s"), height=len(options), font=('Times, 8'))
        list.place(x=startx + 150, y=starty+25)
        for op in range(len(options)):
            list.insert(tk.END, options[op])
            list.itemconfig(op)

        select = tk.Button(parent, text="Continue", bg=color("t"), command=selection)
        select.place(x=startx + 275, y=starty+25)


        # Prompt the user to select which variable to study
        # Prompt the user for minimum and maximum values
        # Prompt the user for interval
    elif program == "Deceleration":
        tk.Label(parent, text="Deceleration. ", bg=color("t"),
                 font=('Times, 10')).place(x=startx, y=starty)
        # Prompt the user for inputs from rocket toolkit program




def setup():
    parent = tk.Tk()
    parent.title('USUSpACe')
    parent.geometry('300x250')
    parent.config(bg=color("p"))
    # ADD USU LOGO SOMEHOW
    tk.Label(parent, text="THE OFFICIAL USU SpACe END-TO-END PROBLEM SOLVER (USEEPS)", bg=color("s"), font=('Times, 18')).pack()

    imglabel=tk.Label(parent, height=100, width=100)
    mainimage = (Image.open('USU LOGO.jpg'))
    sizedimage = mainimage.resize((200, 200))
    imglabel.image = ImageTk.PhotoImage(sizedimage)


    imglabel['image'] = imglabel.image
    imglabel.place(x=0, y=0)
    return parent


parent = setup()
step1(100, 200)

parent.mainloop()
