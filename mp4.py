import math as math
import numpy as np
import matplotlib.pyplot as plt

ho = float(input('Enter the initial height of projectile above the ground in meters: '))
vo = float(input('Enter the the magnitude of the velocity in m/s: '))
theta1 = float(input('Enter the angle in degrees  with respect to the +x-axis at which the projectile is fired: '))
ax = float(input('Enter the x-component of the acceleration,considering the sign,in m/s^2: '))
ay = float(input('Enter the y-component of the acceleration,considering the sign,in m/s^2: '))

if ay==0:
    print('The vertical acceleration is zero, free fall is not possible. Try again.')
    quit()

theta=math.radians(theta1)
vox = vo*math.cos(theta)
voy = vo*math.sin(theta)
a = (1/2)*ay
b = voy
c = ho
tf1 = np.roots([a,b,c])
tf = max(tf1)
t = np.linspace(0,tf,1000)
d = (math.sqrt(voy**2-4*(1/2*ay)*ho))
x = d+vox*t
y = ho+voy*t+(1/2)*ay*t**2

plt.plot(x,y,'r')
plt.grid()
plt.title('Projectile Trajectory')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')






