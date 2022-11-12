import json

import pygame, sys
from player_ship import Player_Ship
from gun import Gun
import keys
from pygame.sprite import Group
from island import Island
from can import Can
from enemy_ship import Enemy
from enemy_gun import Enemy_gun
from enemy_ship import spawn_x
from styles import anim_ship
from backgorund import Back, Back2
from submarine import Submarine
from sub_gun import Sub_gun
from keys import update_bullet
import time
from blow import Blow
from random import choice
from score_panel import Score_panel
# from score_counter import draw_text
from styles import back_ground
from styles import anim_can

# from dead_enemy import Dead_Enemy

inim = []


def run():
    pygame.init()
    screen = pygame.display.set_mode((960, 1050))
    pygame.display.set_caption("SHIP WARS")  # Надо придумать!!!
    # bg_color = back_ground
    game_over = False

    enemy = Enemy(screen)
    inim.append(enemy)
    try:
        file = open('save.json')
        score = (json.load(file))
    except:
        score = 0

    score_panel = Score_panel(screen, score)
    try:
        file = open('save.json')
        score_panel.score = (json.load(file))
    except:
        pass
    score_panel.update()
    submarine = Submarine(screen)
    enemy_gun = Enemy_gun(screen, enemy)
    sub_gun = Sub_gun(screen, submarine)
    # dead_enemy = Dead_enemy(screen, enemy)
    can = Can(screen)
    island = Island(screen)
    player_ship = Player_Ship(screen)
    gun = Gun(screen, player_ship)
    bullets = Group()
    back2 = Back2(screen)
    back = Back(screen)
    imge_for_can  = anim_can[0].convert_alpha()

    blow = Blow(screen)

    hit = False
    broke = False
    while True:
        back2.down()
        # bg_color = back_ground
        back.scroling()
        update_bullet(bullets)
        sub_gun.update(submarine)
        submarine.moving_sub()
        enemy_gun.update(enemy)
        enemy.moving_enemy()
        can.moving_can()
        island.moving()
        gun.output_bullet()
        bullets.update()
        player_ship.move()
        score_panel.draw_score()
        keys.movement(screen, player_ship, bullets, enemy, submarine, score_panel)
        # dead.output()
        keys.update_screen(back2, back, player_ship, bullets, island, can, enemy, enemy_gun, submarine, sub_gun,
                           blow, score_panel)

        '''КОРАБЛЬ ВРАГ'''
        if pygame.sprite.spritecollideany(enemy, bullets):
            enemy.death()
            score_panel.update()
        if pygame.Rect.colliderect(player_ship.hitbox, enemy.hitbox):
            enemy.death()
            score_panel.update()
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(2)
                sys.exit()
        if pygame.Rect.colliderect(player_ship.hitbox, enemy_gun.rect):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            enemy_gun.shot(enemy)
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(2)
                sys.exit()

        '''ПОДВОДНАЯ ЛОДКА'''
        if pygame.sprite.spritecollideany(submarine, bullets):
            submarine.death()
            score_panel.update()
        if pygame.Rect.colliderect(player_ship.hitbox, submarine.hitbox):
            submarine.death()
            score_panel.update()
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(2)
                sys.exit()
        if pygame.Rect.colliderect(player_ship.hitbox, sub_gun.rect):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            sub_gun.shot(submarine)
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(2)
                sys.exit()

        '''БОЧКА'''
        if pygame.sprite.spritecollideany(can, bullets):
            broke = True
            can.broke = True
            img = choice([1, 2])
            if img == 1:
                can.broke_heart = False
                can.broke_rocket = True
            #    can.image = pygame.image.load("imgs/heart.svg")
            if img == 2:
                can.broke_rocket = False
                can.broke_heart = True

             #   can.image = pygame.image.load('imgs/rocket.svg')
        if pygame.Rect.colliderect(player_ship.hitbox, can.hitbox):
            if broke:
                if img == 1:
                    player_ship.have_rocket = True
                    can.death()
                    score_panel.update()
                    score_panel.update()
                    can.broke = False
                    can.broke_rocket = False
                   # can.image = imge_for_can
                else:
                    if hit:
                        hit = False
                        player_ship.speed = 1
                        can.death()
                        can.broke = False
                        can.broke_heart = False
                  #  can.image = imge_for_can
            else:
                if not hit:
                    hit = True
                    player_ship.speed = 0.5
                    can.death()
                else:
                    time.sleep(2)
                    sys.exit()
              #  can.image =imge_for_can
            broke = False
            can.broke = False
            can.broke_heart = False
            can.broke_rocket = False
        if can.rect.y >= 1100:
            #can.image = imge_for_can
            broke = False
            can.broke = False
            can.broke_heart = False
            can.broke_rocket = False

        '''ОСТРОВ'''
        if pygame.Rect.colliderect(player_ship.hitbox, island.hitbox):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(2)
                sys.exit()


run()
