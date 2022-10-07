import pygame, sys
from gun import Gun
from styles import back_ground
from backgorund import Back

def movement(screen, player_ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            '''движение'''
            if event.key == pygame.K_d:
                player_ship.moveright = True
            if event.key == pygame.K_a:
                player_ship.moveleft = True
            if event.key == pygame.K_w:
                player_ship.moveup = True
            if event.key == pygame.K_s:
                player_ship.movedown = True

            '''стрельба'''
            if event.key == pygame.K_SPACE:
                player_ship.sht = True  # Добавил поле sht для проверки стреляет корабль или нет
                new_bullet = Gun(screen, player_ship)
                bullets.add(new_bullet)





        elif event.type == pygame.KEYUP:
            '''движение'''
            if event.key == pygame.K_d:
                player_ship.moveright = False
            if event.key == pygame.K_a:
                player_ship.moveleft = False
            if event.key == pygame.K_w:
                player_ship.moveup = False
            if event.key == pygame.K_s:
                player_ship.movedown = False
            if event.key == pygame.K_SPACE:
                player_ship.sht = False  # убераем занчение True с shoot, если корабль не стреляет


def update_screen(back,player_ship, bullets, island, can, enemy, enemy_gun):
    # ЗАПОЛЕНЕНИЯ ЗАДЕНГО ЭКРАНА, ПРИДУМАТЬ СПОСОБ!
   # screen.blit(bg_color,(0,0))
   # screen.blit(bg_color,(0,0))
    #  screen.fill(bg_color) Заполенение экрана белым цветом, сопоставим с  main() bg_color
    # dead.output()
    back.output_back()
    enemy_gun.output_enemy_bullet()
    enemy.output()
    island.output()
    can.output()
    player_ship.output()
    ####

    ###
    for bullet in bullets.sprites():
        bullet.output_bullet()
    pygame.display.flip()


def update_bullet(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
