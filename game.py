import pygame
from constants import *
from player import Player
from ennemy import Ennemy

class Game:

    # au chargement du jeu
    def __init__(self): 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Graven Bros")

        # Importer l'image d'arriere plan
        self.background_image = pygame.image.load('assets/images/background.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # import le joueur
        self.player = Player()

        self.ennemy_group = pygame.sprite.Group()
        self.ennemy_group.add(Ennemy())

    
    def keyboard(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player.move_up()

        elif keys[pygame.K_DOWN]:
            self.player.move_down()

        if keys[pygame.K_RIGHT]:
            self.player.move_right()

        if keys[pygame.K_LEFT]:
            self.player.move_left()

    def check_collisions(self):
        if pygame.sprite.groupcollide(self.player.all_projectiles, self.ennemy_group, True, True):
            print("un ennemie a été touché !")

            self.ennemy_group.add(Ennemy())

        if pygame.sprite.spritecollide(self.player, self.ennemy_group, True):
            print("game over")

    def run(self):
        # boucle du jeu pour maintenir la fenetre allumé
        game = True
        clock = pygame.time.Clock()
        while game:

            self.keyboard()
            self.check_collisions()

            for ennemy in self.ennemy_group:
                ennemy.move()

            for projectile in self.player.all_projectiles:
                projectile.move()
        
            self.screen.blit(self.background_image, (0, 0))  # interface du jeu
            self.ennemy_group.draw(self.screen)
            self.player.all_projectiles.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)
           
            
            pygame.display.flip() # actualiser l'ecran

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.launch_projectile()
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()

            clock.tick(60)