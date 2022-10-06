import pygame

"""ВСЯ АНИМАЦИЯ ИГРЫ"""
#Тоже не нравится как выглядит, но по идеи это никак по другому не структурировать, мб придумаешь, тоже переделаешь.



"""Списки со всеми спрайтами"""
anim_fire=[]
anim_ship=[]
anim_can = []
anim_island = []
anim_shipplayer_moveup = []
""""""


can = pygame.image.load("imgs/island1.png")


"""Анимация Коробля"""
#for island in range(1,11): 
  #  file = "imgs/island{}.png".format(island)
   # img = pygame.image.load(file)
   # anim_island.append(img)
""""""


"""Анимация Коробля при выстреле"""
for j in range(1,13):
    filename = "imgs/fire_player_ship{}.svg".format(j)
    img = pygame.image.load(filename)
    anim_fire.append(img)
""""""


"""Анимация Коробля при бездействии"""
for i in range(1,15):
    file =  "imgs/ship_frame{}.svg".format(i)
    im = pygame.image.load(file)
    anim_ship.append(im)
""""""


"""Анимация для бочки"""
for y in range(1,7): 
    file_name = "imgs/бочка{}.svg".format(y)
    img_can = pygame.image.load(file_name)
    anim_can.append(img_can)
""""""


"""Анимация для передвижения корабля вперед"""
for moveup in range(1,33): 
    filename_up= "imgs/player_ship_moveup{}.svg".format(moveup)
    img_moveup = pygame.image.load(filename_up)
    anim_shipplayer_moveup.append(img_moveup)
""""""