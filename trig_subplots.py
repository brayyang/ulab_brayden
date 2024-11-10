import numpy as np
import matplotlib.pyplot as plt

# Function 1: horizontal subplots
def horizontal_subplots(h, k):
    # Defining domain
    x = np.linspace(0, 2*np.pi, 100)

    #Defining the functions
    h = np.cos(x)
    k = np.sin(x)

    # Plotting the graphs
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].plot(x, h, label="cosx")
    ax[1].plot(x ,k, label="sinx")
    
    # Title and Labels
    ax[0].set_xlabel("X-axis")
    ax[0].set_ylabel("Y-axis")
    ax[1].set_xlabel("X-axis")
    ax[1].set_ylabel("Y-axis")
    return

# Function 2: vertical subplots
def vertical_subplots(h, k):
    # Defining domain
    x = np.linspace(0, 2*np.pi, 100)

    #Defining the functions
    h = np.cos(x)
    k = np.sin(x)

    # Plotting the graphs
    fig, ax = plt.subplots(2, 1, figsize=(4, 8))
    ax[0].plot(x, h, label="cosx")
    ax[1].plot(x ,k, label="sinx")
    
    # Title and Labels
    ax[0].set_xlabel("X-axis")
    ax[0].set_ylabel("Y-axis")
    ax[1].set_xlabel("X-axis")
    ax[1].set_ylabel("Y-axis")
    return
