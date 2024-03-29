import pygame, sys
from gun import Gun
import json
import random
import time

part = []
part1 = []
part2 = []
part3 = []

def movement(screen, player_ship, bullets, enemy, submarine, score_panel, start_menu, speedup, freq):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score_panel.new_score > score_panel.record:
                score_panel.record = score_panel.new_score
            with open('save.json', 'w') as file:
                json.dump(score_panel.record, file)
            with open('money.json', 'w') as file:
                json.dump(score_panel.balance, file)
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
                if player_ship.have_rocket:
                    enemy.death()
                    submarine.death()
                    score_panel.update()
                    score_panel.update()
                    speedup.rocket_shot = True
                    player_ship.have_rocket = False
                player_ship.sht = True  # Добавил поле sht для проверки стреляет корабль или нет
                new_bullet = Gun(screen, player_ship, freq)
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
        elif event.type == pygame.MOUSEMOTION:
            start_menu.update(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_menu.check_click(event.pos)


def update_screen(clock, color, back, screen, score_panel, bullets, island, player_ship, can, enemy, enemy_gun,
                  submarine,
                  sub_gun, blow, start_menu, freq):
    # ЗАПОЛЕНЕНИЯ ЗАДЕНГО ЭКРАНА, ПРИДУМАТЬ СПОСОБ!
    # screen.blit(bg_color,(0,0))
    # screen.blit(bg_color,(0,0))
    #  screen.fill(bg_color) Заполенение экрана белым цветом, сопоставим с  main() bg_color
    # dead.output()

    def particle(x, y):
        part.append([[x, y], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
        for p in part:
            p[0][0] += p[1][0]
            p[0][1] += p[1][1]
            p[2] -= 0.1
            # p[1][1] +=0.1
            pygame.draw.circle(screen, (132, 209, 225), [int(p[0][0]), int(p[0][1])], int(p[2]))
            if p[2] <= 0:
                part.remove(p)
    
    def particle1(x, y):
        part1.append([[x, y], [random.randint(0, 10) / 5 - 1, -2], random.randint(4, 6)])
        for p in part1:
            p[0][0] += p[1][0]
            p[0][1] += p[1][1]
            p[2] -= 0.1
            # p[1][1] +=0.1
            pygame.draw.circle(screen, (78,87,84), [int(p[0][0]), int(p[0][1])], int(p[2]))
            if p[2] <= 0:
                part1.remove(p)
    
    def particle2(x, y):
        part2.append([[x, y+15], [random.randint(0, 25) / 10 - 1, -2], random.randint(4, 12)])
        for p in part2:
            p[0][0] += p[1][0]
            p[0][1] += p[1][1]
            p[2] -= 0.1
            # p[1][1] +=0.1
            pygame.draw.circle(screen, (132, 209, 225), [int(p[0][0]), int(p[0][-1])], int(p[2]))
            if p[2] <= 0:
                part2.remove(p)
                
    def particle3(x, y):
        part3.append([[x, y-10], [random.randint(0, 25) / 10 - 1, -2], random.randint(4, 10)])
        for p in part3:
            p[0][0] += p[1][0]
            p[0][1] += p[1][1]
            p[2] -= 0.1
            # p[1][1] +=0.1
            pygame.draw.circle(screen, (132, 209, 225), [int(p[0][0]), int(p[0][1])], int(p[2]))
            if p[2] <= 0:
                part3.remove(p)
                
    screen.fill(color)
    back.output_back()
    island.output()
    enemy_gun.output_enemy_bullet()
   #enemy.output()
    can.output()
    #player_ship.output()
    submarine.output()
    sub_gun.output_enemy_bullet()
    particle3(enemy.rect.centerx, enemy.y + 150)
    particle(submarine.rect.centerx, submarine.y)
    particle1(sub_gun.rect.centerx, sub_gun.y)
    particle1(enemy_gun.rect.centerx, enemy_gun.y)
    if player_ship.moveup: 
        particle2(player_ship.rect.centerx, player_ship.y)
    else: 
        part2.clear()
    enemy.output()
    score_panel.draw_score()
    player_ship.output()
    # player_ship.output()

    start_menu.draw()
    if pygame.Rect.colliderect(player_ship.hitbox, enemy.hitbox) or pygame.sprite.spritecollideany(enemy, bullets):
        blow.rect.x = enemy.rect.x
        blow.rect.y = enemy.rect.y
        blow.draw('ship')
    if pygame.sprite.spritecollideany(submarine, bullets) or pygame.Rect.colliderect(player_ship.hitbox,
                                                                                     submarine.hitbox):
        blow.rect.x = submarine.rect.x
        blow.rect.y = submarine.rect.y
        blow.draw('sub')
    if pygame.sprite.spritecollideany(can, bullets) or pygame.Rect.colliderect(player_ship.hitbox, can.hitbox):
        if not can.change:
            blow.rect.x = can.rect.x
            blow.rect.y = can.rect.y
            blow.draw('can')
    ####

    ###
    for bullet in bullets.sprites():
        bullet.output_bullet()
        particle1(bullet.rect.centerx, bullet.y)
    clock.tick(freq)
    # pygame.display.set_caption(str(clock.get_fps()))
    pygame.display.flip()
 


def update_bullet(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
