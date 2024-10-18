import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, health=50):
        super().__init__()
        self.image = pygame.image.load('human_enemy.png')  # Placeholder for enemy image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3
        self.health = health

    def update(self):
        self.rect.x -= self.speed  # Move toward the left (player direction)
        if self.rect.x < 0:
            self.rect.x = 800  # Respawn at the right edge if it goes off screen

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()  # Remove enemy from screen
