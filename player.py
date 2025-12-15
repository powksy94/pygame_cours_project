import pygame
from constants import *
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png")
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect.x = 69
        self.rect.y = FLOOR

        self.speed = 3

        # saut
        self.vy = 0
        self.gravity = 0.6
        self.is_jump = False

        self.all_projectiles = pygame.sprite.Group()
    
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self.rect.x))

      

    def move_right(self):
        if self.rect.x + self.speed < SCREEN_WIDTH:
            self.rect.x += self.speed

    def move_left(self):
        if self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed

    def move_up(self):
        if self.rect.y - self.speed >= 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.y + self.speed <= FLOOR:
            self.rect.y += self.speed

    def jump(self):
        if not self.is_jump:
            self.is_jump = True
            self.vy = -12

    def update(self):
        if self.is_jump:
            self.rect.y += self.vy
            self.vy += self.gravity

            if self.rect.y >= FLOOR:
                self.rect.y = FLOOR
                self.is_jump = False
                self.vy = 0
