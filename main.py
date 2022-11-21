from ursina import *
from ursina import curve
from player import Player
from monster import * 
from ursina.prefabs.first_person_controller import *
import keyboard
import time

app = Ursina()
sword = Entity(model = "models/sword.obj", parent = camera, texture = "textures/sword.png", position =(2,0,2.5), rotation=(0, 90, 0))
def input(key):
    # Attacking
    if key == "z":       
        sword.animate("rotation", sword.rotation + Vec3(0, 0, -90), duration = 0.25, curve = curve.linear)
    elif key == "x":
        sword.animate("rotation", sword.rotation + Vec3(0, 0, -sword.rotation_z), duration = 0.05, curve = curve.linear)
    
            
                            
        
class Scenery:
    def map(self):
        
        ground = Entity(model="plane", collider="box", scale=64, texture="grass", texture_scale=(4,4))
        Sky()
    
s = Scenery()
m = Monster()      
if __name__ == "__main__":
    s.map()
    Monster()
    #Monster.m_health(lp2=30)
    Player("cube", (0, 10, 10), "box")
    Player.health(lp=100)



    
    
    app.run()