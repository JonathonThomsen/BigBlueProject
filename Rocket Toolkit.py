import math
import matplotlib.pyplot as plt
import numpy as np


def deployangle(brakearea, time, base, ttfd, top):
    ttfd = ttfd * (top / 90)
    if time < ttfd:

        topangle = top * math.pi/180
        theta = topangle * (time / ttfd)
        area = base + (4 * brakearea * math.sin(theta))
    else:

        topangle = top * math.pi / 180
        theta = topangle
        area = base + (4 * brakearea * math.sin(theta))

    return area, theta*180/math.pi


def plots():
    figure, axis = plt.subplots(2,2)
    for i in range(0, len(totalvelsACS)):
        name = str(tops[i]) + " Degree Deployment Angle"
        axis[0,0].plot(totaltimes[i], totalvelsACS[i], label=name)
    axis[0, 0].plot(totaltimes[-1], totalvelsB[-1], "r", label="Without ACS")
    axis[0, 0].set_title(" Vertical Velocity (After Burnout)")
    axis[0, 0].legend(loc="upper right")
    axis[0, 0].set_xlabel("Time after Burnout (Seconds)")
    axis[0, 0].set_ylabel("Velocity (Feet/Second)")
    for i in range(0, len(totalAltsB)):
        name = str(tops[i]) + " Degree Deployment Angle"
        axis[0, 1].plot(totaltimes[i], totalAltsACS[i], label=name)
    axis[0,1].plot(totaltimes[-1], totalAltsB[-1], "r", label="Without ACS")

    axis[0,1].set_title("Altitude (After Burnout)")
    axis[0, 1].legend(loc="upper right")
    axis[0, 1].set_xlabel("Time after Burnout (Seconds)")
    axis[0, 1].set_ylabel("Altitude (Feet)")
    for i in range(0, len(totalarealist)):
        axis[1, 0].plot(totaltimes[i], totalarealist[i])
        #, label="Normal Area"
    axis[1, 0].set_title("Frontal Area (After Burnout)")
    axis[1, 0].set_ylabel("Area (Square Inches)")
    axis[1, 0].set_xlabel("Time after Burnout (Seconds)")
    for i in range(0, len(totalthetalist)):
        axis[1,1].plot(totaltimes[i], totalthetalist[i])
    axis[1,1].set_title("Airbrake Deployment Angle (After Burnout)")
    axis[1, 1].set_xlabel("Time after Burnout (Seconds)")
    axis[1, 1].set_ylabel("Angle (Degrees)")
    plt.show()


top = 90



base = math.pi * (3.1 ** 2)
brakearea = 4
Cd = 0.17
dt = .01
m = 45.95
ttfd = 3
CdA = 0.2
densities = [0.0018687, 0.0018116, 0.0017558, 0.0017013, 0.0016482, 0.0015963, 0.0015457, 0.0014963, 0.0014482, 0.001400, 0.001400, 0.001400 ]

totalarealist = []
totaltimes = []
totalvelsACS = []
totalvelsB = []
totalAltsACS= []
totalAltsB = []
totalthetalist = []
tops = []
first = True
while first or totalvelsB[-1][-1]> 0:
    if top > 90:
        break
    first = False
    VelACS = 927.1163
    AltACS = 5233.272
    VelB = VelACS
    AltB = AltACS
    tops.append(top)
    dragACS = [0]
    arealist = [base]
    times = [0]
    velsACS = [VelACS]
    velsB = [VelB]
    AltsACS= [AltACS]
    AltsB = [AltB]
    thetalist = [0]
    time = 0
    while velsB[-1] > 0:
        area, theta = deployangle(brakearea, time, base, ttfd, top)
        densityACS = densities[int((AltACS - 4000) / 1000)]
        densityB = densities[int((AltB-4000)/1000)]
        FdACS = .5 * CdA * (VelACS**2) * densityACS * area
        FdB = .5 * Cd * (VelB ** 2) * densityB * base
        VelACS = VelACS - (FdACS * dt / m) - (32.174 * dt)
        VelB = VelB - (FdB * dt / m) - (32.174 * dt)
        AltACS = AltACS + (VelACS * dt)
        AltB = AltB + (VelB * dt)
        time = time + dt
        times.append(time)
        arealist.append(area)
        velsACS.append(VelACS)
        velsB.append(VelB)
        AltsACS.append(AltACS)
        AltsB.append(AltB)
        thetalist.append(theta)
        dragACS.append(FdACS)
    totalarealist.append(arealist)
    totaltimes.append(times)
    totalvelsACS.append(velsACS)
    totalvelsB.append(velsB)
    totalAltsACS.append(AltsACS)
    totalAltsB.append(AltsB)
    totalthetalist.append(thetalist)
    print(top)
    top = top +10

    # input()
"""
altdiff = []
veldiff = []
for i in range(0, len((AltsB))):
    veldiff.append(velsB[i]-velsACS[i])
    altdiff.append(AltsB[i]-AltsACS[i])
altint = np.trapz(altdiff, times)
velint = np.trapz(veldiff, times)

print("Apogee Delta: ", velint)
print("Average Deceleration: ", velint/times[-1], " Ft/s^2")
print("Final Apogee (With Max ACS Deployment): ", AltsACS[-1])
"""
for i in range(0, len(totalAltsACS)):
    print(totalAltsACS[i])
    print(totaltimes[i])
    print(max(totalAltsB[0]))
print(dragACS)
plots()


