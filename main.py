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
from styles import back_ground

# from dead_enemy import Dead_Enemy

inim = []

SCORES = 0

def run():
    global SCORES
    pygame.init()
    screen = pygame.display.set_mode((960, 1050))
    pygame.display.set_caption("Название игры")  # Надо придумать!!!
    # bg_color = back_ground

    enemy = Enemy(screen)
    inim.append(enemy)

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

    blow = Blow(screen)

    hit = False
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
        keys.movement(screen, player_ship, bullets)
        player_ship.move()
        # dead.output()
        keys.update_screen(back2, back, player_ship, bullets, island, can, enemy, enemy_gun, submarine, sub_gun, blow)

        '''КОРАБЛЬ ВРАГ'''
        if pygame.sprite.spritecollideany(enemy, bullets):
            enemy.death()
            SCORES += 1
            print(SCORES)
        if pygame.Rect.colliderect(player_ship.hitbox, enemy.hitbox):
            enemy.death()
            SCORES += 1
            print(SCORES)
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                # break
                time.sleep(1)
                sys.exit()
        if pygame.Rect.colliderect(player_ship.hitbox, enemy_gun.rect):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            enemy_gun.shot(enemy)
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(1)
                sys.exit()

        '''ПОДВОДНАЯ ЛОДКА'''
        if pygame.sprite.spritecollideany(submarine, bullets):
            submarine.death()
            SCORES += 1
            print(SCORES)
        if pygame.Rect.colliderect(player_ship.hitbox, submarine.hitbox):
            submarine.death()
            SCORES += 1
            print(SCORES)
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(1)
                sys.exit()
        if pygame.Rect.colliderect(player_ship.hitbox, sub_gun.rect):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            sub_gun.shot(submarine)
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(1)
                sys.exit()

        '''БОЧКА'''
        if pygame.sprite.spritecollideany(can, bullets):
            broke = True
            img = choice([1, 2])
            if img == 1:
                can.image = pygame.image.load('work_images/rocket.png')
            if img == 2:
                can.image = pygame.image.load('work_images/health.png')
        if pygame.Rect.colliderect(player_ship.hitbox, can.hitbox):
            if broke:
                broke = False
                if img == 1:
                    enemy.death()
                    submarine.death()
                    img = 3
                if img == 2:
                    if hit:
                        hit = False
                        player_ship.speed = 1
                        img = 3
                else:
                    if not hit:
                        hit = True
                        player_ship.speed = 0.5
                # player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
                can.death()
                can.image = pygame.image.load('work_images/can.png')
        if can.rect.y >= 1100:
            can.image = pygame.image.load('work_images/can.png')
            img = 3

        '''ОСТРОВ'''
        if pygame.Rect.colliderect(player_ship.hitbox, island.hitbox):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(1)
                sys.exit()


run()
