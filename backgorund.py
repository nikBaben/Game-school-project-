from styles import back


class Back():
    def __init__(self, screen, freq):
        self.screen = screen
        self.image = back.convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        if freq == 60:
            self.speed = 1.6
        if freq == 144:
            self.speed = 1
        else:
            self.speed = 1.4
        self.y = -1050

    def scroling(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.top == 50:
            self.y = -1050

    def output_back(self):
        self.screen.blit(self.image, self.rect)
