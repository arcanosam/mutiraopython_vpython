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
    pos=(-3,7.1,-15),
    text=u'O que é?',
    color=color.red, font=u'Tahoma',
    height=1.2
)

fotob = materials.texture(
    data=materials.loadTGA('img\\bsw1283'),
)

bbswf = box(
    pos=(-1.5,1,0),
    axis=(0,0,1),
    material=fotob
)

bbswf.rotate(
    angle=-pi/2,
    axis=(0,0,1)
)
bbswf.rotate(
    angle=radians(196),
    axis=(0,1,0)
)
bbswf.rotate(
    angle=radians(10),
    axis=(1,0,0)
)


label(
    pos=bbswf.pos+(-0.22,0.5,0),
    text=u'Maintainer',
    xoffset=-15,yoffset=15,
    color=color.red
)

label(
    pos=bbswf.pos+(-0.05,-0.55,0), 
    text='Bruce Sherwood',
    xoffset=0, yoffset=-15,
    color=(0.7,0,1)
)

bbswf.rotate(angle=-pi/2)

bsw_text = ''.join([
    u'"...make it possible for\n',
    u'users who know nothing\n',
    u'about CGs to be able to\n',
    u'write programs that ge-\n',
    u'nerate navigable real-time\n'
    u'3D animations."'
])

bswtxt3d = text(
     pos=(-3.3,5.2,-15),
     text=bsw_text,
     color=color.yellow, font=u'Tahoma',
     height=0.8
)

text(
     pos=(-3.8,-2.5,-15),
     text=u'Aplicabilidade',
     color=color.red, font=u'Tahoma',
     height=1.2
)

appfst = text(
     pos=(-2.2,-10.5,-15),
     text=u'Ensino', align='left',
     color=color.white, font=u'Tahoma',
     height=1.2
)

appscd = text(
     pos=(-3.3,-9.6,-15),
     text=u'Simulação',
     color=color.cyan, font=u'Tahoma',
     height=1.2
)

appthd = text(
     pos=(0,-4.3,-15),
     text=u'Prototipação',
     color=color.magenta, font=u'Tahoma',
)

appscd.rotate(angle=pi/3.2,axis=(0,0,1))
appthd.rotate(angle=-pi/2.8,axis=(0,0,1))