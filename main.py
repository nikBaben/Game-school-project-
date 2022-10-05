import pygame,sys
from player_ship import Player_Ship
from gun import Gun
import keys
from pygame.sprite import Group
from island import Island
from can import Can
from enemy_ship import Enemy
from enemy_gun import Enemy_gun
from enemy_ship import spawn_x
import time 
inim=[]
def run():
    pygame.init()
    screen = pygame.display.set_mode((960, 1050))
    pygame.display.set_caption("Название игры")  # Надо придумать!!!
    bg_color = (83, 193, 215)

    enemy = Enemy(screen)
    inim.append(enemy)

    enemy_gun = Enemy_gun(screen, enemy)
    # dead_enemy = Dead_enemy(screen, enemy)a
    can = Can(screen)
    island = Island(screen)
    player_ship = Player_Ship(screen)
    gun = Gun(screen, player_ship)
    bullets = Group()

    while True:
        """Коллизия для вражеского корабля"""
        #Если не  понравится, переделаешь, ну или найдешь другой способ
        for gun in bullets: 
               if enemy.rect.collidepoint(gun.rect.center):
                    pygame.image.load("work_images/island.png")
                    enemy.y = -600
                    enemy.rect.centerx = enemy.screen_rect.centerx - spawn_x()
        """"""
        for enemy in inim: 
            if player_ship.rect.colliderect(enemy): 
                player_ship.image = pygame.image.load("work_images/island.png")
                pygame.QUIT
                sys.exit()
              
           
           # player_ship.kill()dw
      #  for player_ship in bullets: 
             #  if enemy.rect.collidepoint(player_ship.rect.center):
               #     pygame.image.load("work_images/island.png")
                #    player_ship.remove()
                 #   enemy.rect.centerx = enemy.screen_rect.centerx - spawn_x()
       

        # dead_enemy.output()
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
