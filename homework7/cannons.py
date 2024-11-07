# File: cannons.py

import numpy as np

g = -9.8

def radians_degrees(angle):
    ''' 
    Converts radians to degrees
    Inputs:
    angle (float): angle in degrees 
    
    '''
    
    radians = angle * np.pi / 180
    
    return radians

def cannon_launch(cannon):
    ''' 
    Calculates how far away from the launching a cannonball will land if fired at a given angle with a given velocity
    Acceleration due to gravity at the surface of Earth: g = -9.8 m/s

    Model for displacement due to acceleration: y = v0t + gt^2

    Inputs:
    angle (float): angle of launch in degrees
    initial_velocity (float): velocity after launch in meters/second

    '''
    results = []
    
    for cannonball in cannon:
            
        angle = cannonball[0]
        initial_velocity = cannonball[1]
        
        radians = radians_degrees(angle)
        
        v_hi = initial_velocity * np.cos(radians) # Initial horizontal velocity
    
        v_vi = initial_velocity * np.sin(radians) # Initial vertical velocity
    
        t = -v_vi / g # Time it takes for cannonball to reach maximum height (half time spent in air)
    
        distance = v_hi * 2 * t # Horizontal distance the cannonball travels
        
        result = "Distance travelled: " + str(distance) + " meters."
        result = "".join(result)
    
        if distance == 30:
            result2 = " You hit the target!"
        elif distance >= 30:
            result2 = " Too far!"
        else:
            result2 = " Not far enough!"
       
        result = result + result2
        
        results.append(result)
        
    return results

def height(cannon):
    ''' 
    Calculates the maximum height of the cannonball

    Acceleration due to gravity at the surface of Earth: g = -9.8 m/s

    Model for displacement due to acceleration: y = v0t + gt^2

    Inputs:
    angle (float): angle of launch in degrees
    initial_velocity (float): velocity after launch in meters/second

    '''
    results = []
    
    for cannonball in cannon:
            
        angle = cannonball[0]
        initial_velocity = cannonball[1]

        radians = radians_degrees(angle)

        v_vi = initial_velocity * np.sin(radians) # Initial vertical velocity

        t = -v_vi / g # Time it takes for cannonball to reach maximum height

        y = (v_vi * t) + g * t ** 2 # Y displacement at maximum height

        result = "Maximum height: " + str(y) + " meters"
        result = "".join(result)
        results.append(result)
        
    return results
    