import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
M_earth = 5.97219e24
M_moon = 7.342e22
M_sun = 1.989e30
R_moon = 384400000
R_earth = 149597870700

def equations_of_motion(y):
    x_e, y_e, vx_e, vy_e, x_m, y_m, vx_m, vy_m = y
    r_e = np.sqrt(x_e**2 + y_e**2)
    r_m = np.sqrt(x_m**2 + y_m**2)
    r_em = np.sqrt((x_m - x_e)**2 + (y_m - y_e)**2)

    ax_e = -G * (M_sun * x_e / r_e**3 + M_moon * (x_e - x_m) / r_em**3)
    ay_e = -G * (M_sun * y_e / r_e**3 + M_moon * (y_e - y_m) / r_em**3)
    ax_m = -G * (M_sun * x_m / r_m**3 + M_earth * (x_m - x_e) / r_em**3)
    ay_m = -G * (M_sun * y_m / r_m**3 + M_earth * (y_m - y_e) / r_em**3)

    return np.array([vx_e, vy_e, ax_e, ay_e, vx_m, vy_m, ax_m, ay_m])

def improved_euler(y, dt, func):
    k1 = dt * func(y)
    k2 = dt * func(y + 0.5 * k1)
    return y + k2

t_total = 3.154e7
dt = 3600

x_e0, y_e0 = R_earth, 0
vx_e0, vy_e0 = 0, np.sqrt(G * M_sun / R_earth)
x_m0, y_m0 = x_e0, y_e0 + R_moon
vx_m0, vy_m0 = vx_e0 + np.sqrt(G * M_earth / R_moon), vy_e0

y0 = np.array([x_e0, y_e0, vx_e0, vy_e0, x_m0, y_m0, vx_m0, vy_m0])

t_values = np.arange(0, t_total, dt)
trajectory = np.zeros((len(t_values), 8))
trajectory[0] = y0

for i in range(1, len(t_values)):
    trajectory[i] = improved_euler(trajectory[i-1], dt, equations_of_motion)

plt.figure(figsize=(10, 10))
plt.plot(trajectory[:, 0], trajectory[:, 1], label="Ziemia")
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Trajektoria Ziemi wokół Słońca')
plt.axis('equal')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 10))
plt.plot(trajectory[:, 4] - trajectory[:, 0], trajectory[:, 5] - trajectory[:, 1], label="Księżyc")
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Trajektoria Księżyca wokół Ziemi')
plt.axis('equal')
plt.legend()
plt.grid()
plt.show()