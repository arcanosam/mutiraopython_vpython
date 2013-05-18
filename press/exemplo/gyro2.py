# from visual import *


# scene.width=800
# scene.height=800
# scene.title='Nutating Gyroscope'

Lshaft = 1.
r = Lshaft/2.
Rshaft = 0.03
M = 1.
Rrotor = 0.4
Drotor = 0.1
I3 = 0.5*M*Rrotor**2
I1 = M*r**2 + .5*I3
hpedestal = Lshaft
wpedestal = 0.1
tbase = 0.05
wbase = 3*wpedestal
g = 9.8
Fgrav = vector(0,-M*g,0)
top = vector(0,0,0)

theta = 0.3*pi
thetadot = 0
psi = 0
psidot = 30
phi = -pi/2
phidot = 0

if False:
    a = (1-I3/I1)*sin(theta)*cos(theta)
    b = -(I3/I1)*psidot*sin(theta)
    c = M*g*r*sin(theta)/I1
    phidot = (-b+sqrt(b**2-4*a*c))/(2*a)

pedestal = box(
    pos=top-vector(0,hpedestal/2.,0),
    height=hpedestal,
    length=wpedestal,
    width=wpedestal,
    color=(0.4,0.4,0.5)
)

base = box(
    pos=top-vector(0,hpedestal+tbase/2.,0),
    height=tbase,
    length=wbase,
    width=wbase,
    color=pedestal.color
)

gyro=frame(axis=(sin(theta)*sin(phi),cos(theta),sin(theta)*cos(phi)))

shaft = cylinder(
    axis=(Lshaft,0,0),
    radius=Rshaft,
    color=color.green,
    material=materials.rough,
    frame=gyro
)

rotor = cylinder(
    pos=(Lshaft/2 - Drotor/2, 0, 0),
    axis=(Drotor, 0, 0),
    radius=Rrotor,
    color=color.gray(0.7),
    material=materials.rough,
    frame=gyro
)

tip = sphere(
    pos=gyro.pos + gyro.axis * Lshaft,
    color=color.yellow,
    radius=0.001*shaft.radius,
    make_trail=True,
    interval=5,
    retain=250
)

tip.trail_object.radius = 0.2*shaft.radius

self.dsy.autoscale = 0 # scene.autoscale = 0

dt = 0.0001
t = 0.
Nsteps = 20

while True:
    rate(100)
    for step in range(Nsteps):

        atheta = sin(theta)*cos(theta)*phidot**2+(
            M*g*r*sin(theta)-I3*(psidot+phidot*cos(theta))*phidot*sin(theta))/I1
        aphi = (I3/I1)*(psidot+phidot*cos(theta))*thetadot/sin(theta)-2*cos(theta)*thetadot*phidot/sin(theta)
        apsi = phidot*thetadot*sin(theta)-aphi*cos(theta)

        thetadot += atheta*dt
        phidot += aphi*dt
        psidot += apsi*dt

        theta += thetadot*dt
        phi += phidot*dt
        psi += psidot*dt

    gyro.axis = vector(sin(theta)*sin(phi),cos(theta),sin(theta)*cos(phi))

    gyro.rotate(angle=psidot*dt*Nsteps)
    tip.pos = gyro.pos + gyro.axis * Lshaft
    t = t+dt*Nsteps
