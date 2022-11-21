from ursina import * 
from ursina.prefabs.health_bar import *

class Monster(Entity):
    def __init__(self, position=(0, 0, 10), scale=(2,2,2)):
        super().__init__(model="models/mon.obj",
         position = position, 
         scale = scale, collider = "box", texture="textures/green.jpg")

        self.follow = None

    def m_health(lp2):
        lp2 = 30
        hb = HealthBar(bar_color=color.red, roundness =.5, scale=(.5, .08))
        hb=lp2

    def movement(self):
        pass
    
    