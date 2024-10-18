import pygame

def game_over(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, (250, 250))

    pygame.display.flip()
    pygame.time.wait(2000)