import pygame

from constants import *

class Ennemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/bat.png')
        self.image = pygame.transform.scale(self.image, (ENNEMY_WIDTH, ENNEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - ENNEMY_HEIGHT - 20
        self.rect.y = FLOOR - 100

    def move(self):
        self.rect.x -= 3