import math
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas


def thrustcurve(engine):
    reader = pandas.read_csv(engine)
    thrustlist = reader.values.tolist()
    thrustlist = thrustlist[3:len(thrustlist)]
    times = [float(thrustlist[i][0]) for i in range(len(thrustlist))]
    thrusts = [float(thrustlist[i][1]) * 0.2248089431 for i in range(len(thrustlist))]
    gravity = np.interp(start_elevation, altitudes, gravities)
    ISP = (np.trapz(thrusts, times) / (wet_mass - dry_mass)) / gravity

    mass_flow_rates = [(thrust / (ISP * gravity)) for thrust in thrusts]

    return times, thrusts, mass_flow_rates


def recursive_tunnel(previous):
    # UNPACKING __________________________________________________________________
    time, z_accel, z_vel, z_pos, y_accel, y_vel, y_pos, x_accel, x_vel, x_pos, spin_vel, spin_pos, thrust, mass, \
    mass_flow_rate, dt, drag = previous

    # ENVIRONMENT DATA ___________________________________________________________
    gravity = np.interp(z_pos, altitudes, gravities)
    density = np.interp(z_pos, altitudes, densities)
    wind_x, wind_y, spin_accel = environment(wind, z_pos)
    if z_pos >= goal_apogee:
        return
    elif z_pos < start_elevation:
        return
    else:
        temp = []
        time = time + dt
        if mass > dry_mass:
            mass_flow_rate = np.interp(time, times, mass_flow_rates)
            mass = mass - (mass_flow_rate * dt)
            thrust = np.interp(time, times, thrusts)

        else:
            mass = dry_mass
            mass_flow_rate = 0
            thrust = 0
        z_accel = ((thrust * math.cos(launch_rail_phi) / mass) - gravity)
        total_vel = math.sqrt(x_vel**2 + y_vel**2 + z_vel**2)
        if z_vel >= 0:
            #drag = 0
            drag = -(.5 * cd * density * (total_vel ** 2) * frontal_area * dt)  # slug/ft^3 * ft/s * ft^2 *s * ft/s^2 * s - slug*ft/s
        else:
            #drag = 0

            drag = (.5 * cd * density * (total_vel ** 2) * frontal_area * dt)  # slug/ft^3  * ft^2/s^2 *s * ft^2 * s - slug*ft/s


        print(drag/dt)
        z_vel = z_vel + (z_accel * dt) + (drag/mass)
        z_pos = z_pos + (z_vel * dt) + (.5 * z_accel * (dt ** 2))
        if thrust == 0:
            y_accel = 0
            x_accel = 0
        else:
            y_accel = (z_accel * math.sin(launch_rail_phi) * math.sin(launch_rail_theta))
            x_accel = z_accel * math.sin(launch_rail_phi) * math.cos(launch_rail_theta)
        if wind_y<0 or wind_y>0:
            y_vel = y_vel + (y_accel * dt)+ (1-(y_vel/wind_y))
        if wind_x<0 or wind_x>0:
            x_vel = x_vel + (x_accel * dt)+ (1-(x_vel/wind_x))
        else:
            y_vel = y_vel + (y_accel * dt)
            x_vel = x_vel + (x_accel * dt)
        y_pos = y_pos + (y_vel * dt) + (.5 * y_accel * (dt ** 2))
        x_pos = x_pos + (x_vel * dt) + (.5 * x_accel * (dt ** 2))
        spin_vel = spin_vel + (spin_accel * dt)
        spin_pos = (spin_pos + (spin_vel * dt) + (.5 * spin_accel * (dt ** 2)))
        temp.append(time)
        temp.append(z_accel)
        temp.append(z_vel)
        temp.append(z_pos)
        temp.append(y_accel)
        temp.append(y_vel)
        temp.append(y_pos)
        temp.append(x_accel)
        temp.append(x_vel)
        temp.append(x_pos)
        temp.append(spin_vel)
        temp.append(spin_pos)
        temp.append(thrust)
        temp.append(mass)
        temp.append(mass_flow_rate)


        if (feet_per_iteration / z_vel) > max_dt or (feet_per_iteration / z_vel) <= 0:
            dt = max_dt
        else:
            dt = feet_per_iteration / z_vel
        temp.append(dt)
        temp.append(drag/dt)
        flight.append(temp)
        print(temp)
        recursive_tunnel(temp)


# Master Data List


