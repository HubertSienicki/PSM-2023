import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


# stałe
g = 9.81 
L = 1.0   

theta0 = math.pi / 4   
omega0 = 0.0          

tmax = 10.0
dt = 0.01    
N = int(tmax / dt) + 1 

def angular_acceleration(theta, omega):
    return -g / L * math.sin(theta)


def euler(theta0, omega0, tmax, dt):

    t = 0.0
    theta = theta0
    omega = omega0
    
    t_list = [t]
    theta_list = [theta]
    omega_list = [omega]
    
    for i in range(N):
        alpha = angular_acceleration(theta, omega)
        
        theta = theta + omega * dt
        omega = omega + alpha * dt
        
        t = t + dt
        
        t_list.append(t)
        theta_list.append(theta)
        omega_list.append(omega)
        
    return t_list, theta_list, omega_list

def euler_midpoint(theta0, omega0, tmax, dt):
    t = 0.0
    theta = theta0
    omega = omega0
    
    t_list = [t]
    theta_list = [theta]
    omega_list = [omega]
    
    for i in range(N):
        theta_mid = theta + 0.5 * omega * dt
        omega_mid = omega + 0.5 * angular_acceleration(theta, omega) * dt
        alpha_mid = angular_acceleration(theta_mid, omega_mid)
        
        theta = theta + omega_mid * dt
        omega = omega + alpha_mid * dt
        
        t = t + dt

        t_list.append(t)
        theta_list.append(theta)
        omega_list.append(omega)
        
    return t_list, theta_list, omega_list

def RK2(theta0, omega0, tmax, dt):
    t = 0.0
    theta = theta0
    omega = omega0
    
    t_list = [t]
    theta_list = [theta]
    omega_list = [omega]

    for i in range(N):

        alpha1 = angular_acceleration(theta, omega)

        theta_mid = theta + 0.5 * omega * dt
        omega_mid = omega + 0.5 * alpha1 * dt
        alpha2 = angular_acceleration(theta_mid, omega_mid)
        
        theta = theta + omega_mid * dt
        omega = omega + alpha2 * dt
        
        t = t + dt

        t_list.append(t)
        theta_list.append(theta)
        omega_list.append(omega)
        
    return t_list, theta_list, omega_list

def plot_energy(t_list, theta_list, omega_list, L, m):

    theta_list = np.array(theta_list)
    omega_list = np.array(omega_list)
    
    K_list = 0.5 * m * (L * omega_list)**2
    
    U_list = m * 9.81 * L * (1 - np.cos(theta_list))
    
    E_list = K_list + U_list
    
    plt.plot(t_list, K_list, label='Energia kinetyczna')
    plt.plot(t_list, U_list, label='Energia potencjalna')
    plt.plot(t_list, E_list, label='Energia całkowita')
    plt.legend()
    plt.xlabel('Czas (s)')
    plt.ylabel('Energia (J)')
    plt.show()

def main():
    # parametry wahadła
    L = 1.0
    m = 1.0
    theta0 = np.pi/4.0
    omega0 = 0.0
    tmax = 10.0
    dt = 0.01
    
    t_list_euler, theta_list_euler, omega_list_euler = euler(theta0, omega0, tmax, dt)
    
    plot_energy(t_list_euler, theta_list_euler, omega_list_euler, L, m)
    
    t_list_euler_mid, theta_list_euler_mid, omega_list_euler_mid = euler_midpoint(theta0, omega0, tmax, dt)
    

    plot_energy(t_list_euler_mid, theta_list_euler_mid, omega_list_euler_mid, L, m)
    
    t_list_rk2, theta_list_rk2, omega_list_rk2 = RK2(theta0, omega0, tmax, dt)
    
    plot_energy(t_list_rk2, theta_list_rk2, omega_list_rk2, L, m)

t = np.arange(0.0, tmax, dt)

theta = np.zeros_like(t)
omega = np.zeros_like(t)
theta[0] = theta0
omega[0] = omega0

for i in range(1, len(t)):
    alpha = -g / L * np.sin(theta[i-1])
    
    omega[i] = omega[i-1] + alpha * dt
    theta[i] = theta[i-1] + omega[i] * dt

fig, ax = plt.subplots()

pendulum, = ax.plot([], [], 'o-', lw=2)

ax.set_xlim(-L-0.5, L+0.5)
ax.set_ylim(-L-0.5, L+0.5)

def update(frame):
    x = [0, L * np.sin(theta[frame])]
    y = [0, -L * np.cos(theta[frame])]
    
    pendulum.set_data(x, y)
    
    return pendulum,

ani = FuncAnimation(fig, update, frames=len(t), interval=dt*1000, blit=True)

plt.show()

if __name__ == "__main__":
    main()

