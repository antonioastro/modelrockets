import numpy as np
#this works in 2 dimensions, x (downwind) and y (vertically)

class Rocket():
        position = np.array([0.,0.])
        velocity = np.array([0.,0.])
        accceleration = np.array([0.,0.])
        force = np.array([0.,0.])
        massengine = 0.
        massrocket = 0.
        massprop = 0.
        impulse = 0.
        thrusttime = 0.
        timedelay = 0.
        chute = 0.
        
        rocket_ = []
        
        def __init__(self,initialPosition,initialVelocity,initialAcceleration,force,massengine,massrocket,massprop,impulse,thrusttime,timedelay,chute):
            self.rocket_.append(self)
            self.position = np.array(initialPosition)
            self.velocity = np.array(initialVelocity)
            self.acceleration = np.array(initialAcceleration)
            self.force = np.array(force)
            self.massengine = massengine
            self.massrocket = massrocket
            self.massprop = massprop
            self.impulse = impulse
            self.thrusttime = thrusttime
            self.timedelay = timedelay
            self.chute = chute
            
        def eulercramer(self,deltaT):
            self.velocity = self.velocity + (self.acceleration*deltaT)
            self.position = self.position + (self.velocity*deltaT)
            
        def __repr__(self): #this states what is printed when print(Class) is called. Generally just ignore this.
            return (self.position,self.velocity,self.acceleration,self.force)