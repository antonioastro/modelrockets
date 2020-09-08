import numpy as np 
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

data=np.load('data.npy',allow_pickle=True)
rocketlist=np.load('listrockets.npy',allow_pickle=True)

f1=plt.figure('Trajectory')
obj=0
while obj < len(rocketlist):
    xpos=[]
    ypos=[]
    for line in data:
        xpos.append(line[obj+1].position[0])
        ypos.append(line[obj+1].position[1])
    plt.plot(xpos,ypos,'-')
    obj=obj+1
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.savefig('trajectory.png',bbox_inches='tight',dpi=1000)

f2=plt.figure('Altitude')
obj=0
while obj < len(rocketlist):
    time=[]
    ypos=[]
    for line in data:
        time.append(line[obj])
        ypos.append(line[obj+1].position[1])
    plt.plot(time,ypos,'-')
    obj=obj+1
plt.xlabel('time since launch (s)')
plt.ylabel('y-position (m)')
plt.savefig('Altitude.png',bbox_inches='tight',dpi=1000)
#plt.show('Trajectory') 

f3=plt.figure('Acceleration')
obj=0
while obj < len(rocketlist):
    time=[]
    acc=[]
    for line in data:
        time.append(line[obj])
        acctot = np.linalg.norm(line[obj+1].acceleration)/9.81
        acc.append(acctot)
    plt.plot(time,acc,'-')
    obj=obj+1
plt.xlabel('time since launch (s)')
plt.ylabel('total acceleration (g)')
plt.savefig('acceleration.png',bbox_inches='tight',dpi=1000)

f4=plt.figure('Velocity')
obj=0
while obj < len(rocketlist):
    time=[]
    vel=[]
    for line in data:
        time.append(line[obj])
        veltot = np.linalg.norm(line[obj+1].velocity)
        vel.append(veltot)
    plt.plot(time,vel,'-')
    obj=obj+1
plt.xlabel('time since launch (s)')
plt.ylabel('total velocity (m/s)')
plt.savefig('velocity.png',bbox_inches='tight',dpi=1000)

print('done')