import pygame


class Score_panel():
    def __init__(self, screen, score, money, purchase, num, bought, last_skin):
        self.screen = screen
        self.font = pygame.font.Font("imgs/retro-land-mayhem.ttf", 100)
        self.font1 = pygame.font.Font("imgs/retro-land-mayhem.ttf", 30)
        self.font2 = pygame.font.Font("imgs/retro-land-mayhem.ttf", 40)
        self.font3 = pygame.font.Font(None, 30)
        self.record = score
        self.balance = money
        self.img = pygame.image.load("imgs/score.svg").convert_alpha()
        '''картинка монеты'''
        self.monet = pygame.image.load('work_images/money.png').convert_alpha()
        '''картинка монеты'''
        self.img_menu = pygame.transform.scale(self.img, (65, 65))
        self.image = pygame.transform.scale(self.img, (50, 50))
        self.new_score = 48
        self.record_img = self.font1.render(f'{str(self.record)}', True, (255, 255, 255))
        self.record_img2 = self.font2.render(f'{str(self.record)}', True, (255, 255, 255))
        self.new_score_img = self.font.render(f'{str(self.new_score)}', True, (255, 255, 255))
        self.balance_img = self.font1.render(f'{str(self.balance)}', True, (255, 255, 255))
        self.menu = False

        if purchase == 2:
            self.status1 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status2 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status3 = self.font3.render('Не куплено: цена - 100', True, (255, 255, 255))
        elif purchase == 3:
            self.status1 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status2 = self.font3.render('Не куплено: цена - 75', True, (255, 255, 255))
            self.status3 = self.font3.render('Доступно', True, (255, 255, 255))
        elif purchase == 5:
            self.status1 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status2 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status3 = self.font3.render('Доступно', True, (255, 255, 255))
        else:
            self.status1 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status2 = self.font3.render('Не куплено: цена - 75', True, (255, 255, 255))
            self.status3 = self.font3.render('Не куплено: цена - 100', True, (255, 255, 255))

        self.no_money1 = self.font3.render('Не хватает денег', True, (255, 0, 0))
        self.no_money2 = self.font3.render('Не хватает денег', True, (255, 0, 0))

        if bought == 0:
            if (num > 75) and (num < 100):
                self.no_money1 = self.font3.render('', True, (255, 255, 255))
                self.no_money2 = self.font3.render('Не хватает денег', True, (255, 0, 0))
            if num >= 100:
                self.no_money1 = self.font3.render('', True, (255, 255, 255))
                self.no_money2 = self.font3.render('', True, (255, 255, 255))
        if bought == 2:
            self.no_money1 = self.font3.render('', True, (255, 255, 255))
            self.no_money2 = self.font3.render('', True, (255, 255, 255))
            if num < 100:
                self.no_money2 = self.font3.render('Не хватает денег', True, (255, 0, 0))
        if bought == 3:
            self.no_money1 = self.font3.render('', True, (255, 0, 0))
            if num < 75:
                self.no_money1 = self.font3.render('Не хватает денег', True, (255, 0, 0))
            self.no_money2 = self.font3.render('', True, (255, 255, 255))
        if bought >= 5:
            self.no_money1 = self.font3.render('', True, (255, 255, 255))
            self.no_money2 = self.font3.render('', True, (255, 255, 255))

        if last_skin == 2:
            self.chosen1 = self.font3.render('', True, (0, 255, 0))
            self.chosen2 = self.font3.render('Скин выбран', True, (0, 255, 0))
            self.chosen3 = self.font3.render('', True, (0, 255, 0))
        if last_skin == 3:
            self.chosen1 = self.font3.render('', True, (0, 255, 0))
            self.chosen2 = self.font3.render('', True, (0, 255, 0))
            self.chosen3 = self.font3.render('Скин выбран', True, (0, 255, 0))
        else:
            self.chosen1 = self.font3.render('Скин выбран', True, (0, 255, 0))
            self.chosen2 = self.font3.render('', True, (0, 255, 0))
            self.chosen3 = self.font3.render('', True, (0, 255, 0))

    def update(self):
        self.new_score += 1
        self.new_score_img = self.font.render(f'{str(self.new_score)}', True, (255, 255, 255))
        if self.new_score > self.record:
            self.record_img = self.font1.render(f'{str(self.new_score)}', True, (255, 255, 255))

    def update_money(self, type):
        if type == 'score':
            self.balance += 10
        elif type == 'can':
            self.balance += 5
        elif type == 'buy1':
            self.balance -= 75
        elif type == 'buy2':
            self.balance -= 100
        self.balance_img = self.font1.render(f'{str(self.balance)}', True, (255, 255, 255))

    def update_status(self, purchase):
        if purchase == 2:
            self.status1 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status2 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status3 = self.font3.render('Не куплено: цена - 100', True, (255, 255, 255))
        if purchase == 3:
            self.status1 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status2 = self.font3.render('Не куплено: цена - 75', True, (255, 255, 255))
            self.status3 = self.font3.render('Доступно', True, (255, 255, 255))
        if purchase >= 5:
            self.status1 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status2 = self.font3.render('Доступно', True, (255, 255, 255))
            self.status3 = self.font3.render('Доступно', True, (255, 255, 255))

    def update_no_money(self, num, bought):
        if bought == 0:
            if (num > 75) and (num < 100):
                self.no_money1 = self.font3.render('', True, (255, 255, 255))
            if num >= 100:
                self.no_money1 = self.font3.render('', True, (255, 255, 255))
                self.no_money2 = self.font3.render('', True, (255, 255, 255))
        if bought == 2:
            self.no_money1 = self.font3.render('', True, (255, 255, 255))
            if num < 100:
                self.no_money2 = self.font3.render('Не хватает денег', True, (255, 0, 0))
        if bought == 3:
            self.no_money2 = self.font3.render('', True, (255, 255, 255))
            if num < 75:
                self.no_money1 = self.font3.render('Не хватает денег', True, (255, 0, 0))
        if bought >= 5:
            self.no_money1 = self.font3.render('', True, (255, 255, 255))
            self.no_money2 = self.font3.render('', True, (255, 255, 255))

    def update_choose(self, skin_num):
        if skin_num == 2:
            self.chosen1 = self.font3.render('', True, (0, 255, 0))
            self.chosen2 = self.font3.render('Скин выбран', True, (0, 255, 0))
            self.chosen3 = self.font3.render('', True, (0, 255, 0))
        elif skin_num == 3:
            self.chosen1 = self.font3.render('', True, (0, 255, 0))
            self.chosen2 = self.font3.render('', True, (0, 255, 0))
            self.chosen3 = self.font3.render('Скин выбран', True, (0, 255, 0))
        else:
            self.chosen1 = self.font3.render('Скин выбран', True, (0, 255, 0))
            self.chosen2 = self.font3.render('', True, (0, 255, 0))
            self.chosen3 = self.font3.render('', True, (0, 255, 0))

    def zeroing(self):
        self.record = 0
        self.new_score = 0
        self.new_score_img = self.font.render(f'{str(self.new_score)}', True, (255, 255, 255))
        self.record_img = self.font1.render(f'{str(self.record)}', True, (255, 255, 255))
        self.record_img2 = self.font2.render(f'{str(self.record)}', True, (255, 255, 255))

    def draw_score(self):
        self.screen.blit(self.record_img, (self.screen.get_rect().width - self.record_img.get_rect().width - 10, 10))
        self.screen.blit(self.new_score_img, (
            (self.screen.get_rect().width // 2) - (self.new_score_img.get_width() // 2),
            20))
        self.screen.blit(self.image, (
            self.screen.get_rect().width - self.image.get_rect().width - 20 - self.record_img.get_width(), 10))

    def draw_record(self):
        if self.menu:
            # self.screen.blit(self.record_img2, (440,300))
            self.screen.blit(self.record_img2,
                             ((self.screen.get_rect().width // 2) - self.record_img.get_rect().width - 20, 305))
            self.screen.blit(self.img_menu,
                             ((self.screen.get_rect().width // 2) + (self.record_img.get_rect().width // 2) - 25, 300))

        else:
            self.screen.blit(self.record_img,
                             (self.screen.get_rect().width - self.record_img.get_rect().width - 10, 10))
            # self.screen.blit(self.image, (self.screen.get_rect().width - self.image.get_rect().width - 60, 10))
            self.screen.blit(self.image, ((self.screen.get_rect().width // 2) - self.image.get_rect().width - 60, 10))

    def draw_balance(self):
        self.screen.blit(self.monet, (5, 5))
        self.screen.blit(self.balance_img, (self.screen.get_rect().width - 900, 10))

    def draw_status(self):
        self.screen.blit(self.status1, (30, 300))
        self.screen.blit(self.status2, (30, 600))
        self.screen.blit(self.status3, (30, 900))

    def draw_no_money(self):
        self.screen.blit(self.no_money1, (30, 620))
        self.screen.blit(self.no_money2, (30, 920))

    def draw_choice(self):
        self.screen.blit(self.chosen1, (30, 320))
        self.screen.blit(self.chosen2, (30, 640))
        self.screen.blit(self.chosen3, (30, 940))
