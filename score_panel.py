import pygame


class Score_panel():
    def __init__(self, screen, score, money):
        self.screen = screen
        self.font = pygame.font.Font("imgs/retro-land-mayhem.ttf", 100)
        self.font1 = pygame.font.Font("imgs/retro-land-mayhem.ttf", 30)
        self.font2 = pygame.font.Font("imgs/retro-land-mayhem.ttf", 40)
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
