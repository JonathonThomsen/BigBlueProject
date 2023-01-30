import keyboard
import time

from pywinauto.application import Application


def repeatKeyboardInput(keyName, repeatNum):
    for kiki in range(repeatNum):
        keyboard.send(keyName)


def runsimfromflightscreen(whichone, cross, rocketnum):
    repeatKeyboardInput("tab", 7)
    mainwindow.child_window(title="ViewData Row 0", top_level_only=False).click_input()
    time.sleep(1)
    keyboard.send("alt+f")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(1)
    keyboard.send("tab")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(1)
    keyboard.write(rocketpath[rocketnum] + ", " + weights[rocketnum][whichone] + " Ibs, with " + cross + " MPH Crosswind")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(1)
    keyboard.send("left")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(1)
    keyboard.send("alt+f4")
    time.sleep(1)


#rocketpath = ["M1419 Base", "M1600 Base", "M2000 Base", "M2400 Base"]
rocketpath = ["M2000 Base"]
#enginepath = ["AeroTech_M1419W.eng", "AeroTech_M1600R.eng", "AeroTech_M2000R.eng", "AeroTech_M2400T.eng"]
enginepath = ["AeroTech_M2000R.eng"]
apppath = "C:/Users/jtkin/Documents/Capstone/Project/RASAero II/RASAero II.exe"
outputpath = "C:/Users/jtkin/Documents/Capstone/Project/Base Cases/1419 Weights/Trial.CSV"
outputpath2 = "Trial"
CG = [
    #"72.05",
    #"72.05",
    "73.62"
    #"71.26"
]

weights = [
    #["45.03", "47.03", "49.03", "51.03", "53.03", "55.03"],
    #["45.03", "47.03", "49.03", "51.03", "53.03", "55.03"],
    ["49.60", "51.60", "53.60", "55.60", "57.60", "59.60"]
    #["44.00", "46.00", "48.00", "50.00", "52.00", "54.00"]
]
'''
#weights = [["45.03"],
           ["45.
           ["49.60"],
           ["44.00"]]
           '''
crosswind = ["0", "4", "8", "12", "16", "20"]
app = Application(backend="uia").start(apppath)
mainwindow = app.RASAero
mainwindow.Menu.File.click_input()
repeatKeyboardInput("down", 2)
keyboard.send("enter")
for num in range(0, len(enginepath)):
    # Loading Rocket File
    keyboard.write(rocketpath[num])
    keyboard.send("enter")

    # Loading Engine File
    mainwindow.Menu.File.click_input()
    repeatKeyboardInput("tab", 5)
    keyboard.send("enter")
    keyboard.write(enginepath[num])
    keyboard.send("enter")

    # Clicking Flight Simulation
    mainwindow.ToolStrip1.Button8.click_input(double=True)

    for i in range(0, len(weights[0])):
        mainwindow.child_window(title="Motor(s) Loaded Row 0", top_level_only=False).click_input(double=True)
        keyboard.send("tab")
        repeatKeyboardInput("right", 5)
        repeatKeyboardInput("backspace", 5)
        keyboard.write(CG[num])
        repeatKeyboardInput("tab", 2)
        repeatKeyboardInput("right", 5)
        repeatKeyboardInput("backspace", 5)
        keyboard.write(weights[num][i])
        repeatKeyboardInput("tab", 2)
        keyboard.send("enter")
        '''
        repeatKeyboardInput("tab", 7)
        mainwindow.child_window(title="ViewData Row 0", top_level_only=False).click_input()

        keyboard.send("alt+f")

        keyboard.send("enter")

        keyboard.send("enter")

        keyboard.send("tab")

        keyboard.send("enter")

        keyboard.write(rocketpath[num] + "+" + weights[i])

        keyboard.send("enter")

        keyboard.send("left")

        keyboard.send("enter")

        keyboard.send("alt+f4")
        '''
        for windy in range(0, len(crosswind)):
            keyboard.send("alt")
            keyboard.send("enter")
            keyboard.send("enter")
            repeatKeyboardInput("tab", 5)
            repeatKeyboardInput("right", 5)

            repeatKeyboardInput("backspace", 5)
            keyboard.write(crosswind[windy])

            repeatKeyboardInput("tab", 5)
            keyboard.send("enter")

            keyboard.send("alt")

            keyboard.send("tab")

            keyboard.send("enter")

            keyboard.send("enter")
            runsimfromflightscreen(i, crosswind[windy], num)

        time.sleep(5)
        keyboard.send("tab")
        time.sleep(5)
        keyboard.send("enter")
    keyboard.send("alt+f4")
    keyboard.send("enter")
    mainwindow.Menu.File.click_input()
    repeatKeyboardInput("tab", 2)
    keyboard.send("enter")
    keyboard.send("tab")
    keyboard.send("enter")
print("Sim...done.")
