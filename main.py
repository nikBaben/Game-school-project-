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
from styles import anim_ship


inim=[]
def run():
    pygame.init()
    screen = pygame.display.set_mode((960, 1050))
    pygame.display.set_caption("Название игры")  # Надо придумать!!!
    bg_color = (95,205,228)

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
        #Если не понравится, переделаешь, ну или найдешь другой способ
        #Выглядит пока что страшно, но что поделать) Надо будет придумать как это уменьшить и довести до идеала
        for gun in bullets: 
               if enemy.rect.collidepoint(gun.rect.center):
                    now = enemy.last_update #Скорее всего проблема заключается в этом) Счетчик кадров как-то странно работает, 
                                            #ну либо я тупой) Короче тоже посмотри, возможно тут не надо c класса (enemy) конкретный кадр брать
                                            #Можно будет попробовать прямо в цикле взять счетчик, и его обновлять

                    if now - enemy.last_update >enemy.frame_rate:
                        enemy.last_update = now
                        enemy.frame += 1 
                    else:
                        center = enemy.rect.center
                        enemy.image = anim_ship[enemy.frame]# Хз почему, но пока что поигрывается только 1 кадр, надо тоже исправить, мб у тебя получится
                        enemy.rect.center = center 
                        if enemy.frame == len(anim_ship)-13:# Из-за того что поигрывается 1 кадр, пришлось сдлеать такую зависимость, если будут все кадры поигрываться, тогда уберем -13
                            enemy.y = -600 
                            enemy.rect.centerx = enemy.screen_rect.centerx - spawn_x()
                            enemy.frame = 0
        """"""
           
                    
                
            
        """Коллизия для нрашего корабля"""
        for enemy in inim: 
            if player_ship.rect.colliderect(enemy): 
                player_ship.image = pygame.image.load("work_images/island.png")
        """"""
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
