
from ursina import *
from ursina.prefabs.first_person_controller import * 
from ursina.prefabs.health_bar import *

class Player(Entity):
    def __init__(self, model, scale, position):
        super().__init__(model="cube", position= position, scale=(1,1,1), visible_self = False)

        self.collider = BoxCollider(self, center=Vec3(0, 1, 0), size=(1, 2, 1))
        camera.parent = self
        camera.position = (0,2,0)
        camera.rotation = (0,0,0)
        camera.fov = 69
        self.sword = None
        FirstPersonController()

    def health(lp):
        lp = 100
        hb = HealthBar(bar_color=color.lime, roundness =.5, scale=(.5, .04))
        hb.value = lp


        