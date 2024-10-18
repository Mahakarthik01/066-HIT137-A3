import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bone.png')  # Placeholder image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 8

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 800:  # If the projectile goes off the screen
            self.kill()
