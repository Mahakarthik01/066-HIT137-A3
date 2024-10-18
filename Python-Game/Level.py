import pygame

class Level:
    def __init__(self, background_image, enemies, collectibles, is_boss=False):
        self.background = pygame.image.load(background_image)
        self.enemies = pygame.sprite.Group(enemies)
        self.collectibles = pygame.sprite.Group(collectibles)
        self.is_boss = is_boss

    def update(self):
        self.enemies.update()
        self.collectibles.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.enemies.draw(screen)
        self.collectibles.draw(screen)
