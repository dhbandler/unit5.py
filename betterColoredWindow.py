#Daniel
#3/28/18
#colorChangeWindow.py changes color randomly
from ggame import *
from random import randint

def mouseClick(event):
    num = randint(0,4)
    Sprite(color[num])

green = Color(0x006600,1)
brown = Color(0x8B4513,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)
red = Color(0xFF0000,1)

color = []
    
color.append(RectangleAsset(1000,1000,LineStyle(1,green),green))
color.append(RectangleAsset(1000,1000,LineStyle(1,brown),brown))
color.append(RectangleAsset(1000,1000,LineStyle(1,black),black))
color.append(RectangleAsset(1000,1000,LineStyle(1,yellow),yellow))
color.append(RectangleAsset(1000,1000,LineStyle(1,red),red))

App.listenMouseEvent("click", mouseClick)

App().run()

