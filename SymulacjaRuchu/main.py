import math
import matplotlib.pyplot as plt

g = 9.81
mass = 1.0
drag = 0.01

start_x, start_y = 0.0, 0.0 
start_v = 50.0
theta = math.pi / 4

dt = 0.01
t_max = 10.0

def euler_method():
    x, y = start_x, start_y
    v_xx, v_y = start_v * math.cos(theta), start_v * math.sin(theta)
    x_data, y_data = [x], [y]

    while y >= 0.0:
        v = math.sqrt(v_xx ** 2 + v_y ** 2)
        force_x = -drag * v * v_xx
        force_y = -mass * g - drag * v * v_y
        acceleration_x = force_x / mass
        acceleration_y = force_y / mass

        x += v_xx * dt
        y += v_y * dt
        v_xx += acceleration_x * dt
        v_y += acceleration_y * dt

        x_data.append(x)
        y_data.append(y)

    return x_data, y_data

def midpoint_method():
    x, y = start_x, start_y
    v_xx, v_y = start_v * math.cos(theta), start_v * math.sin(theta)
    x_data, y_data = [x], [y]

    while y >= 0.0:
        v = math.sqrt(v_xx ** 2 + v_y ** 2)
        force_x = -drag * v * v_xx
        force_y = -mass * g - drag * v * v_y
        acceleration_x = force_x / mass
        acceleration_y = force_y / mass

        x += v_xx * dt + 0.5 * acceleration_x * dt ** 2
        y += v_y * dt + 0.5 * acceleration_y * dt ** 2
        v_xx += acceleration_x * dt
        v_y += acceleration_y * dt

        x_data.append(x)
        y_data.append(y)

    return x_data, y_data

euler_x, euler_y = euler_method()
midpoint_x, midpoint_y = midpoint_method()

plt.plot(euler_x, euler_y, label='Euler')
plt.plot(midpoint_x, midpoint_y, label='Midpoint')
plt.xlabel('Horizontal distance (m)')
plt.ylabel('Vertical distance (m)')
plt.legend()
plt.show()