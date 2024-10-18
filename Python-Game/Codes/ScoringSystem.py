import pygame


class Score:
    def __init__(self, font_size=36, color=(255, 255, 255), initial_score=0):
        self.font = pygame.font.SysFont(None, font_size)  # Initialize font for score display
        self.color = color
        self.score = initial_score  # Start with an initial score

    def increase(self, points):
        """Increase the score by a certain number of points."""
        self.score += points

    def reset(self):
        """Reset the score to zero."""
        self.score = 0

    def draw(self, screen, x=10, y=10):
        """Draw the current score on the screen."""
        score_text = self.font.render(f'Score: {self.score}', True, self.color)
        screen.blit(score_text, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Initialize the score system
    score_system = Score()

    # Load player, enemies, collectibles, etc.
    player = player()

    running = True
    while running:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move(keys_pressed)
        player.update()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw player, enemies, collectibles, etc.
        screen.blit(player.image, player.rect)

        # Increase score on defeating enemies or collecting items (example):
        # If player defeats an enemy
        # score_system.increase(100)

        # If player collects an item
        # score_system.increase(50)

        # Draw the score on the screen
        score_system.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
