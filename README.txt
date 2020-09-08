For v1 of the model rocket simulation there are 4 files. When using the simulation, all files must be in the same directory.
I hope to develop this in future and make it a little more user-friendly with a user interface, etc. But currently that is beyond the scope of my programming abilities.

I hope this readme helps :) 
Give me a follow on Twitter @antonioastro_.
Let me know if you use the simulation, and if you get an accelerometer and altimeter for the rockets please show me a comparison! 
If you have any problems using this, please ask me on Twitter :)

----Rocket.py----

This is the class definition that defines all parameters that affect the rocket. 
This does not need editing unless new parameters are accounted for that directly concern the rocket.
You need not run the code, simply have it saved in the directory.

----RocketInfo----

This creates instances of rockets using the Rocket class. 
The parameters are all given values in this in the form of a numpy array (with pos, vel, acc, force as numpy arrays/vectors also)
These go by:

NAME = ([[position/meters x,y],[velocity/meters per sec x,y],[acceleration/meters per sec^2 x,y],[force/newtons x,y],
			mass of engine/grams, mass of rocket/grams, mass of propellant/grams, total impulse/newton secs,
			total thrust duration/secs, time delay/secs, parachute diameter/ meters])
			
You need only change the values - remember to stick to the same units. You should be able to read values straight off the Estes table if you used those motors.
To add other rockets and engine combinations, simply find out the information you need and copy and paste the dummy for editing.
DO NOT CHANGE ANYTHING in the position, velocity, acceleration, force arrays as this gets overridden anyway
unless you have a raised or moving launch platform, in which case remember the positive x- and y-components are the horizontal and vertical axis, respectively.

Hash out the other rockets so as not to clutter up the graph. If you didn't do this, the rockets would all be plotted. Collisions of rockets are not accounted for.
You need not run the code, simply have it saved in the directory.

----RocketSim----
The actual simulation file. It runs the simulation using an iterative update process to calculate new telemetry based on the previous values. It will save 2 .npy files for use in the RocketPlot file containing all the data.
You may leave default values throughout, or change certain values as detailed below. Once done, click RUN and wait until the terminal reads "saved data". Then, open the RocketPlot file.

There are a few manually edited parameters here that have an effect on the accuracy of the simulation, and a few that affect the rocket directly. Within this code these are the only things that should be changed.
Changing anything else will likely break the simulation. 

"deltaT" (on line 8) - this is the accuracy of the simulation in units of seconds. Each iteration, the simulation will add this time interval to the previous for calculating updated telemetry. 
		The lower this value, the more accurate your simulation. It is recommended that this is lower in value than the "thrust duration" of your rocket motor or it simply won't budge from the Origin.
		This is by default 0.01 seconds (or 10 milliseconds)
		
"runtime" (on line 9) - this is how long the simulation will simulate for in units of seconds. So the simulation will iterate in increments of deltaT from 0 to this value. 
		By default this is 2000 seconds.
		If your rocket happens to land (i.e reach y=0) before this time limit it will stop plotting, but the simulation will continue until this runtime value is reached. 
		
"rho" (line 14) is the density of air in units kg/m^3. By default this is the density of air at sea level. It assumes constant density.
		This also affects the rocket.
		
"wind" (line 15) is the windspeed in m/s. This is only a magnitude of speed. Direction is by default in the positive x-direction in the final plots.
		This is default 5 m/s
		
Inside "def Gravity", 
		the value "g" (line 18) is the local gravity. By default this is Earth's gravity as a vector array affecting in the y-direction as [-9.81] m/s^2. 
		This does not need to be changed, but changing it does affect the rocket.
		
Inside "def Drag", 
		on line 28 is a formula. Within it is the number "2.3". This is the coefficient of drag for a hollow hemisphere. This is set as constant, but could be changed. 
		This is the only thing within the formula that can be changed here, although it is recommended to leave it default.
		
The simulation makes several assumptions.
1) assume the engine exerts a constant force throughout the burn.
2) assume constant air density
3) assume constant wind speed everywhere.
4) assume air resistance until parachute deployment is negligible
5) assume the mass of the rocket does not change until after all propellant is used up.
6) assume constant gravity. 
7) assume flat earth. (If you gained enough altitude and wind speed, the rocket would go for many thousands of kilometers downwind where curvature would be present) 
8) assume wind causes a constant force on the rocket, accelerating it to the side (eventually the rocket would be superluminal if it had enough time) although the simulation isn't expected to run long enough.

----RocketPlot----
You need not change anything in this file. By clicking run, this will look for the saved data files from RocketSim and plot the data on 4 graphs that will be saved as png files in the same directory.
1) Trajectory (plots an x-y graph)
2) Altitude (plots an altitude-time graph)
3) Acceleration (plots acceleration-time graph)
4) Velocity (plots velocity-time graph)

Graphs 2,3,4 take the magnitudes of these vector values, so all values appear positive on the graphs. 