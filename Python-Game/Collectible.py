import pygame
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, type_of_collectible):
        super().__init__()
        self.type = type_of_collectible
        if self.type == 'health':
            self.image = pygame.image.load('health_pack.png')
        elif self.type == 'extra_life':
            self.image = pygame.image.load('extra_life.png')
        self.rect = self.image.get_rect(topleft=(x, y))

    def apply(self, player):
        if self.type == 'health':
            player.health = min(player.health + 25, 100)  # Heal player by 25
        elif self.type == 'extra_life':
            player.lives += 1  # Add an extra life
        self.kill()  # Remove collectible after use
