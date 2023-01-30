import csv
import random
import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt
from PIL import Image, ImageTk


def get_file_columns(filename):
    with open(filename) as file:
        rows = list(csv.reader(file))
        file.close()
        return rows[0]


class capstoneGUI:

    def __init__(self):
        self.parent = tk.Tk()
        self.block_x = 25
        self.block_y = 150
        self.theme = True
        self.choice = None
        self.dropdown = None
        self.filename = None
        self.x_axis = None
        self.y_axis = None
        self.burnout = None
        self.sections = None
        self.regime_options = None
        self.regimes = None
        self.view_options = None
        self.max_alt = None
        self.study_options = None
        self.min_val = None
        self.max_val = None
        self.int_val = None
        self.dropdownY = None
        self.var_study_list = None
        self.dropdownX = None
        self.column = 0
        self.setup()

    def restart(self):
        self.theme = not self.theme
        self.reset_children()
        self.block_x = 25
        self.block_y = 150
        self.setup()
        self.step1()

    def reset_children(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def color(self, regime):
        themes = self.theme
        if themes:
            if regime == "p":
                return "#05244a"
            elif regime == "s":
                return "#c0bcb3"
            elif regime == "t":
                return "#fefeff"
        else:
            red = int(100 * random.random())
            if red < 10:
                red = 10 + red
            green = int(100 * random.random())
            if green < 10:
                green = 10 + green
            blue = int(100 * random.random())
            if blue < 10:
                blue = 10 + blue
            num = "#" + str(red) + str(green) + str(blue)
            return num

    def selection(self):
        self.block_y = self.block_y + 75
        self.choice = self.dropdown.get(tk.ANCHOR)
        self.step2()

    def step1(self):
        tk.Label(self.parent, text="Choose an Option: ", bg=self.color("s"), relief=tk.RAISED).place(x=self.block_x,
                                                                                                     y=self.block_y)
        options = ["View Data", "Variable Study", "Deceleration"]
        self.dropdown = tk.Listbox(self.parent, selectmode="single", bg=self.color("s"), height=len(options),
                                   font='Times, 8',
                                   relief=tk.RAISED)
        self.dropdown.place(x=self.block_x + 150, y=self.block_y)
        for op in range(len(options)):
            self.dropdown.insert(tk.END, options[op])
            self.dropdown.itemconfig(op)

        select = tk.Button(self.parent, text="Continue", bg=self.color("t"), command=self.selection, relief=tk.RAISED)
        select.place(x=self.block_x + 275, y=self.block_y)

    def setup(self):
        self.parent.title('USUSpACe')
        self.parent.geometry('1250x1000')
        self.parent.config(bg=self.color("p"))
        tk.Label(self.parent, text="The Official USU SpACe Design and Rocket Performance Analyzer (DRPA)",
                 bg=self.color("s"),
                 font='Times, 18', relief=tk.RAISED).pack(padx=50, side=tk.TOP)
        image_label = tk.Label(self.parent, height=100, width=133)
        logo = (Image.open('USU LOGO.jpg'))
        formatted_logo = logo.resize((140, 110))
        image_label.image = ImageTk.PhotoImage(formatted_logo)
        image_label['image'] = image_label.image
        image_label.place(x=0, y=0)
        group_label = tk.Label(self.parent, height=100, width=133)
        group = (Image.open('SpACe.png'))
        formatted_group = group.resize((140, 110))
        group_label.image = ImageTk.PhotoImage(formatted_group)
        group_label['image'] = group_label.image
        group_label.place(x=1250, y=0)
        if self.theme:
            select = tk.Button(self.parent, text="Restart (Party Mode!)", bg=self.color("t"), command=self.restart,
                               relief=tk.RAISED)
        else:
            select = tk.Button(self.parent, text="Restart", bg=self.color("t"), command=self.restart,
                               relief=tk.RAISED)

        select.place(x=500, y=50)

        self.step1()
        self.parent.mainloop()
        return self.parent

    def confirm(self):
        self.block_y = self.block_y + 50
        self.step3()

    def file_browser(self):
        self.block_y = self.block_y + 25
        self.filename = tk.filedialog.askopenfilename(initialdir="/",
                                                      title="Select a File",
                                                      filetypes=((".csv",
                                                                  "*.csv*"),
                                                                 ("all files",
                                                                  "*.*")))
        path = tk.Entry(self.parent, bg=self.color("s"), width=50, relief=tk.RAISED)
        path.insert(tk.END, self.filename)
        path.place(x=self.block_x + 150, y=self.block_y)
        confirm = tk.Button(self.parent, bg=self.color("t"), text="Load File", command=self.confirm, relief=tk.RAISED)
        confirm.place(x=self.block_x + 150, y=self.block_y + 25)

    def step2(self):

        tk.Label(self.parent, bg=self.color("s"), text="Select a file: ", relief=tk.RAISED).place(x=self.block_x,
                                                                                                  y=self.block_y)
        browse = tk.Button(self.parent, bg=self.color("t"), text="Browse", command=self.file_browser,
                           relief=tk.RAISED)
        browse.place(x=self.block_x + 150, y=self.block_y)

    def menu_selection_x(self):
        self.x_axis = self.dropdownX.get(tk.ANCHOR)
        self.dropdown_Y_block()

    def plotter(self):

        with open(self.filename) as file:
            rows = list(csv.reader(file))
            all_data = list(zip(*rows))
            all_data = [list(i) for i in all_data]

            file.close()

        for i in range(len(all_data)):
            if all_data[i][0] == "Thrust (lb)":
                for j in range(2, len(all_data[i])):
                    if float(all_data[i][j]) == 0:
                        self.burnout = j
                        break
                break
        for i in range(len(all_data)):
            if all_data[i][0] == "Altitude (ft)":
                temp = [float(all_data[i][j]) for j in range(1, len(all_data[i]))]
                self.max_alt = temp.index(max(temp))
                break

        plt.clf()
        x_list = []
        y_list = []
        if 'Liftoff to Burnout' in self.sections:
            powered_x = []
            powered_y = []
            for i in range(0, len(all_data)):
                if all_data[i][0] == self.x_axis:
                    for j in range(1, self.burnout + 1):
                        powered_x.append(float(all_data[i][j]))
                        x_list.append(float(all_data[i][j]))
                if all_data[i][0] == self.y_axis:
                    for j in range(1, self.burnout + 1):
                        powered_y.append(float(all_data[i][j]))
                        y_list.append(float(all_data[i][j]))
            plt.plot(powered_x, powered_y, color='red', label="Liftoff to Burnout")
        if 'Burnout to Apogee' in self.sections:
            unpowered_x = []
            unpowered_y = []
            for i in range(0, len(all_data)):
                if all_data[i][0] == self.x_axis:
                    for j in range(self.burnout + 1, self.max_alt + 1):
                        unpowered_x.append(float(all_data[i][j]))
                        x_list.append(float(all_data[i][j]))
                if all_data[i][0] == self.y_axis:
                    for j in range(self.burnout + 1, self.max_alt + 1):
                        unpowered_y.append(float(all_data[i][j]))
                        y_list.append(float(all_data[i][j]))
            plt.plot(unpowered_x, unpowered_y, color='green', label="Burnout to Apogee")
        if 'Apogee to Landing' in self.sections:
            falling_x = []
            falling_y = []
            for i in range(0, len(all_data)):
                if all_data[i][0] == self.x_axis:
                    for j in range(self.max_alt + 1, len(all_data[i])):
                        falling_x.append(float(all_data[i][j]))
                        x_list.append(float(all_data[i][j]))
                if all_data[i][0] == self.y_axis:
                    for j in range(self.max_alt + 1, len(all_data[i])):
                        falling_y.append(float(all_data[i][j]))
                        y_list.append(float(all_data[i][j]))
            plt.plot(falling_x, falling_y, color='black', label="Apogee to Landing")
        tk.Label(self.parent, text=self.x_axis, bg=self.color("t"),
                 font='Times, 10', relief=tk.RAISED, width=25).place(x=self.block_x, y=self.block_y)
        tk.Label(self.parent, text="Maximum: " + str(round(max(x_list), 2)), bg=self.color("t"),
                 font='Times, 10', relief=tk.RAISED, width=15).place(x=self.block_x + 300, y=self.block_y)
        tk.Label(self.parent, text="Minimum: " + str(round(min(x_list), 2)), bg=self.color("t"),
                 font='Times, 10', relief=tk.RAISED, width=15).place(x=self.block_x + 175, y=self.block_y)

        tk.Label(self.parent, text=self.y_axis, bg=self.color("t"),
                 font='Times, 10', relief=tk.RAISED, width=25).place(x=self.block_x, y=self.block_y + 25)
        tk.Label(self.parent, text="Maximum: " + str(round(max(y_list), 2)), bg=self.color("t"),
                 font='Times, 10', relief=tk.RAISED, width=15).place(x=self.block_x + 300, y=self.block_y + 25)
        tk.Label(self.parent, text="Minimum: " + str(round(min(y_list), 2)), bg=self.color("t"),
                 font='Times, 10', relief=tk.RAISED, width=15).place(x=self.block_x + 175, y=self.block_y + 25)

        plt.xlabel(self.x_axis)
        plt.ylabel(self.y_axis)
        plt.legend()
        plt.show()

    def regime_selection(self):
        self.sections = [self.regime_options[i] for i in self.regimes.curselection()]
        self.block_y = 575
        self.plotter()

    def flight_regimes(self):
        self.block_y = self.block_y + 100
        tk.Label(self.parent, text="Flight Regime: ", bg=self.color("t"),
                 font='Times, 10', relief=tk.RAISED).place(x=self.block_x, y=self.block_y + 25)
        self.regime_options = ["Liftoff to Burnout", "Burnout to Apogee", "Apogee to Landing"]
        self.regimes = tk.Listbox(self.parent, selectmode="multiple", bg=self.color("s"),
                                  height=len(self.regime_options), font='Times, 8')
        self.regimes.place(x=self.block_x + 150, y=self.block_y + 25)
        for op in range(len(self.regime_options)):
            self.regimes.insert(tk.END, self.regime_options[op])
            self.regimes.itemconfig(op)

        select = tk.Button(self.parent, text="Continue", bg=self.color("t"), command=self.regime_selection)
        select.place(x=self.block_x + 275, y=self.block_y + 25)

    def menu_selection_y(self):
        self.y_axis = self.dropdownY.get(tk.ANCHOR)
        self.flight_regimes()

    def dropdown_Y_block(self):
        self.block_y = self.block_y + 100
        tk.Label(self.parent, text="Y-Axis Variable: ", bg=self.color("t"),
                 font='Times, 10', relief=tk.RAISED).place(x=self.block_x, y=self.block_y + 25)
        self.dropdownY = tk.Listbox(self.parent, selectmode="single", bg=self.color("s"), height=5, width=25,
                                    font='Times, 8',
                                    relief=tk.RAISED)
        self.dropdownY.place(x=self.block_x + 150, y=self.block_y + 25)
        y_scroll = tk.Scrollbar(self.parent, orient="vertical", relief=tk.RAISED)
        y_scroll.config(command=self.dropdownY.yview)
        y_scroll.place(x=self.block_x + 305, y=self.block_y + 25)
        self.dropdownY.config(yscrollcommand=y_scroll.set)
        for op in range(len(self.view_options)):
            self.dropdownY.insert(tk.END, self.view_options[op])
            self.dropdownY.itemconfig(op)

        select = tk.Button(self.parent, text="Continue", bg=self.color("t"), command=self.menu_selection_y,
                           relief=tk.RAISED)
        select.place(x=self.block_x + 325, y=self.block_y + 25)

    def max_min(self):
        floor = self.min_val.get()
        ceiling = self.max_val.get()
        step = self.int_val.get()
        print(floor)
        print(ceiling)
        print(step)


    def max_min_block(self):
        spacer = 350
        for column in range(len(self.studies)):
            tk.Label(self.parent, text="Enter Minimum Value for " + self.studies[column] + ": ", bg=self.color("t"),
                     font='Times, 10', relief=tk.RAISED).place(x=self.block_x+(column*spacer), y=self.block_y + 100)
            self.min_val = tk.Entry(self.parent, bg=self.color("s"), width=10, relief=tk.RAISED)
            self.min_val.place(x=self.block_x + 225 + (column*spacer), y=self.block_y + 100)

            tk.Label(self.parent, text="Enter Maximum Value for " + self.studies[column] + ": ", bg=self.color("t"),
                     font='Times, 10', relief=tk.RAISED).place(x=self.block_x + (column*spacer), y=self.block_y + 125)
            self.max_val = tk.Entry(self.parent, bg=self.color("s"), width=10, relief=tk.RAISED)
            self.max_val.place(x=self.block_x + 225+ (column*spacer), y=self.block_y + 125)
            tk.Label(self.parent, text="Enter Interval:", bg=self.color("t"),
                     font='Times, 10', relief=tk.RAISED).place(x=self.block_x+ (column*spacer), y=self.block_y + 150)
            self.int_val = tk.Entry(self.parent, bg=self.color("s"), width=10, relief=tk.RAISED)
            self.int_val.place(x=self.block_x + 225+ (column*spacer), y=self.block_y + 150)
            self.max_min()
            confirm = tk.Button(self.parent, bg=self.color("t"), text="Execute", command=self.max_min,
                            relief=tk.RAISED)
            confirm.place(x=self.block_x + 150 + (column*spacer), y=self.block_y + 175)




    def vs_selection(self):
        self.studies = [self.study_options[i] for i in self.var_study_list.curselection()]
        self.max_min_block()


    def step3(self):
        if self.choice == "View Data":
            tk.Label(self.parent, text="Data Viewer. ", bg=self.color("t"),
                     font='Times, 10', relief=tk.RAISED).place(x=self.block_x, y=self.block_y)

            tk.Label(self.parent, text="X-Axis Variable: ", bg=self.color("t"),
                     font='Times, 10', relief=tk.RAISED).place(x=self.block_x, y=self.block_y + 25)

            self.view_options = get_file_columns(self.filename)
            self.dropdownX = tk.Listbox(self.parent, selectmode="single", bg=self.color("s"), height=5, width=25,
                                        font='Times, 8',
                                        relief=tk.RAISED)
            self.dropdownX.place(x=self.block_x + 150, y=self.block_y + 25)
            x_scroll = tk.Scrollbar(self.parent, orient="vertical", relief=tk.RAISED)
            x_scroll.config(command=self.dropdownX.yview)
            x_scroll.place(x=self.block_x + 305, y=self.block_y + 25)
            self.dropdownX.config(yscrollcommand=x_scroll.set)
            for op in range(len(self.view_options)):
                self.dropdownX.insert(tk.END, self.view_options[op])
                self.dropdownX.itemconfig(op)

            select = tk.Button(self.parent, text="Continue", bg=self.color("t"), command=self.menu_selection_x,
                               relief=tk.RAISED)
            select.place(x=self.block_x + 325, y=self.block_y + 25)

        elif self.choice == "Variable Study":
            tk.Label(self.parent, text="Variable Study. ", bg=self.color("t"),
                     font='Times, 10', relief=tk.RAISED).place(x=self.block_x, y=self.block_y)
            tk.Label(self.parent, text="What is to be varied?", bg=self.color("t"),
                     font='Times, 10', relief=tk.RAISED).place(x=self.block_x, y=self.block_y + 25)
            self.study_options = ["Weight", "Crosswind", "Motor"]

            self.var_study_list = tk.Listbox(self.parent, selectmode="multiple", bg=self.color("s"),
                                             height=len(self.study_options),
                                             font='Times, 8',
                                             relief=tk.RAISED)
            self.var_study_list.place(x=self.block_x + 150, y=self.block_y + 25)
            for op in range(len(self.study_options)):
                self.var_study_list.insert(tk.END, self.study_options[op])
                self.var_study_list.itemconfig(op)

            select = tk.Button(self.parent, text="Continue", bg=self.color("t"), command=self.vs_selection,
                               relief=tk.RAISED)
            select.place(x=self.block_x + 275, y=self.block_y + 25)

            # Prompt the user to select which variable to study
            # Prompt the user for minimum and maximum values
            # Prompt the user for interval
        elif self.choice == "Deceleration":
            tk.Label(self.parent, text="Deceleration. ", bg=self.color("t"),
                     font='Times, 10', relief=tk.RAISED).place(x=self.block_x, y=self.block_y)
            # Prompt the user for inputs from rocket toolkit program


capstoneGUI()
