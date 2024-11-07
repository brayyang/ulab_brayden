# File: finding_velocity.py
import numpy as np

masses = np.array([5, 3]) # ([mass 1, mass 2])
initial_velocities = np.array([
    [3, 4] # [x initial velocity, y initial velocity] for mass 1
    [-2, 5] # [x initial velocity, y initial velocity] for mass 2
])

# Assume the masses collide elastically

def total_momentum(x_momentum, y_momentum):
    # Calculating total initial momentum
    initial_x_momentum = np.sum(masses * initial_velocities[:, 0]) # Gives initial momentum in the x direction
    initial_y_momentum = np.sum(masses * initial_velocities[:, 1]) # Gives initial momentum in the y direction
    initial_momentum = np.array([initial_x_momentum, initial_y_momentum])

    # By conservation of momentum,
    total_momentum = final_momentum = initial_momentum   
    
    return total_momentum

def total_kinetic_energy(masses):
    # Calculating total initial kinetic energy
    initial_kinetic_energy = np.sum(0.5 * masses * (velocities[:, 0] ** 2 + velocities[:, 0] ** 2))

    # By conservation of mechanical energy,
    total_kinetic_energy = final_kinetic_energy = initial_kinetic_energy
    
    return initial_kinetic_energy

def final_velocity(masses):
    # Calculating final velocity of each mass
    final_kinetic
