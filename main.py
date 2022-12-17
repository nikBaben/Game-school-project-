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
from checker import Checker
import random
from vid import Video
from styles import vidi, back_for_vidi, back_for_dye, menu1
from skins import Skins_changer
from speeduper import Speedup

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
checker = Checker()
video = Video(vidi)
skins = Skins_changer()
current = None

particles = []
backi = back_for_vidi.convert_alpha()
back_for_dye2 = back_for_dye.convert_alpha()
backi.set_alpha(225)

font_logo = pygame.font.Font("imgs/tetx.ttf", 70)
font_lose = pygame.font.Font("imgs/tetx.ttf", 40)
text_logo = font_logo.render('SHIP WARS', False, (0, 255, 255))
text_lose = font_lose.render('ВЫ ПРОИГРАЛИ!', False, (0, 255, 255))


def emit_particle(x, y, x_vel, y_vel, radius):
    particles.append([[x, y], [x_vel, y_vel], radius])


def update_particle():
    for i, particle in reversed(list(enumerate(particles))):
        particle[1][1] += particle[1][0]
        particle[1][1] += particle[1][0]

        particle[2] -= 0.05

        reversed_particle = particles[len(particles) - i - 1]
        pygame.draw.circle(screen, (0, 255, 255), (int(reversed_particle[0][0]), int(reversed_particle[0][1])),
                           reversed_particle[2])
        if particle[2] <= 0:
            particles.pop(i)


def switch(scene):
    global current
    current = scene


