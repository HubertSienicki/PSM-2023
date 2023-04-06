import numpy as np
import matplotlib.pyplot as plt

def simulate_rolling_sphere(radius, mass, angle, friction, initial_velocity, time_step, duration):
    
    gravity = 9.81
    
    num_steps = int(duration / time_step)
    time = np.zeros(num_steps)
    position = np.zeros(num_steps)
    velocity = np.zeros(num_steps)
    kinetic_energy = np.zeros(num_steps)
    potential_energy = np.zeros(num_steps)
    total_energy = np.zeros(num_steps)
    angle_of_rotation = np.zeros(num_steps)
    
    # Set initial conditions
    time[0] = 0
    position[0] = 0
    velocity[0] = initial_velocity
    kinetic_energy[0] = 0.5 * mass * velocity[0]**2
    potential_energy[0] = mass * gravity * radius * (1 - np.cos(angle))
    total_energy[0] = kinetic_energy[0] + potential_energy[0]
    angle_of_rotation[0] = 0
    
    for i in range(num_steps - 1):
        
        acceleration = gravity * np.sin(angle) - friction * gravity * np.cos(angle)
        
        alpha = (radius * acceleration) / (2 * radius)
        
        velocity_half = velocity[i] + 0.5 * time_step * acceleration
        position_half = position[i] + 0.5 * time_step * velocity[i]
        angle_half = angle_of_rotation[i] + 0.5 * time_step * alpha
        
        acceleration_half = gravity * np.sin(angle) - friction * gravity * np.cos(angle)
        alpha_half = (radius * acceleration_half) / (2 * radius)
        
        velocity[i+1] = velocity[i] + time_step * acceleration_half
        position[i+1] = position[i] + time_step * velocity_half
        angle_of_rotation[i+1] = angle_of_rotation[i] + time_step * alpha_half
        
        kinetic_energy[i+1] = 0.5 * mass * velocity[i+1]**2
        potential_energy[i+1] = mass * gravity * radius * (1 - np.cos(angle + position[i+1]/radius))
        total_energy[i+1] = kinetic_energy[i+1] + potential_energy[i+1]
        
        time[i+1] = time[i] + time_step
    
    return time, position, velocity, kinetic_energy, potential_energy, angle_of_rotation

def simulate_rolling_ball(radius, mass, angle, friction, initial_velocity, time_step, duration):
    
    gravity = 9.81
    
    num_steps = int(duration / time_step)
    time = np.zeros(num_steps)
    position = np.zeros(num_steps)
    velocity = np.zeros(num_steps)
    kinetic_energy = np.zeros(num_steps)
    potential_energy = np.zeros(num_steps)
    total_energy = np.zeros(num_steps)
    
    time[0] = 0
    position[0] = 0
    velocity[0] = initial_velocity
    kinetic_energy[0] = 0.5 * mass * velocity[0]**2
    potential_energy[0] = mass * gravity * radius * (1 - np.cos(angle))
    total_energy[0] = kinetic_energy[0] + potential_energy[0]
    angle_rotation = np.zeros(num_steps)
    
    for i in range(num_steps - 1):
        
        acceleration = gravity * np.sin(angle) - friction * gravity * np.cos(angle)

        velocity_half = velocity[i] + 0.5 * time_step * acceleration

        acceleration_half = gravity * np.sin(angle) - friction * gravity * np.cos(angle)
        
        velocity[i+1] = velocity[i] + time_step * acceleration_half
        position[i+1] = position[i] + time_step * velocity_half
        angle_rotation[i+1] = angle_rotation[i] + time_step * (velocity_half / radius)

        kinetic_energy[i+1] = 0.5 * mass * velocity[i+1]**2
        potential_energy[i+1] = mass * gravity * radius * (1 - np.cos(angle + position[i+1]/radius))
        total_energy[i+1] = kinetic_energy[i+1] + potential_energy[i+1]
        
        time[i+1] = time[i] + time_step
    
    return time, position, velocity, kinetic_energy, potential_energy, angle_rotation


time_ball, position_ball, velocity_ball, kinetic_energy_ball, potential_energy_ball, angle_ball = simulate_rolling_ball(radius=0.1, mass=0.1, angle=np.pi/6, friction=0.01, initial_velocity=0.0, time_step=0.01, duration=5.0)

time_sphere, position_sphere, velocity_sphere, kinetic_energy_sphere, potential_energy_sphere, angle_sphere = simulate_rolling_sphere(radius=0.1, mass=0.1, angle=np.pi/6, friction=0.01, initial_velocity=0.0, time_step=0.01, duration=5.0)

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
ax1.plot(time_ball, position_ball, label='Ball')
ax2.plot(time_sphere, position_sphere, label='Sphere')
ax1.set_xlabel('Time (s)')
ax2.set_xlabel('Time (s)')
ax1.set_ylabel('Position (m)')
ax2.set_ylabel('Position (m)')
ax1.legend()
ax2.legend()

fig2, ((ax3, ax4), (ax5, ax6)) = plt.subplots(2, 2, figsize=(12,8))
ax3.plot(time_ball, kinetic_energy_ball, label='Kinetic Energy')
ax3.plot(time_ball, potential_energy_ball, label='Potential Energy')
ax3.plot(time_ball, kinetic_energy_ball + potential_energy_ball, label='Total Energy')
ax4.plot(time_sphere, kinetic_energy_sphere, label='Kinetic Energy')
ax4.plot(time_sphere, potential_energy_sphere, label='Potential Energy')
ax4.plot(time_sphere, kinetic_energy_sphere + potential_energy_sphere, label='Total Energy')
ax3.set_xlabel('Time (s)')
ax4.set_xlabel('Time (s)')
ax3.set_ylabel('Energy (J)')
ax4.set_ylabel('Energy (J)')
ax3.legend()
ax4.legend()

ax5.plot(time_ball, angle_ball, color='red', label='Angle')
ax6.plot(time_sphere, angle_sphere, color='red', label='Angle')
ax5.set_xlabel('Time (s)')
ax6.set_xlabel('Time (s)')
ax5.set_ylabel('Angle (rad)')
ax6.set_ylabel('Angle (rad)')
ax5.legend()
ax6.legend()

plt.show()