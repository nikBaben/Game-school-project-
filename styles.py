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
anim_skin1 = []
skin_1_anim = []
skin4 = pygame.image.load("work_images/skin_1.png")
#skin2 = pygame.image.load("work_images/skin_2.png")
#skin3 = pygame.image.load("work_images/skin_3.png")
back = pygame.image.load("imgs/lll.png")
vidi = "imgs/game_back.mp4"
back_for_vidi = pygame.image.load("imgs/for_vid.png")
back_for_dy = pygame.image.load("imgs/back_for_dye.png")
back_for_dye = pygame.transform.scale(back_for_dy, (960, 1050)) 
menu1 = pygame.image.load("imgs/menu2.png")
back_skins = pygame.image.load("imgs/фон для магазина.png")
anim_skin2 = []
skin3 = pygame.image.load("imgs/skin3.svg")
image_big = pygame.transform.scale(skin3, (150, 200))
skin2 = pygame.image.load("imgs/скин2.png")
image_small = pygame.transform.scale(skin2, (120, 150))
back_dead = pygame.image.load("imgs/фон для смерти.png")

#skins_1 = pygame.image.load("imgs/skin s1.png")






""""""


"""Анимация острова"""
for island in range(1,17): 
    file = "imgs/island{}.svg".format(island)
    img = pygame.image.load(file)
    anim_island.append(img)
""""""

for skin1 in range(1,18): 
    sub_file1 = "imgs/submarine/submarine{}.svg".format(skin1)
    sub1 = pygame.image.load(sub_file1)
    anim_skin1.append(sub1)


for skin2 in range(2,21): 
    skin2_file = "imgs/skins/скин{}.png".format(skin2)
    skin_2 = pygame.image.load(skin2_file)
    anim_skin2.append(skin_2)
    

"""Анимация подлодки"""
for submarine in range(1,18):
    sub_file = "imgs/submarine/submarine{}.svg".format(submarine)
    sub = pygame.image.load(sub_file)
    anim_submarine.append(sub)
""""""

"""скин 1"""
for skin_1 in range(1,20):
    skin_1_file = "imgs/first_skin{}.png".format(skin_1)
    skin_1 = pygame.image.load(skin_1_file)
    skin_1_anim.append(skin_1)
    
    
    
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
for moveup in range(1,61):
    player_moveup_file = "imgs/player/player_move_up{}.svg".format(moveup)
    player_moveup =pygame.image.load(player_moveup_file)
    player_move_up.append(player_moveup)
""""""