def menu():
    video.play()

    try:
        file = open('save.json')
        score = (json.load(file))
    except:
        score = 0

    try:
        file = open('money.json')
        money = (json.load(file))
    except:
        money = 0

    score_panel = Score_panel(screen, score, money)
    score_panel.menu = True

    def start_game():
        switch(run)
        checker.menu = False
        score_panel.menu = False

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

    def go_skins():
        switch(skins_menu)
        checker.menu = False

    start_menu = Menu(screen)
    # start_menu.add_item(MenuItem('SHIP WARS', start_game, (start_menu.cur_x - 60.5, start_menu.logo_y)))
    start_menu.add_item(MenuItem('ИГРАТЬ', start_game, (start_menu.cur_x - 105, start_menu.cur_y)))
    start_menu.add_item(MenuItem('ВЫХОД', end_game, (start_menu.cur_x - 87.5, start_menu.cur_y)))
    start_menu.add_item(MenuItem('ВЫБРАТЬ СКИН', go_skins, (start_menu.cur_x - 210, start_menu.cur_y)))
    start_menu.add_item(MenuItem('СБРОСИТЬ СЧЕТ', score_del, (start_menu.cur_x - 227.5, start_menu.cur_y)))
    runing = True
    while runing:
        if not checker.menu:
            checker.menu = True
            video.stop()
            runing = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                switch(None)
                video.stop()
                sys.exit()

            # runing = False
            elif event.type == pygame.MOUSEMOTION:
                start_menu.update(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_menu.check_click(event.pos)

        video.draw_to(screen, (0, 0))
        # screen.fill((255, 0, 0))
        t = video.current_time.format("%h:%m:%s")
        if t == "00:02:26":
            video.restart()
        # screen.blit(backi, (0, 0))
        a = menu1.convert_alpha()
        screen.blit(a, (150, 100))
        # screen.blit(text_logo, (200, 200))
        start_menu.draw()
        score_panel.draw_record()
        score_panel.draw_balance()
        ## mx, my = pygame.mouse.get_pos()
        # emit_particle(mx, my, 12, random.uniform(-12, 12), random.uniform(-12, 12))
        # update_particle()
        pygame.display.flip()


def deadi():
    def go_menu():
        switch(menu)
        checker.deadi = False

    def go_play():
        switch(run)
        checker.deadi = False

    start_menu = Menu(screen)
    start_menu.add_item(MenuItem('ВЕРНУТЬСЯ В МЕНЮ', go_menu, (start_menu.cur_x - 280, 400)))
    start_menu.add_item(MenuItem('НАЧАТЬ ЗАНОВО', go_play, (start_menu.cur_x - 227.5, 450)))

    runing = True
    while runing:
        if not checker.deadi:
            checker.deadi = True
            runing = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
                switch(None)
            elif event.type == pygame.MOUSEMOTION:
                start_menu.update(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_menu.check_click(event.pos)

        # font = pygame.font.Font("imgs/retro-land-mayhem.ttf", 25)
        # new_score_img = font.render(f'{str("TEXTTEXTTEXTTEXT")}', True, (255, 255, 255))
        a = back_for_dye2
        screen.blit(a, (0, 0))
        screen.blit(backi, (0, 0))
        screen.blit(text_lose, (240, 200))
        start_menu.draw()
        # mx, my = pygame.mouse.get_pos()
        # emit_particle(mx, my, 12, random.uniform(-12, 12), random.uniform(-12, 12))
        #  update_particle()
        # screen.blit(new_score_img, (230, 500))
        pygame.display.flip()


def skins_menu():
    def go_to_menu():
        checker.skins = False
        switch(menu)

    def skin_1():
        skins.changed = True
        skins.first = True
        skins.second = False
        skins.third = False

    def skin_2():
        skins.changed = True
        skins.first = False
        skins.second = True
        skins.third = False

    def skin_3():
        skins.changed = True
        skins.first = False
        skins.second = False
        skins.third = True

    start_menu = Menu(screen)
    start_menu.add_item(MenuItem('ВЕРНУТЬСЯ В МЕНЮ', go_to_menu, (start_menu.cur_x - 280, 100)))
    start_menu.add_item(MenuItem('скин 1', skin_1, (start_menu.cur_x - 450, 400)))
    start_menu.add_item(MenuItem('скин 2', skin_2, (start_menu.cur_x - 450, 700)))
    start_menu.add_item(MenuItem('скин 3', skin_3, (start_menu.cur_x - 450, 1000)))
    runing = True
    while runing:
        if not checker.skins:
            checker.skins = True
            runing = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
                switch(None)
            elif event.type == pygame.MOUSEMOTION:
                start_menu.update(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_menu.check_click(event.pos)

        screen.fill((100, 100, 100))
        start_menu.draw()
        pygame.display.flip()


def run():
    try:
        file = open('save.json')
        score = (json.load(file))
    except:
        score = 0

    try:
        file = open('money.json')
        money = (json.load(file))
    except:
        money = 0

    score_panel = Score_panel(screen, score, money)
    player_ship = Player_Ship(screen)
    gun = Gun(screen, player_ship)

    blow = Blow(screen)

    def go_to_menu():
        if score_panel.new_score > score_panel.record:
            score_panel.record = score_panel.new_score
        with open('save.json', 'w') as file:
            json.dump(score_panel.record, file)
        with open('money.json', 'w') as file:
            json.dump(score_panel.balance, file)
        switch(menu)
        checker.run = False

    start_menu = Menu(screen)
    start_menu.game = True
    '''КНОПКИ'''
    start_menu.add_item(MenuItem('←', go_to_menu, (5, 5)))
    '''КНОПКИ'''

    hit = False
    broke = False
    runing = True
    speedup = Speedup()
    while runing:
        if not checker.run:
            submarine.death()
            can.death()
            enemy.death()
            island.y = -500
            runing = False
            checker.run = True

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

        if player_ship.changed == False:
            if skins.changed:
                if skins.first:
                    player_ship.skin1 = True
                    player_ship.changed = True
                elif skins.second:
                    player_ship.skin2 = True
                    player_ship.changed = True
                elif skins.third:
                    player_ship.skin3 = True
                    player_ship.changed = True

        if (score_panel.new_score > 3) and (score_panel.new_score % 50 == 0):
            if not speedup.check:
                enemy.speed += 0.3
                submarine.speed += 0.3
                can.speed += 0.3
                island.speed += 0.3
                sub_gun.speed += 0.3
                enemy_gun.speed += 0.3
                score_panel.update_money('score')
                speedup.check = True
        if (score_panel.new_score > 0) and (score_panel.new_score % 50 != 0):
            speedup.check = False
        '''КОРАБЛЬ ВРАГ'''
        if pygame.sprite.spritecollideany(enemy, bullets):
            enemy.death()
            score_panel.update()
        if pygame.Rect.colliderect(player_ship.hitbox, enemy.hitbox):
            enemy.death()
            score_panel.update()
            # player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
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
                enemy_gun.death(enemy)
                sub_gun.death(submarine)
                hit = False
                runing = False

        if pygame.Rect.colliderect(player_ship.hitbox, enemy_gun.rect):
            # player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            enemy_gun.shot(enemy)
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                with open('money.json', 'w') as file:
                    json.dump(score_panel.balance, file)
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                enemy_gun.death(enemy)
                sub_gun.death(submarine)
                hit = False
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
            # player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                with open('money.json', 'w') as file:
                    json.dump(score_panel.balance, file)
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                enemy_gun.death(enemy)
                sub_gun.death(submarine)
                hit = False
                runing = False

        if pygame.Rect.colliderect(player_ship.hitbox, sub_gun.rect):
            #  player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            sub_gun.shot(submarine)
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                with open('money.json', 'w') as file:
                    json.dump(score_panel.balance, file)
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                enemy_gun.death(enemy)
                sub_gun.death(submarine)
                hit = False
                runing = False

        '''БОЧКА'''
        if pygame.sprite.spritecollideany(can, bullets):
            if not broke:
                can.change = True
                broke = True
                can.broke = True
                can.blow = True
                img = choice([1, 1, 2, 2, 3])
                if img == 1:
                    can.broke_heart = False
                    can.broke_rocket = True
                    can.broke_money = False
                # can.blow = False
                #    can.image = pygame.image.load("imgs/heart.svg")
                if img == 2:
                    can.broke_rocket = False
                    can.broke_heart = True
                    can.broke_money = False
                if img == 3:
                    can.broke_heart = False
                    can.broke_rocket = False
                    can.broke_money = True
                    can.image = pygame.image.load('work_images/money.png')
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
                if img == 2:
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
                        with open('money.json', 'w') as file:
                            json.dump(score_panel.balance, file)
                        submarine.death()
                        can.death()
                        enemy.death()
                        island.y = -500
                        switch(deadi)
                        enemy_gun.death(enemy)
                        sub_gun.death(submarine)
                        hit = False
                        runing = False
                if img == 3:
                    score_panel.update_money('can')

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
            #  player_ship.image = pygame.image.load('work_images/health_pl.png')  # ТУТ МЕНЯТЬ АНИМАЦИЮ
            if not hit:
                hit = True
                player_ship.speed = 0.5
            else:
                if score_panel.new_score > score_panel.record:
                    score_panel.record = score_panel.new_score
                with open('save.json', 'w') as file:
                    json.dump(score_panel.record, file)
                with open('money.json', 'w') as file:
                    json.dump(score_panel.balance, file)
                submarine.death()
                can.death()
                enemy.death()
                island.y = -500
                switch(deadi)
                enemy_gun.death(enemy)
                sub_gun.death(submarine)
                hit = False
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
