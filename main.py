import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
        player.draw(screen)
        pygame.display.flip()
        tick_time = clock.tick(60)
        dt = tick_time / 1000


if __name__ == "__main__":
    main()
