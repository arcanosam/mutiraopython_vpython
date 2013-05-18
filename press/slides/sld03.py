# -*- coding: utf-8 -*-

# from visual import *
# scene.range = 3

text(
     pos=(-5,9.2,-15),
     text=u'Instalação',
     color=color.green, font=u'Tahoma',
     height=2
)

twin = materials.texture(
    data=materials.loadTGA('img\wtex128')
)

tlin = materials.texture(
    data=materials.loadTGA('img\ltex128')
)

tmco = materials.texture(
    data=materials.loadTGA('img\mtex128')
)

lwin = box(
    pos=(-1.8,1.5,0),
    axis=(0,0,1),
    material=twin
)

llin = box(
    pos=(-1.8,0,0),
    axis=(0,0,1),
    material=tlin
)

lmco = box(
    pos=(-1.8,-1.5,0),
    axis=(0,0,1),
    material=tmco
)

lwin.rotate(angle=pi)
lwin.rotate(
    angle=radians(198),
    axis=(0,1,0)
)
lwin.rotate(
    angle=radians(16),
    axis=(1,0,0)
)

llin.rotate(angle=pi)
llin.rotate(
    angle=radians(198),
    axis=(0,1,0)
)

lmco.rotate(angle=pi)
lmco.rotate(
    angle=radians(195),
    axis=(0,1,0)
)
lmco.rotate(
    angle=radians(348),
    axis=(1,0,0)
)

text(
    pos=(-2.8,3,-7),
    text=u'Executável',
    color=color.yellow, font=u'Tahoma',
    height=1
)

text(
    pos=(-2.8,0.2,-7),
    text=u'Arq. TGZ\nLeia o INSTALL.txt!', 
    color=color.yellow, 
    font=u'Tahoma',
    height=0.8
)

text(
    pos=(-2.8,-3.5,-9.5),
    text=u'DMG no\n"Applications"\nDirectory', 
    color=color.yellow, font=u'Tahoma',
    height=0.9
)