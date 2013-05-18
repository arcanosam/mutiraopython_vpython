# from visual import *
# Example of use of faces object for building arbitrary shapes (here, a cone)
# David Scherer July 2001

f = frame()

box( size=(0.5,0.5,0.5) )

N = 20

try:
    model = faces( pos = zeros( (N*3,3), float ), frame = f )
except:
    model = faces( pos = zeros( (N*3,3), Float ), frame = f )

t = arange(0,2*pi+2*pi/N,2*pi/N)

model.pos[0::3, 0] = sin(t[:-1])
model.pos[0::3, 2] = cos(t[:-1])

model.pos[1::3, 0] = sin(t[1:])
model.pos[1::3, 2] = cos(t[1:])

model.pos[2::3, 1] = 2

model.normal = model.pos
model.normal[2::3,0] = sin(t[1:])
model.normal[0::1,1] = 0.5
model.normal[2::3,2] = cos(t[1:])

model.color = model.pos

for vertex in range(3*N):
    hue = float(vertex // 3)/N
    model.color[vertex] = color.hsv_to_rgb((hue,1,1))


while True:
    rate(100)
    f.rotate(angle=0.01)
