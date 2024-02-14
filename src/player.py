import pygame
from src.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.speed = 6

        #######################
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.bullets.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def shoot(self):
        bullet = Bullet(self.rect.center, (0, -1))  # Shoot upwards
        self.bullets.add(bullet)
