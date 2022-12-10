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
from backgorund import Back
from submarine import Submarine
from sub_gun import Sub_gun
from keys import update_bullet
import time
from blow import Blow
from random import choice
from score_panel import Score_panel
# from score_counter import draw_text
from styles import anim_can
from menu import Menu, MenuItem

inim = []


# print(pygame.font.get_fonts())


def run():
    pygame.init()
    screen = pygame.display.set_mode((960, 1050))
    pygame.display.set_caption("SHIP WARS")  # Надо придумать!!!
    color = (95, 205, 228)
    enemy = Enemy(screen)
    inim.append(enemy)
    try:
        file = open('save.json')
        score = (json.load(file))
    except:
        score = 0

    score_panel = Score_panel(screen, score)
    submarine = Submarine(screen)
    enemy_gun = Enemy_gun(screen, enemy)
    sub_gun = Sub_gun(screen, submarine)
    can = Can(screen)
    island = Island(screen)
    player_ship = Player_Ship(screen)
    gun = Gun(screen, player_ship)
    bullets = Group()
    back = Back(screen)

    '''КНОПКИ'''

    def start_game():
        Game(screen, color, enemy, score_panel, submarine, enemy_gun, sub_gun, can, island, player_ship, gun, bullets,
             back, blow, start_menu)

    def end_game():
        if score_panel.new_score > score_panel.record:
            score_panel.record = score_panel.new_score
        with open('save.json', 'w') as file:
            json.dump(score_panel.record, file)
        sys.exit()

    def score_del():
        if Score_panel:
            with open('save.json', 'w') as file:
                json.dump(0, file)
            score_panel.zeroing()

    start_menu = Menu(screen)
    start_menu.add_item(MenuItem('Начать игру', start_game, (start_menu.cur_x, start_menu.cur_y)))
    start_menu.add_item(MenuItem('Выход', end_game, (start_menu.cur_x, start_menu.cur_y)))
    start_menu.add_item(MenuItem('Сбросить счет', score_del, (start_menu.cur_x, start_menu.cur_y)))
    '''КНОПКИ'''
    blow = Blow(screen)

    hit = False
    broke = False
    speedup = False
    while True:
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
        blow.draw("nothing")
        score_panel.draw_score()
        keys.movement(screen, player_ship, bullets, enemy, submarine, score_panel, start_menu)
        keys.update_screen(color, back, screen, score_panel, bullets, island, player_ship, can, enemy, enemy_gun,
                           submarine, sub_gun,
                           blow, start_menu)

        if (score_panel.new_score > 0) and (score_panel.new_score % 50) == 0:
            if not speedup:
                enemy.speed += 0.3
                submarine.speed += 0.3
                can.speed += 0.3
                island.speed += 0.3
                sub_gun.speed += 0.3
                enemy_gun.speed += 0.3
                speedup = True
        if (score_panel.new_score > 0) and (score_panel.new_score % 50) != 0:
            speedup = False
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
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                time.sleep(2)
                sys.exit()
        if pygame.Rect.colliderect(player_ship.hitbox, enemy_gun.rect):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            enemy_gun.shot(enemy)
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                time.sleep(2)
                sys.exit()

        '''ПОДВОДНАЯ ЛОДКА'''
        if pygame.sprite.spritecollideany(submarine, bullets):
            # blow.draw("sub")
            # submarine.dead = False
            submarine.blow = True

        if submarine.hit == True:
            if submarine.dead == True:
                submarine.death()
                score_panel.update()
        # else:
        #   pass
        # submarine.blow = False
        if pygame.Rect.colliderect(player_ship.hitbox, submarine.hitbox):
            submarine.death()
            score_panel.update()
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                time.sleep(2)
                sys.exit()
        if pygame.Rect.colliderect(player_ship.hitbox, sub_gun.rect):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            sub_gun.shot(submarine)
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                time.sleep(2)
                sys.exit()

        '''БОЧКА'''
        if pygame.sprite.spritecollideany(can, bullets):
            if not broke:
                can.change = True
                broke = True
                can.broke = True
                can.blow = True
                img = choice([1, 2])
                if img == 1:
                    can.broke_heart = False
                    can.broke_rocket = True
                # can.blow = False
                #    can.image = pygame.image.load("imgs/heart.svg")
                if img == 2:
                    can.broke_rocket = False
                    can.broke_heart = True
                # can.blow = False

            #   can.image = pygame.image.load('imgs/rocket.svg')
        if pygame.Rect.colliderect(player_ship.hitbox, can.hitbox):
            if broke:
                if img == 1:
                    player_ship.have_rocket = True
                    can.death()
                    can.broke = False
                    can.broke_rocket = False
                # can.image = imge_for_can
                else:
                    if hit:
                        hit = False
                        player_ship.speed = 1
                        can.broke = False
                        can.broke_heart = False
                    can.change = False
                    can.death()

                #  can.image = imge_for_can
            else:
                if not hit:
                    hit = True
                    player_ship.speed = 0.5
                    can.change = False
                    can.death()
                else:
                    if score_panel.new_score > score_panel.record:
                        score_panel.record = score_panel.new_score
                    with open('save.json', 'w') as file:
                        json.dump(score_panel.record, file)
                    time.sleep(2)
                    sys.exit()
            #  can.image =imge_for_can
            broke = False
            can.broke = False
            can.broke_heart = False
            can.broke_rocket = False
        if can.rect.y >= 1100:
            # can.image = imge_for_can
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
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                time.sleep(2)
                sys.exit()
        if pygame.Rect.colliderect(enemy.hitbox, island.hitbox):
            enemy.death()
        if pygame.Rect.colliderect(submarine.hitbox, island.hitbox):
            submarine.death()
        if pygame.Rect.colliderect(island.hitbox, can.hitbox):
            can.death()


run()
