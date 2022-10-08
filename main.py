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
    # dead_enemy = Dead_enemy(screen, enemy)a
    can = Can(screen)
    island = Island(screen)
    player_ship = Player_Ship(screen)
    gun = Gun(screen, player_ship)
    bullets = Group()
    back = Back(screen)

    while True:
        """"""

        """Коллизия для нрашего корабля"""
        for enemy in inim:
            if player_ship.rect.colliderect(enemy):
                player_ship.image = pygame.image.load("work_images/island.png")
        """"""
        # dead_enemy.output()
        #  screen.blit(bg_color,(0,0))

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
        keys.update_screen(back, player_ship, bullets, island, can, enemy, enemy_gun, submarine, sub_gun)


run()
