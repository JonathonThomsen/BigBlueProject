from numpy import linspace
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

def aerodrag(height, velocity, option):
    print(height)
    if option == False:
        density = 0
    else:
        density = 1.2
        #density = -((3*10**-24)*height**5) + ((7*10**-19)*height**4) - ((8*10**-14)*height**3) + ((5*10**-9)*height**2) - (0.0001*height) + 1.2284
    drag = .5 * CD * density * (velocity**2) * area
    #print(drag)
    return drag
'''
Example Problem:
Constant thrust of 500 Newtons
Total Burn Time of 10 Seconds
10 kg of fuel
Empty mass is 20 kg
0 degree yz pitch at start
0 degree xz pitch at start
'''
CD = 0.00075
area = 1
trajectoryposburn = [[0, 0, 0]]
trajectoryvelburn = [[0, 0, 0]]
trajectoryaccburn = [[0, 0, 0]]
trajectoryposglide = []
trajectoryvelglide = []
trajectoryaccglide = []
totalburntime = 2 # Seconds
phi = 1 * (math.pi/180)
theta = 0 * (math.pi/180)
time = [0]
fuel = 1000 # Kg
totalmass = [10+fuel]
emptymass = totalmass[-1] - fuel
mdot = fuel/totalburntime # Kg/s
thrust = 50000 # Newtons
dt = .0001
glide = False
inflight = True
account = True
while inflight == True:
    time.append(time[-1] + dt)

    if totalmass[-1] > emptymass:
        dragaccel = 2 #aerodrag(trajectoryposburn[-1][2], trajectoryvelburn[-1][2], account)/totalmass[-1]
        up = math.cos(phi)
        over = math.sin(phi)
        intermediateacc = []
        intermediateacc.append(trajectoryaccburn[-1][0] + ((thrust * over * math.cos(theta)) / (totalmass[-1])))
        intermediateacc.append(trajectoryaccburn[-1][1] + ((thrust * over * math.sin(theta)) / (totalmass[-1])))
        intermediateacc.append(trajectoryaccburn[-1][2] + ((thrust * up) / (totalmass[-1])) - 9.81 - dragaccel)
        trajectoryaccburn.append(intermediateacc)
        intermediatevel = []
        intermediatevel.append(trajectoryvelburn[-1][0] + trajectoryaccburn[-1][0] * dt)
        intermediatevel.append(trajectoryvelburn[-1][1] + trajectoryaccburn[-1][1] * dt)
        intermediatevel.append(trajectoryvelburn[-1][2] + trajectoryaccburn[-1][2] * dt)
        trajectoryvelburn.append(intermediatevel)
        intermediatepos = []
        intermediatepos.append(trajectoryposburn[-1][0] + (.5 * trajectoryaccburn[-1][0] * (dt ** 2)))
        intermediatepos.append(trajectoryposburn[-1][1] + (.5 * trajectoryaccburn[-1][1] * (dt ** 2)))
        intermediatepos.append(trajectoryposburn[-1][2] + (.5 * trajectoryaccburn[-1][2] * (dt ** 2)))
        trajectoryposburn.append(intermediatepos)
        totalmass.append(totalmass[-1] - (mdot * dt))

    else:
        if glide == True:
            dragaccel = 2 #aerodrag(trajectoryposglide[-1][2], trajectoryvelglide[-1][2], account) / totalmass[-1]
            intermediateacc = []
            intermediateacc.append(trajectoryaccglide[-1][0])
            intermediateacc.append(trajectoryaccglide[-1][1])
            intermediateacc.append(trajectoryaccglide[-1][2] - 9.81 - dragaccel)
            trajectoryaccglide.append(intermediateacc)
            intermediatevel = []
            intermediatevel.append(trajectoryvelglide[-1][0] + trajectoryaccglide[-1][0] * dt)
            intermediatevel.append(trajectoryvelglide[-1][1] + trajectoryaccglide[-1][1] * dt)
            intermediatevel.append(trajectoryvelglide[-1][2] + trajectoryaccglide[-1][2] * dt)
            trajectoryvelglide.append(intermediatevel)
            intermediatepos = []
            intermediatepos.append(trajectoryposglide[-1][0] + (.5 * trajectoryaccglide[-1][0] * (dt ** 2)))
            intermediatepos.append(trajectoryposglide[-1][1] + (.5 * trajectoryaccglide[-1][1] * (dt ** 2)))
            intermediatepos.append(trajectoryposglide[-1][2] + (.5 * trajectoryaccglide[-1][2] * (dt ** 2)))
            trajectoryposglide.append(intermediatepos)
            if intermediatepos[2]<=0:
                inflight = False

        else:
            thrust = 0
            dragaccel = 2 #aerodrag(trajectoryposburn[-1][2], trajectoryvelburn[-1][2], account) / totalmass[-1]
            glidetime = time[-1]
            intermediateacc = []
            intermediateacc.append(trajectoryaccburn[-1][0])
            intermediateacc.append(trajectoryaccburn[-1][1])
            intermediateacc.append(trajectoryaccburn[-1][2] - 9.81 - dragaccel)
            trajectoryaccglide.append(intermediateacc)
            intermediatevel = []
            intermediatevel.append(trajectoryvelburn[-1][0] + trajectoryaccburn[-1][0] * dt)
            intermediatevel.append(trajectoryvelburn[-1][1] + trajectoryaccburn[-1][1] * dt)
            intermediatevel.append(trajectoryvelburn[-1][2] + trajectoryaccburn[-1][2] * dt)
            trajectoryvelglide.append(intermediatevel)
            intermediatepos = []
            intermediatepos.append(trajectoryposburn[-1][0] + (.5 * trajectoryaccburn[-1][0] * (dt ** 2)))
            intermediatepos.append(trajectoryposburn[-1][1] + (.5 * trajectoryaccburn[-1][1] * (dt ** 2)))
            intermediatepos.append(trajectoryposburn[-1][2] + (.5 * trajectoryaccburn[-1][2] * (dt ** 2)))
            trajectoryposglide.append(intermediatepos)
            glide = True
        totalmass.append(totalmass[-1])
    if trajectoryposburn[-1][2] <= 0:
        break



