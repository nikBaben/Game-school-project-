import pygame

"""ВСЯ АНИМАЦИЯ ИГРЫ"""
#Тоже не нравится как выглядит, но по идеи это никак по другому не структурировать, мб придумаешь, тоже переделаешь.



"""Списки со всеми спрайтами"""
anim_fire=[]
anim_ship=[]
anim_can = []
anim_island = []
anim_enemy=[]
anim_shipplayer_moveup = []
anim_submarine = []
ainm_player_stand = []
blow_can_anim=[]
player_move_up = []
blow_ship_anim = []
blow_sub_anim = []
back = pygame.image.load("imgs/lll.png")
""""""


"""Анимация острова"""
for island in range(1,17): 
    file = "imgs/island{}.svg".format(island)
    img = pygame.image.load(file)
    anim_island.append(img)
""""""


"""Анимация подлодки"""
for submarine in range(1,18):
    sub_file = "imgs/submarine/submarine{}.svg".format(submarine)
    sub = pygame.image.load(sub_file)
    anim_submarine.append(sub)
""""""


"""Анимация взрыва бочки"""
for blow_can in range(1,6):
    blow_can_file = "imgs/blow_can{}.svg".format(blow_can)
    blow_can = pygame.image.load(blow_can_file)
    blow_can_anim.append(blow_can)
""""""


"""Анимация взрыва Вражеского корабля"""
for blow_ship in range(1,5):
    blow_ship_file = "imgs/blow_enemy{}.svg".format(blow_ship)
    blow_ship = pygame.image.load(blow_ship_file)
    blow_ship_anim.append(blow_ship)
""""""


"""Анимация взрыва подлодки"""
for blow_sub in range(1,6):
    blow_sub_file = "imgs/blow_sub{}.svg".format(blow_sub)
    blow_sub = pygame.image.load(blow_sub_file)
    blow_sub_anim.append(blow_sub)
""""""


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
for moveup in range(1,17):
    player_moveup_file = "imgs/player/player_move_up{}.svg".format(moveup)
    player_moveup =pygame.image.load(player_moveup_file)
    player_move_up.append(player_moveup)
""""""