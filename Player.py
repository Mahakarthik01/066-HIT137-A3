import pygame
from Projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('wolf.png')

        self.rect = self.image.get_rect()
        self.rect.x = 100  # Starting X position
        self.rect.y = 300  # Starting Y position
        self.speed = 5
        self.jump_speed = -10
        self.gravity = 0.5
        self.velocity_y = 0
        self.is_jumping = False
        self.health = 100
        self.lives = 3
        self.score = 0

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = self.jump_speed

    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        if self.rect.y >= 300:  # Land back on the ground
            self.rect.y = 300
            self.is_jumping = False

    def shoot(self):
        return Projectile(self.rect.centerx, self.rect.centery)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.lives -= 1
            self.health = 100  # Reset health
