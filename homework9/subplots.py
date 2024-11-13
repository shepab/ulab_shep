# File name: subplots.py

import matplotlib.pyplot as plt
import numpy as np 

def subplots1(xstart, xstop ,title, xaxis, yaxis):
    # Plots the functions cos(x) and sin(x)

    # Defines variables
    x = np.linspace(xstart,xstop)
    hx = np.cos(x)
    kx = np.sin(x)

    # Plots the functions
    fig, ax = plt.subplots(1,2, figsize=(10,5))
    fig.supxlabel(xaxis)
    fig.supylabel(yaxis)
    fig.suptitle(title)

    ax[0].plot(x,hx)
    ax[0].set_title("cos(x)")
    ax[1].plot(x,kx)
    ax[1].set_title("sin(x)")
    
    plt.show()

def subplots2(xstart, xstop ,title, xaxis, yaxis):
    # Plots the functions cos(x) and sin(x)

    # Defines variables
    x = np.linspace(xstart,xstop)
    hx = np.cos(x)
    kx = np.sin(x)

    # Plots the functions
    fig, ax = plt.subplots(2,1, figsize=(10,5))
    fig.supxlabel(xaxis)
    fig.supylabel(yaxis)
    fig.suptitle(title)

    ax[0].plot(x,hx)
    ax[0].set_title("cos(x)")
    ax[1].plot(x,kx)
    ax[1].set_title("sin(x)")
    
    plt.show()