import pygame

"""ВСЯ АНИМАЦИЯ ИГРЫ"""
#Тоже не нравится как выглядит, но по идеи это никак по другому не структурировать, мб придумаешь, тоже переделаешь.



"""Списки со всеми спрайтами"""
anim_fire=[]
anim_ship=[]
anim_can = []
anim_island = []
anim_shipplayer_moveup = []
anim_enemy=[]
anim_submarine = []
ainm_player_stand = []
back_ground = pygame.image.load("imgs/back_ground.png")
back_ground2 = pygame.image.load("imgs/back_ground2.png")

""""""


#can = pygame.image.load("imgs/island1.png")


"""Анимация острова"""
for island in range(1,17): 
    file = "imgs/island{}.svg".format(island)
    img = pygame.image.load(file)
    anim_island.append(img)
""""""

for submarine in range(1,18):
    sub_file = "imgs/submarine/submarine{}.svg".format(submarine)
    sub = pygame.image.load(sub_file)
    anim_submarine.append(sub)



"""Анимация вражеского корабля"""
for enemy in range(1,13):
    filename = "imgs/enemy1_ship{}.svg".format(enemy)
    enemy = pygame.image.load(filename)
    anim_enemy.append(enemy)
""""""


"""Анимация Коробля при выстреле"""
for j in range(1,13):
    filename = "imgs/fire_player_ship{}.svg".format(j)
    img = pygame.image.load(filename)
    anim_fire.append(img)
""""""


"""Анимация Коробля при бездействии"""
for player_stand in range(1,18):
    player_stand = "imgs/player/player_stand{}.svg".format(player_stand)
    player_stand_file = pygame.image.load(player_stand)
    ainm_player_stand.append(player_stand_file)
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