fig = plt.figure()


trajectory = fig.add_subplot(2, 2, 1, projection='3d')
acc = fig.add_subplot(2, 2, 2)
vel = fig.add_subplot(2, 2, 3)
fuel = fig.add_subplot(2, 2, 4)
xaccburn = [trajectoryaccburn[i][0] for i in range(0, len(trajectoryaccburn))]
yaccburn = [trajectoryaccburn[i][1] for i in range(0, len(trajectoryaccburn))]
zaccburn = [trajectoryaccburn[i][2] for i in range(0, len(trajectoryaccburn))]
xaccglide = [trajectoryaccglide[i][0] for i in range(0, len(trajectoryaccglide))]
yaccglide = [trajectoryaccglide[i][0] for i in range(0, len(trajectoryaccglide))]
zaccglide = [trajectoryaccglide[i][0] for i in range(0, len(trajectoryaccglide))]

xvelburn = [trajectoryvelburn[i][0] for i in range(0, len(trajectoryvelburn))]
yvelburn = [trajectoryvelburn[i][1] for i in range(0, len(trajectoryvelburn))]
zvelburn = [trajectoryvelburn[i][2] for i in range(0, len(trajectoryvelburn))]
xvelglide = [trajectoryvelglide[i][0] for i in range(0, len(trajectoryvelglide))]
yvelglide = [trajectoryvelglide[i][1] for i in range(0, len(trajectoryvelglide))]
zvelglide = [trajectoryvelglide[i][2] for i in range(0, len(trajectoryvelglide))]

xposburn = [trajectoryposburn[i][0] for i in range(0, len(trajectoryposburn))]
yposburn = [trajectoryposburn[i][1] for i in range(0, len(trajectoryposburn))]
zposburn = [trajectoryposburn[i][2] for i in range(0, len(trajectoryposburn))]
xposglide = [trajectoryposglide[i][0] for i in range(0, len(trajectoryposglide))]
yposglide = [trajectoryposglide[i][1] for i in range(0, len(trajectoryposglide))]
zposglide = [trajectoryposglide[i][2] for i in range(0, len(trajectoryposglide))]

burntime = [time[i] for i in range(0, len(zposburn))]
glidetime = [time[i] for i in range(len(zposburn), len(time))]
trajectory.plot(xposburn, yposburn, zposburn, color='red')
trajectory.plot(xposglide, yposglide, zposglide, color='blue')
trajectory.title.set_text("Trajectory")

acc.plot(burntime, xaccburn, label='X_Burn')
acc.plot(burntime, yaccburn, label='Y_Burn')
acc.plot(burntime, zaccburn, label='Z_Burn')
acc.plot(glidetime, xposglide, label='X_Glide')
acc.plot(glidetime, yposglide, label='Y_Glide')
acc.plot(glidetime, zposglide, label='Z_Glide')
acc.legend(loc='upper right')
acc.title.set_text("Acceleration (m/s^2)")

vel.plot(burntime, xvelburn, label='X Velocity, Burn')
vel.plot(burntime, yvelburn, label='Y Velocity, Burn')
vel.plot(burntime, zvelburn, label='Z Velocity, Burn')
vel.plot(glidetime, xvelglide, label='X Velocity, Glide')
vel.plot(glidetime, yvelglide, label='Y Velocity, Glide')
vel.plot(glidetime, zvelglide, label='Z Velocity, Glide')
vel.legend(loc='upper right')
vel.title.set_text("Velocity (m/s)")

fuel.plot(time, totalmass, label='Vehicle Mass (Kg)')
fuel.legend(loc='upper right')

print("Total Flight Time: ", time[-1], "Seconds")
print("Burnout Altitude:", zposburn[-1], "Meters")
print("Max Altitude:", max(zposglide), "Meters")
print("Burnout Velocity:", trajectoryvelburn[-1])
print("Max Velocity:", trajectoryvelburn[-1][2])
plt.show()