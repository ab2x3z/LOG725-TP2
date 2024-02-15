import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.color = (0, 0, 0)
        if color == "regular":
            self.image = pygame.image.load('./assets/wall.png')
        elif color == "red":
            self.image = pygame.image.load('./assets/red.png')
            self.color = (255, 0, 0)
        elif color == "green":
            self.image = pygame.image.load('./assets/green.png')
            self.color = (0, 255, 0)
        elif color == "blue":
            self.image = pygame.image.load('./assets/blue.png')
            self.color = (0, 0, 255)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
