import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, direction):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = 10
        self.direction = direction

    def update(self):
        self.rect.move_ip(self.speed * self.direction[0], self.speed * self.direction[1])