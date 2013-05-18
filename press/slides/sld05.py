# -*- coding: utf-8 -*-

# from visual import *
# scene.range = 3

text(
     pos=(-8,9.2,-15),
     text=u'Sobre VPython!',
     color=(0,0.5,1), font=u'Tahoma',
     height=2
)

text(
     pos=(-7.2,7.1,-15),
     text=u'VPython 6 e wxPython',
     color=color.red, font=u'Tahoma',
     height=1.2
)

text(
     pos=(5,6.3,-15),
     text=u'(ou wxVPython)',
     color=color.orange,font=u'Tahoma',
     height=0.5
)

text(
    pos=(-6.2,4.8,-15),
    text=u'* Maior Portabilidade',
    color=color.yellow, font=u'Tahoma',
)

text(
    pos=(-6.2,2.8,-15),
    text=u'* Elimina Threads complexas',
    color=color.yellow, font=u'Tahoma',
)

text(
    pos=(-6.2,0.8,-15),
    text=u'* Mac - Python64 - Cocoa',
    color=color.yellow, font=u'Tahoma',
)

text(
    pos=(-6.2,-1.2,-15),
    text=u'* Animações:',
    color=color.yellow, font=u'Tahoma',
)

text(
    pos=(-5,-3.2,-15),
    text=u'* Rate',
    color=color.yellow, font=u'Tahoma',
)

text(
    pos=(-5,-5.2,-15),
    text=u'* Sleep',
    color=color.yellow, font=u'Tahoma',
)

cube = box(
   pos=(0,-7.2,-15),
   color=color.magenta,
)

while True:
    rate(50)
    cube.rotate(
       axis=(0,1,0), 
       angle=-1*2*70*pi/1e4
    )

