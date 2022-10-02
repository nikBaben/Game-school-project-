import pygame
from player_ship import Player_Ship
from gun import Gun
import keys
from pygame.sprite import Group
from island import Island
from can import Can
from enemy_ship import Enemy
from enemy_gun import Enemy_gun


def run():
    pygame.init()
    screen = pygame.display.set_mode((960, 1050))
    pygame.display.set_caption("Название игры")  # Надо придумать!!!
    # bg_color = (255, 255, 255)
    bg_color = (50, 141, 160)

    enemy = Enemy(screen)
    enemy_gun = Enemy_gun(screen, enemy)
    can = Can(screen)
    island = Island(screen)
    player_ship = Player_Ship(screen)
    gun = Gun(screen, player_ship)
    bullets = Group()

    while True:
        enemy_gun.update(enemy)
        enemy.moving_enemy()
        can.moving_can()
        island.moving()
        gun.output_bullet()
        bullets.update()
        keys.movement(screen, player_ship, bullets)
        player_ship.move()
        keys.update_screen(bg_color, screen, player_ship, bullets, island, can, enemy, enemy_gun)


run()
