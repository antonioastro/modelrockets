from Rocket import Rocket
import matplotlib.pyplot as plt 
import math
import copy
import numpy as np
import RocketInfo

deltaT = 0.01 #timesetp in seconds
runtime = 2000 #total runtime in seconds

data = []
time = 0

wind = 5 #windspeed m/s

def Gravity(obj):
    g=np.array([0.,-9.81]) #local gravity
    Grav = (obj.massrocket+obj.massengine)*g/1000
    return Grav #force due to gravity

def Engine(obj):
    force = obj.impulse / obj.thrusttime #assume engine exerts a constant force
    Eng = np.array([0.,force])
    return Eng #force due to rocket engine

def Drag(obj):
    rho = 1.225 #density of air kg/m3
    dforce = -0.125*rho*obj.velocity*obj.chute**2*2.3*math.pi #remember - C is overridden here to 2.3 due to googling
    return dforce #drag force

def Wind(obj):
    rho = 1.225 #density of air kg/m3
    theta = 90 #half-angle of edge (estimated)
    C = 0.0112*theta+0.162
    wforce = np.array([0.5*rho*wind*0.02*0.3*C,0.])
    return wforce

while (time<runtime):
    temp1=[]
    time = time + deltaT
    for obj in RocketInfo.rocket:
        if time<obj.thrusttime:
            obj.force=Gravity(obj)+Engine(obj)+Wind(obj)
            obj.acceleration=1000*obj.force/(obj.massrocket+obj.massengine) #assume the mass doesnt change until AFTER burn is over (biggest assumption)
        elif obj.thrusttime<time and time<obj.thrusttime+obj.timedelay:
            obj.force=Gravity(obj)+Wind(obj)
            obj.acceleration=1000*obj.force/(obj.massrocket+obj.massengine-obj.massprop)
        else:
            obj.force=Gravity(obj)+Drag(obj)+Wind(obj)
            obj.acceleration=1000*obj.force/(obj.massrocket+obj.massengine-obj.massprop)
        obj.eulercramer(deltaT)
        temp1.append(copy.deepcopy(obj))
        if obj.position[1]<0:
            continue
        else:
            item=[time]
            item=item+temp1
            data.append(item)
            
np.save('data.npy',data)
np.save('listrockets.npy',RocketInfo.rocket)
print('saved data')
