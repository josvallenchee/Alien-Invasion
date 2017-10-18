import pygame

class Ship():
    def __init__(self, screen, setting):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.setting = setting

        self.imageBig = pygame.image.load_basic("6849573677864.jpg")
        self.image = pygame.transform.scale(self.imageBig,(80,80))

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.setting.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -=self.setting.ship_speed

        self.rect.centerx = self.center

    def center_ship(self):
        self.centerx = self.screen_rect.centerx