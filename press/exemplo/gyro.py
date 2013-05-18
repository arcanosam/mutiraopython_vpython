# from visual import *

# Gyroscope hanging from a spring
# Bruce Sherwood

arrowsvisible = False

# scene.title = 'Gyroscope'
# scene.visible = 0

top = vector(0,1.,0)
ks = 100.
Lspring = 1.
Rspring = 0.03
Dspring = 0.03
Lshaft = 1.
Rshaft = 0.03
M = 1.
Rrotor = 0.4
Drotor = 0.1
Dsquare = 1.4*Drotor
I = 0.5*M*Rrotor**2.
omega = 40
g = 9.8
Fgrav = vector(0,-M*g,0)
precession = M*g*(Lshaft/2.)/(I*abs(omega))
phi = atan(precession**2*(Lshaft/2.)/g)
s = M*g/(ks*cos(phi))

phi = 1./( ((I*abs(omega))/(M*Lshaft/2.))**2/(g*Lshaft/2.)-(Lspring+s)/(Lshaft/2.) )

s = M*g/(ks*cos(phi))
phi = 1./( ((I*abs(omega))/(M*Lshaft/2.))**2/(g*Lshaft/2.)-(Lspring+s)/(Lshaft/2.) )
pprecess = vector(0,-1,M*precession*(Lshaft/2.+(Lspring+s)*sin(phi)))

if omega < 0:
    pprecess = -pprecess

support = box(
    pos=top+vector(0,0.01,0),
    size=(0.2,0.02,0.2),
    color=color.green
)
spring = helix(
    pos=top,
    axis=vector(-(Lspring+s)*sin(phi),-(Lspring+s)*cos(phi),0),
    coils=10,
    radius=Rspring,
    thickness=Dspring,
    color=(1,0.7,0.2)
)
gyro = frame(pos=top+spring.axis)
gyro.axis = vector(1,0,0)

shaft = cylinder(
    pos=gyro.pos,
    axis=Lshaft*gyro.axis,
    radius=Rshaft, color=(0.85,0.85,0.85)
)

rotor = cylinder(
    pos=0.5*gyro.axis*(Lshaft-Drotor),
    axis=gyro.axis*Drotor,
    radius=Rrotor,
    color=(0.5,0.5,0.5)
)

stripe1 = curve(
    frame=gyro,
    color=color.black,
    pos=[
        rotor.pos+1.03*rotor.axis+vector(0,Rrotor,0),
        rotor.pos+1.03*rotor.axis-vector(0,Rrotor,0)
    ]
)
stripe1 = curve(
    frame=gyro,
    color=color.black,
    pos=[
        rotor.pos-0.03*rotor.axis+vector(0,Rrotor,0),
        rotor.pos-0.03*rotor.axis-vector(0,Rrotor,0)
    ]
)

gyro.rotate(axis=(0,1,0), angle=pi)

cm = gyro.pos+0.5*Lshaft*gyro.axis
Lrot = I*omega*gyro.axis
p = pprecess
dt = 0.01
t = 0.

Lrotarrow = arrow(
    length=0,
    shaftwidth=Rshaft,
    color=color.red,
    visible=arrowsvisible
)

Lrotscale = 0.2

rotimpulsearrow = arrow(
    length=0,
    shaftwidth=Lrotarrow.shaftwidth,
    color=color.cyan,
    visible=arrowsvisible
)
rotimpulsescale = 5.

Lrotlabel = text(
    text='L',
    height=0.1,
    depth=0.01,
    align='center',
    color=Lrotarrow.color
)
Lrotlabel.visible = arrowsvisible

Lrotimpulselabel = text(
    text='DL',
    align='center',
    height=0.1,
    depth=0.01,
    color=rotimpulsearrow.color
)

Lrotimpulselabel.visible = arrowsvisible

while True:
    rate(50)
    if self.dsy.mouse.clicked: # scene.mouse.clicked # pause the animation with a mouse click
        m = self.dsy.mouse.getclick() # scene.mouse.getclick()
        if m.pick is rotor:
            arrowsvisible = not arrowsvisible
            Lrotarrow.visible = arrowsvisible
            rotimpulsearrow.visible = arrowsvisible
            Lrotlabel.visible = arrowsvisible
            Lrotimpulselabel.visible = arrowsvisible
        else:
            while True:
                rate(50)
                if self.dsy.mouse.clicked: # scene.mouse.clicked
                    self.dsy.mouse.getclick() # scene.mouse.getclick()
                    break
            
    Fspring = -ks*norm(spring.axis)*(mag(spring.axis)-Lspring)

    torque = cross(-0.5*Lshaft*gyro.axis,Fspring)
    Lrot = Lrot+torque*dt
    p = p+(Fgrav+Fspring)*dt
    cm = cm+(p/M)*dt

    if omega > 0:
        gyro.axis = norm(Lrot)
    else:
        gyro.axis = -norm(Lrot)
    gyro.pos = cm-0.5*Lshaft*gyro.axis
    spring.axis = gyro.pos - top
    gyro.rotate(angle=omega*dt/4.)
    shaft.pos = gyro.pos
    shaft.axis = Lshaft*gyro.axis
    rotor.pos = gyro.pos+0.5*gyro.axis*(Lshaft-Drotor)
    rotor.axis = gyro.axis*Drotor

    # Update arrows representing angular momentum and angular impulse
    Lrotarrow.pos = gyro.pos+0.5*Lshaft*gyro.axis+vector(0,2.*Rshaft,0)
    Lrotarrow.axis = Lrot*Lrotscale
    rotimpulsearrow.pos = Lrotarrow.pos+Lrotarrow.axis
    rotimpulsearrow.axis = torque*dt*rotimpulsescale
    Lrotlabel.frame.pos = Lrotarrow.pos+Lrotarrow.axis/2.+vector(0,Rshaft,0)
    Lrotimpulselabel.frame.pos = rotimpulsearrow.pos+rotimpulsearrow.axis-vector(0,3.*Rshaft,0)

    if t == 0.: # make sure everything is set up before first visible display
        self.dsy.visible = 1 # scene.visible = 1
        self.dsy.autoscale = 0 # scene.autoscale = 0
    t = t+dt


