from vpython import *

v = 0.03
dt = 0.001
t = 0

scene = canvas(title='1D Motion', width=800, height=800, x=0, y=0, center=vec(0, 0.06, 0), background=vec(0.5, 0.6, 0.5))
floor = box(pos=vec(0, -(0.005)/2, 0), length=0.3, height=0.005, width=0.1)
cube = box(pos=vec(0, 0.05/2, 0), length=0.05, height=0.05, width=0.05, v=vec(v, 0, 0))

while (cube.pos.x < 0.10):
    rate(1000)
    cube.pos.x += v*dt
    t += dt
print("t=", t)