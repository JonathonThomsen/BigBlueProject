import keyboard
import time
from pywinauto.application import Application

'''
Get All of the Following Data:
rocketpath = ["M1419 Base", "M1600 Base", "M2000 Base", "M2400 Base"]
enginepath = ["AeroTech_M1419W.eng", "AeroTech_M1600R.eng", "AeroTech_M2000R.eng", "AeroTech_M2400T.eng"]
apppath = "C:/Users/jtkin/Documents/Capstone/Project/RASAero II/RASAero II.exe"
outputpath = "C:/Users/jtkin/Documents/Capstone/Project/Base Cases/1419 Weights/Trial.CSV"
CG = [
    # "72.05",
    # "72.05",
    # "73.62"
    "71.26"
]

weights = [
    # ["45.03", "47.03", "49.03", "51.03", "53.03", "55.03"],
    # ["45.03", "47.03", "49.03", "51.03", "53.03", "55.03"],
    # ["49.60", "51.60", "53.60", "55.60", "57.60", "59.60"]
    ["44.00", "46.00", "48.00", "50.00", "52.00", "54.00"]
]
           
crosswind = ["0", "4", "8", "12", "16", "20"]
'''


def repeatKeyboardInput(keyName, repeatNum):
    for kiki in range(repeatNum):
        keyboard.send(keyName)


class RASAero_study:
    def __init__(self, rocket_path, engine_path, RASAero_path, output_path, sustainer_CG, rocket_weight, wind_speed):
        self.rocket_files = rocket_path
        self.engine_files = engine_path
        self.application = RASAero_path
        self.output_file = output_path
        self.CG = [sustainer_CG]
        self.weights = rocket_weight
        self.windy = wind_speed
        self.app = Application(backend="uia").start(self.application)
        self.main_window = self.app.RASAero
        self.master()
    def runsimfromflightscreen(self, weight, crosswind, rocket):
        repeatKeyboardInput("tab", 7)
        self.main_window.child_window(title="ViewData Row 0", top_level_only=False).click_input()
        keyboard.send("alt+f")
        keyboard.send("enter")
        keyboard.send("enter")
        keyboard.send("tab")
        keyboard.send("enter")
        print("Input")
        print(self.engine_files)
        print(self.weights[rocket][weight])
        print(crosswind)
        keyboard.write(self.engine_files[rocket][:-4] + "-Wt" + self.weights[rocket][weight] + "-CW" + crosswind)
        time.sleep(5)
        keyboard.send("enter")
        keyboard.send("left")
        keyboard.send("enter")
        keyboard.send("alt+f4")
    def master(self):
        self.main_window.Menu.File.click_input()
        # keyboard.send("Alt+F")
        repeatKeyboardInput("down", 2)
        keyboard.send("enter")
        keyboard.write(self.rocket_files)
        time.sleep(5)
        keyboard.send("enter")
        for currentrocket in range(len(self.engine_files)):
            self.main_window.Menu.File.click_input()
            repeatKeyboardInput("tab", 5)
            keyboard.send("enter")
            keyboard.write(self.engine_files[currentrocket])
            time.sleep(5)
            keyboard.send("enter")
            # Clicking Flight Simulation
            self.main_window.ToolStrip1.Button8.click_input(double=True)
            for current_weight in range(len(self.weights[currentrocket])):
                print(current_weight)
                print(self.weights)
                self.main_window.child_window(title="Motor(s) Loaded Row 0", top_level_only=False).click_input(
                    double=True)
                keyboard.send("down")
                keyboard.send("enter")
                keyboard.send("tab")
                repeatKeyboardInput("right", 5)
                repeatKeyboardInput("backspace", 5)
                keyboard.write(self.CG[currentrocket])
                time.sleep(5)
                repeatKeyboardInput("tab", 2)
                repeatKeyboardInput("right", 5)
                repeatKeyboardInput("backspace", 5)
                keyboard.write(self.weights[currentrocket][current_weight])
                time.sleep(5)
                repeatKeyboardInput("tab", 2)
                keyboard.send("enter")
                for current_wind in range(0, len(self.windy)):
                    keyboard.send("alt")
                    keyboard.send("enter")
                    keyboard.send("enter")
                    repeatKeyboardInput("tab", 5)
                    repeatKeyboardInput("right", 5)
                    repeatKeyboardInput("backspace", 5)
                    keyboard.write(self.windy[current_wind])
                    time.sleep(5)
                    repeatKeyboardInput("tab", 5)
                    keyboard.send("enter")
                    keyboard.send("alt")
                    keyboard.send("tab")
                    keyboard.send("enter")
                    keyboard.send("enter")
                    self.runsimfromflightscreen(current_weight, self.windy[current_wind], currentrocket)
                keyboard.send("tab")
                keyboard.send("enter")
            keyboard.send("alt+f4")
            keyboard.send("enter")
            self.main_window.Menu.File.click_input()
            repeatKeyboardInput("tab", 2)
            keyboard.send("enter")
            keyboard.send("tab")
            keyboard.send("enter")


rkp = ["M1419 Base"]
engp = ["AeroTech_M1419W.eng", "AeroTech_M1600R.eng", "AeroTech_M2000R.eng", "AeroTech_M2400T.eng"]
applicary = "C:/Users/jtkin/Documents/Capstone/Project/RASAero II/RASAero II.exe"
out = "C:/Users/jtkin/Documents/Capstone/Project/Base Cases/1419 Weights/Trial.CSV"

# One CG for each motor type
CG = ["72.05"]
# One list of Weights for each motor type
weighty = [["45.03"]]
cross = ["0"]
print(engp[0][:-4])
study = RASAero_study(rkp, engp, applicary, out, CG, weighty, cross)
