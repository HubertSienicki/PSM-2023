import math
import matplotlib.pyplot as plt

# Constants
g = 9.81  # m/s^2
mass = 1.0  # kg
drag_coeff = 0.01  # kg/m

# Initial conditions
x0, y0 = 0.0, 0.0  # m
v0 = 50.0  # m/s
theta = math.pi / 4  # radians

# Time step and duration
dt = 0.01  # s
t_max = 10.0  # s

# Euler's method
def euler_method():
    x, y = x0, y0
    vx, vy = v0 * math.cos(theta), v0 * math.sin(theta)
    x_data, y_data = [x], [y]

    while y >= 0.0:
        v = math.sqrt(vx ** 2 + vy ** 2)
        Fx = -drag_coeff * v * vx
        Fy = -mass * g - drag_coeff * v * vy
        ax = Fx / mass
        ay = Fy / mass

        x += vx * dt
        y += vy * dt
        vx += ax * dt
        vy += ay * dt

        x_data.append(x)
        y_data.append(y)

    return x_data, y_data

# Midpoint method
def midpoint_method():
    x, y = x0, y0
    vx, vy = v0 * math.cos(theta), v0 * math.sin(theta)
    x_data, y_data = [x], [y]

    while y >= 0.0:
        v = math.sqrt(vx ** 2 + vy ** 2)
        Fx = -drag_coeff * v * vx
        Fy = -mass * g - drag_coeff * v * vy
        ax = Fx / mass
        ay = Fy / mass

        x += vx * dt + 0.5 * ax * dt ** 2
        y += vy * dt + 0.5 * ay * dt ** 2
        vx += ax * dt
        vy += ay * dt

        x_data.append(x)
        y_data.append(y)

    return x_data, y_data

# Visualize the trajectory using Matplotlib
euler_x, euler_y = euler_method()
midpoint_x, midpoint_y = midpoint_method()

plt.plot(euler_x, euler_y, label='Euler')
plt.plot(midpoint_x, midpoint_y, label='Midpoint')
plt.xlabel('Horizontal distance (m)')
plt.ylabel('Vertical distance (m)')
plt.legend()
plt.show()