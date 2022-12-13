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
import random

pygame.init()
screen = pygame.display.set_mode((960, 1050))
pygame.display.set_caption("SHIP WARS")  # Надо придумать!!!
color = (95, 205, 228)

enemy = Enemy(screen)
submarine = Submarine(screen)
enemy_gun = Enemy_gun(screen, enemy)
sub_gun = Sub_gun(screen, submarine)
can = Can(screen)
island = Island(screen)
bullets = Group()
back = Back(screen)

current = None
particles = []


def emit_particle(x, y, x_vel, y_vel, radius):
    particles.append([[x, y], [x_vel, y_vel], radius])


def update_particle():
    for i, particle in reversed(list(enumerate(particles))):
        particle[1][1] += particle[1][0]
        particle[1][1] += particle[1][0]

        particle[2] -= 0.05

        reversed_particle = particles[len(particles) - i - 1]
        pygame.draw.circle(screen, (255, 255, 255), (int(reversed_particle[0][0]), int(reversed_particle[0][1])),
                           reversed_particle[2])
        if particle[2] <= 0:
            particles.pop(i)


def switch(scene):
    global current
    current = scene


def menu():
    try:
        file = open('save.json')
        score = (json.load(file))
    except:
        score = 0
    runing = True
    score_panel = Score_panel(screen, score)

    def start_game():
        switch(run)

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
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                switch(None)
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                switch(deadi)
                runing = False
            elif event.type == pygame.MOUSEMOTION:
                start_menu.update(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_menu.check_click(event.pos)
                x, y = event.pos
                if (480 < x < 663) and (380 < y < 430):
                    runing = False
        # if not stop:
        #     runing = False
        #     switch(run)
        # font = pygame.font.Font("imgs/retro-land-mayhem.ttf", 50)
        # new_score_img = font.render(f'{str("Press (q) to start")}', True, (255, 255, 255))
        screen.fill((255, 0, 0))
        # screen.blit(new_score_img, (100, 100))
        start_menu.draw()
        score_panel.draw_record()
        mx, my = pygame.mouse.get_pos()
        emit_particle(mx, my, 12, random.uniform(-12, 12), random.uniform(-12, 12))
        update_particle()
        pygame.display.flip()


def deadi():
    runing = True
    while runing:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                runing = False
                switch(None)
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_g:
                switch(run)
                runing = False
        font = pygame.font.Font("imgs/retro-land-mayhem.ttf", 25)
        new_score_img = font.render(f'{str("XAXAXAXA  LOSER press (g) to try again")}', True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(new_score_img, (230, 500))
        pygame.display.flip()


def run():
    try:
        file = open('save.json')
        score = (json.load(file))
    except:
        score = 0

    score_panel = Score_panel(screen, score)
    player_ship = Player_Ship(screen)
    gun = Gun(screen, player_ship)
    start_menu = Menu(screen)

    blow = Blow(screen)

    def go_to_menu():
        print(1111111111111111111111111111111111)
        if score_panel.new_score > score_panel.record:
            score_panel.record = score_panel.new_score
        with open('save.json', 'w') as file:
            json.dump(score_panel.record, file)
        switch(menu)

    '''КНОПКИ'''
    start_menu.add_item(MenuItem('Выход в меню', go_to_menu, (0, 0)))
    '''КНОПКИ'''

    hit = False
    broke = False
    speedup = False
    runing = True
    while runing:
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
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                runing = False
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
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                runing = False

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
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                runing = False
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
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                runing = False

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
                    submarine.death()
                    can.death()
                    enemy.death()
                    island.y = -500
                    switch(deadi)
                    runing = False
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
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                runing = False
        if pygame.Rect.colliderect(enemy.hitbox, island.hitbox):
            enemy.death()
        if pygame.Rect.colliderect(submarine.hitbox, island.hitbox):
            submarine.death()
        if pygame.Rect.colliderect(island.hitbox, can.hitbox):
            can.death()


switch(menu)
while current is not None:
    current()

pygame.quit()