def environment(case, vertical):

    rotational_accel = random.randrange(-36, 36)
    if case == "dynamic":
        x_wind_velocity = 10 # Some function of altitude agl ("vertical" variable)
        y_wind_velocity = 10 # Some function of altitude agl "vertical" variable)

    elif case == "random":
        x_wind_velocity = random.randint(-20, 20)  # Some function of altitude agl
        y_wind_velocity = random.randint(-20, 20)  # Some function of altitude agl


    else:
        x_wind_velocity = 0
        y_wind_velocity = 0


    return x_wind_velocity, y_wind_velocity, rotational_accel


# Inputs - Rocket and Mission
body_diameter = 6.17
frontal_area = math.pi * ((body_diameter / 2) ** 2) / 144
cd = 0.3  # Should be a function of Reynold's number
goal_apogee = 20000
engine = "AeroTech_M1419W.csv"
launch_rail_phi = 0 * math.pi / 180  # 0-90 Degrees, measured from perfectly vertical.
launch_rail_theta = 0 * math.pi / 180  # 0-360 Degrees, measured from positive x-axis
spin_vel = 0
spin_pos = 0

# Environment
start_elevation = 4500
wind = "dynamic"
altitudes = [1000 * i for i in range(0, 26)]
densities = [0.002377, 0.002308, 0.002241, 0.002175, 0.002111,
             0.002048, 0.001987, 0.001927, 0.001869, 0.001812,
             0.001756, 0.001701, 0.001648, 0.001596, 0.001546,
             0.001496, 0.001448, 0.001401, 0.001356, 0.001311,
             0.001267, 0.001225, 0.001184, 0.001144, 0.001105,
             0.001066]
gravities = [32.174, 32.171, 32.1679, 32.1648, 32.1617,
             32.1586, 32.1555, 32.1525, 32.1494, 32.1463,
             32.1432, 32.1401, 32.1371, 32.134, 32.1309,
             32.1278, 32.1247, 32.1217, 32.1186, 32.1155,
             32.1124, 32.1094, 32.1063, 32.1032, 32.1001,
             32.0971]

# Starting Conditions
gravity = np.interp(start_elevation, altitudes, gravities)
wet_mass = 45.03 / gravity
dry_mass = 36.14094 / gravity
times, thrusts, mass_flow_rates = thrustcurve(engine)

time = 0

# Vertical
z_accel = 0
z_vel = 0
z_pos = start_elevation
z_mom = 0
drag = 0

# X-Direction
x_accel = 0
x_vel = 0
x_pos = 0

# Y-Direction
y_accel = 0
y_vel = 0
y_pos = 0

# Computation Parameters and Startup
feet_per_iteration = 100
max_dt = .1
flight = []

temp = [time, z_accel, z_vel, z_pos, y_accel, y_vel, y_pos, x_accel, x_vel, x_pos, spin_vel, spin_pos, thrusts[0],
        wet_mass, mass_flow_rates[0], max_dt, drag]
flight.append(temp)
print(temp)

recursive_tunnel(temp)
fig = plt.figure()
trajectory = fig.add_subplot(2, 2, 1, projection='3d')
acc = fig.add_subplot(2, 2, 2)
vel = fig.add_subplot(2, 2, 3)
spin = fig.add_subplot(2, 2, 4)
max_alt = max([instant[3]-start_elevation for instant in flight])
print("Maximum Altitude Reached: ", max_alt)
trajectory.plot([instant[9] for instant in flight], [instant[6] for instant in flight],
                [step[3] - 4500 for step in flight])
acc.plot([instant[0] for instant in flight], [instant[1] for instant in flight], label='Acceleration (Z)')
acc.plot([instant[0] for instant in flight], [instant[4] for instant in flight], label='Acceleration (Y)')
acc.plot([instant[0] for instant in flight], [instant[7] for instant in flight], label='Acceleration (X)')
vel.plot([instant[0] for instant in flight], [instant[2] for instant in flight], label='Velocity (Z)')
vel.plot([instant[0] for instant in flight], [instant[5] for instant in flight], label='Velocity (Y)')
vel.plot([instant[0] for instant in flight], [instant[8] for instant in flight], label='Velocity (X)')
spin.plot([instant[0] for instant in flight], [instant[10] for instant in flight], label='Spin Velocity (Deg/s)')
spin.plot([instant[0] for instant in flight], [(180*math.cos(instant[11]*math.pi/180))for instant in flight], label='Spin Position (Deg)')

acc.title.set_text("Acceleration (ft/s^2)")
acc.legend(loc='upper right')

vel.title.set_text("Velocity (ft/s)")
vel.legend(loc='upper right')

spin.title.set_text("Spin")
spin.legend(loc='upper right')

plt.show()

