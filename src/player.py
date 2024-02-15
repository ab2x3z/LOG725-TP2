import pygame
import time

from src.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/tank.png')

        self.imageR = self.image
        self.imageL = pygame.transform.rotate(self.image, 180)
        self.imageU = pygame.transform.rotate(self.image, 90)
        self.imageD = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.speed = 6

        self.direction = (1, 0)
        self.bullets = pygame.sprite.Group()
        self.redBulletUsed = False
        self.greenBulletUsed = False
        self.blueBulletUsed = False
        self.color = (255, 0, 0)
        self.lastInputTime = time.time()

    def update(self):
        self.bullets.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.image = self.imageL
            self.direction = (-1, 0)
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.image = self.imageR
            self.direction = (1, 0)
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.image = self.imageU
            self.direction = (0, -1)
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.image = self.imageD
            self.direction = (0, 1)
        
        if keys[pygame.K_SPACE]:
            if time.time() - self.lastInputTime >= 0.6:
                self.shoot()
                self.lastInputTime = time.time()

        if keys[pygame.K_q]:
            if time.time() - self.lastInputTime >= 0.2:
                self.changeColor()
                self.lastInputTime = time.time()

    def changeColor(self):
        if self.color == (255, 0, 0):
            self.color = (0, 255, 0)
        elif self.color == (0, 255, 0):
            self.color = (0, 0, 255)
        elif self.color == (0, 0, 255):
            self.color = (255, 0, 0)
        
    def shoot(self):
        if self.color == (255, 0, 0) and not self.redBulletUsed:
            bullet = Bullet(self.rect.center, self.direction, self.color)
            self.bullets.add(bullet)
            self.redBulletUsed = True

        elif self.color == (0, 255, 0) and not self.greenBulletUsed:
            bullet = Bullet(self.rect.center, self.direction, self.color)
            self.bullets.add(bullet)
            self.greenBulletUsed = True

        elif self.color == (0, 0, 255) and not self.blueBulletUsed:
            bullet = Bullet(self.rect.center, self.direction, self.color)
            self.bullets.add(bullet)
            self.blueBulletUsed = True

        pygame.mixer.Sound('./assets/shoot.wav').play()
