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

# from dead_enemy import Dead_Enemy

inim = []


def run():
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
    back = Back(screen)
    blow = Blow(screen)

    hit = False
    while True:
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
        keys.update_screen(back, player_ship, bullets, island, can, enemy, enemy_gun, submarine, sub_gun, blow)

        '''КОРАБЛЬ ВРАГ'''
        if pygame.sprite.spritecollideany(enemy, bullets):
            enemy.death()
        if pygame.sprite.collide_rect(player_ship, enemy):
            enemy.death()
            # b = True
            blow.rect.x = 100
            blow.rect.y = 500
            blow.draw()
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(1)
                sys.exit()
        if pygame.sprite.collide_rect(player_ship, enemy_gun):
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
        if pygame.sprite.collide_rect(player_ship, submarine):
            submarine.death()
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(1)
                sys.exit()
        if pygame.sprite.collide_rect(player_ship, sub_gun):
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
            can.death()
        if pygame.sprite.collide_rect(player_ship, can):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            can.death()
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(1)
                sys.exit()

        '''ОСТРОВ'''
        if pygame.sprite.collide_rect(player_ship, island):
            player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                time.sleep(1)
                sys.exit()


run()
