import pygame


class Score_panel():
    def __init__(self, screen, score):
        self.screen = screen
        self.font = pygame.font.Font("imgs/supermario286rusbylyajka.otf", 100)
        self.font1 = pygame.font.Font("imgs/supermario286rusbylyajka.otf", 30)
        self.record = score
        self.img = pygame.image.load("imgs/score.svg").convert_alpha()
        self.image = pygame.transform.scale(self.img, (50, 50))
        self.new_score = 0
        self.record_img = self.font1.render(f'{str(self.record)}', True, (81, 179, 199))
        self.new_score_img = self.font.render(f'{str(self.new_score)}', True, (81, 179, 199))

    def update(self):
        self.new_score += 1
        self.new_score_img = self.font.render(f'{str(self.new_score)}', True, (81, 179, 199))

    def draw_score(self):
        self.screen.blit(self.record_img, (self.screen.get_rect().width - self.record_img.get_rect().width - 10, 10))
        self.screen.blit(self.new_score_img, (470,
                                              0))  # (((self.screen.get_rect().width)/2 )+self.new_score_img.get_rect().width -60, 525))#(450,480)) #(self.screen.get_rect().width - self.new_score_img.get_rect().width - 10, 30))
        self.screen.blit(self.image, (self.screen.get_rect().width - self.image.get_rect().width - 60, 10))
