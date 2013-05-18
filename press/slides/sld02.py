# -*- coding: utf-8 -*-

# from visual import *
# scene.range = 3

sldtext1 = u''.join([
    u'O que veremos:\n\n',
])

sldtext2 = u''.join([
    u'1) Instalação:\n',
    u'---> Windows\n',
    u'---> Linux\n',
    u'---> Mac'
])

sldtext3 = u''.join([
    u'2) Sobre VPython:\n',
    u'----> O que é?\n',
    u'----> Aplicabilidade\n',
    u'----> VPython 6 e wxPython !!'
])


text(
    pos=(-10,10.5,-15),
    text=sldtext1,
    color=color.green, font=u'Tahoma'
)

text(
    pos=(-7,7.5,-15),
    text=sldtext2, 
    color=color.yellow, font=u'Tahoma'
)

text(
    pos=(-7,1.6,-15),
    text=sldtext3,
    color=(0,0.5,1), font=u'Tahoma'
)

text(
    pos=(-7,-7,-15),
    text=u'EXEMPLOS !!!!!',
    color=(1,0,0.6), font=u'Tahoma',
    height=2
)