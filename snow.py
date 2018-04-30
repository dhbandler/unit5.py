#Daniel Bandler
#4/30/18
#snow.py makes it snow

from ggame import *
from random import randint

SNOW = 1
WIDTH = 980
HEIGHT = 490


def step():
    moreSnow()
    for snow in data["snowlist"]:
        if snow.y <= HEIGHT:
            snow.y += 1
    
    
def moreSnow():
    data["frames"] += 1
    if data["frames"] == 50:
        data["snowlist"].append(Sprite(snow,(randint(1,WIDTH),0)))
    

if __name__ == "__main__":
    
    data = {}
    data["frames"] = 0
    data["snowlist"] = []
    
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    blue = Color(0x87ceeb,1)
    
    sky = RectangleAsset(WIDTH+40,HEIGHT+40,LineStyle(1,blue),blue)
    snow = CircleAsset(20,LineStyle(1,black), white)
    
    Sprite(sky)
    
    for i in range(SNOW):
        data["snowlist"].append(Sprite(snow,(randint(1,WIDTH),0)))
    
    App().run(step)
