import pygame
from Camera import Camera
from Level import Level
from Enemy import Enemy
from Collectible import Collectible
from Player import Player
from Projectile import Projectile
from ScoringSystem import Score



def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Load player, enemies, collectibles, etc.
    player = Player()
    camera = Camera(800, 600)

    level_1 = Level('level1_background.png', [Enemy(500, 300)], [Collectible(700, 350, 'health')])

    running = True
    while running:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move(keys_pressed)
        player.update()

        level_1.update()

        # Camera follows player
        camera.update(player)

        # Drawing everything
        screen.fill((0, 0, 0))
        level_1.draw(screen)
        screen.blit(player.image, player.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
