import pygame

NON_ACTIVE = (255, 255, 255)
ACTIVE = (0, 255, 255)


class MenuItem():
    def __init__(self, text, func, item_pos):
       # self.font = pygame.font.Font("imgs/retro-land-mayhem.ttf", 100)
        self.font = pygame.font.Font("imgs/tetx.ttf", 35)
        self.font1 = pygame.font.Font("imgs/tetx.ttf", 20)
       # self.font_logo = pygame.font.Font("imgs/tetx.ttf", 50)
   #     self.font = pygame.font.SysFont(None, 40, True)
        self.text = text
        self.action = func
        self.color = NON_ACTIVE
        self.text_img = self.font.render(self.text, True, self.color)
        self.text_img1 = self.font1.render(self.text, True, self.color)
     #   self.text_img_logo = self.font_logo.render(self.text, True, self.color)
        self.x, self.y = item_pos
        print(self.text_img.get_width())
        #self.game = False

    def check_hover(self, pos):
        x, y = pos
        return (self.x <= x <= self.x + self.text_img.get_width()) and (
                self.y <= y <= self.y + self.text_img.get_height())

    def draw_item(self, screen):
       # if self.game: 
          #  screen.blit(self.text_img1, (self.x, self.y))
        screen.blit(self.text_img, (self.x, self.y))


class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.items = []
        self.cur_x = self.screen.get_width() // 2
        self.cur_y = 400
      #  self.logo_y = 200
     #   self.logo_x = self.screen.get_width() // 2


    def add_item(self, menu_item):
        self.items.append(menu_item)
        self.cur_y += 60

    def update(self, pos):
        for item in self.items:
            if item.check_hover(pos):
                item.color = ACTIVE
            else:
                item.color = NON_ACTIVE
            item.text_img = item.font.render(item.text, True, item.color)
            #item.text_img1 = item.font1.render(item.text, True, item.color)
         #   item.text_img_logo =  item.font_logo.render(item.text, True, item.color)

    def check_click(self, pos):
        for item in self.items:
            if item.check_hover(pos):
                item.action()

    def draw(self):
        for item in self.items:
            item.draw_item(self.screen)
