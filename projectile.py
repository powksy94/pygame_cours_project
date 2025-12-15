import pygame
import math
from constants import *

BOUNCE_Y = FLOOR - 100

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player_x, direction=1):
        super().__init__()
        
        # On garde une image d'origine non modifiée
        self.original_image = pygame.image.load('assets/images/fireball.png')
        self.original_image = pygame.transform.scale(self.original_image, (PROJECTILE_WIDTH, PROJECTILE_HEIGHT))
        self.image = self.original_image.copy()

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.bottom = FLOOR

        # Physique
        self.vx = 3 * direction
        self.vy = 0
        self.gravity = 0.75
        self.bounce_speed = 12

    def move(self):
        # --- Physique ---
        self.rect.x += self.vx
        self.vy += self.gravity
        self.rect.y += self.vy

        # --- Rebond ---
        if self.rect.bottom >= FLOOR:
            self.rect.bottom = FLOOR
            self.vy = -self.bounce_speed

        # --- Calcul de l'angle ---
        angle = math.degrees(math.atan2(-self.vy, self.vx))

        # --- Rotation à partir de l'image ORIGINALE ---
        self.image = pygame.transform.rotate(self.original_image, angle)

        # Garder le centre malgré la rotation
        self.rect = self.image.get_rect(center=self.rect.center)
