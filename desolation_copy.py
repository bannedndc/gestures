import numpy
import pygame as pg
import time

pg.mixer.init()
pg.init()

elbow = pg.mixer.Sound("sounds/fall.wav")

elbow.play()
# sounds = [elbow]
# 
# pg.mixer.set_num_channels(50)
# 
# cameo = []
# for i in range(8):
#     elbow.play()
#     # sounds[cameo[i]].play()
#     # sounds[alex[i]].play()
#     # sounds[sierra[i]].play()
#     # sounds[cameo[i]].play()
#     time.sleep(0.545)
