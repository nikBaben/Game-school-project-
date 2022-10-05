import pygame

"""ВСЯ АНИМАЦИЯ ИГРЫ"""

anim_fire=[]
anim_ship=[]
anim_can = []
anim_island = []
can = pygame.image.load("imgs/island1.png")


"""Анимация Коробля"""
#for island in range(1,11): 
  #  file = "imgs/island{}.png".format(island)
   # img = pygame.image.load(file)
   # anim_island.append(img)
""""""

for j in range(1,13):
    filename = "imgs/fire_player_ship{}.svg".format(j)
    img = pygame.image.load(filename)
  
    anim_fire.append(img)

for i in range(1,15):
    file =  "imgs/ship_frame{}.svg".format(i)
    im = pygame.image.load(file)
  
    anim_ship.append(im)

for y in range(1,7): 
    file_name = "imgs/бочка{}.svg".format(y)
    img_can = pygame.image.load(file_name)
    anim_can.append(img_can)