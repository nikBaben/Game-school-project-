import pygame
from player_ship import Player_Ship
from gun import Gun
import keys
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((960, 1050))
    pygame.display.set_caption("Название игры") #Надо придумать!!!
    #bg_color = (255, 255, 255)
    bg_color = pygame.image.load("imgs/back1.svg")
    
    player_ship = Player_Ship(screen)
    gun = Gun(screen, player_ship)
    bullets = Group()

    while True:
   
        gun.output_bullet()
        bullets.update()
        keys.movement(screen, player_ship, bullets)
        player_ship.move()
        keys.update_screen(bg_color, screen, player_ship, bullets)


run()
