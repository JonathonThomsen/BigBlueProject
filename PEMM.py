import math
from matplotlib import pyplot as plt

Mdry = 25
V = 1268
Z = 3479
P = Mdry * V

t = 0
zOptimal = 10000
maxDeploy = 60/180 * math.pi
timeTotarget = 6
halftime = .5 * timeTotarget
density = .0752
dt = .1
newalt = (.5 * (V**2))/( 32.217)


def thetaFunct(t, halftime, maxDeploy):
    return 0
    #return -((maxDeploy / halftime) * abs(t - halftime)) + maxDeploy


base = math.pi * (6.17 ** 2) / 144
area = 16/144
deployAngle = thetaFunct(t, halftime, maxDeploy)
dragForce = (density) * V * (base + (area* math.sin(deployAngle)) )
pos = [Z]
vel = [V]
mom = [P]
time = [t]
dep = [deployAngle]
print("Time Since Burnout: ", time)
print("Altitude: ", pos)
print("Velocity: ", vel)
print("Momentum: ", mom)
print("Deployment Angle: ", dep)
print("Drag Force: ", dragForce)
error = 1
while error > .001:
    time.append(time[-1] + dt)
    deployAngle = thetaFunct(time[-1], halftime, maxDeploy)
    dragForce = (density) * vel[-1] * (base + (area * math.sin(deployAngle)))
    P = mom[-1] - (dragForce * dt)
    mom.append(P)
    V = (mom[-1]/Mdry) - (32.17405 * time[-1])
    Z = pos[-1] + (V * dt)
    t = time[-1] + dt
    pos.append(Z)
    vel.append(V)

    dep.append(deployAngle* 180/math.pi)
    print("Time Since Burnout: ", time)
    print("Altitude: ", pos)
    print("Velocity: ", vel)
    print("Momentum: ", mom)
    print("Deployment Angle (Degrees): ", dep)
    print("Drag Force: ", dragForce)
    newalt = (.5 * (V**2))/( 32.17405)
    error = (newalt - zOptimal)/zOptimal
    print(newalt)
    input()

print(dep)
print(time)
plt.plot(time, pos)

plt.show()
# plt.plot(vel, t)
