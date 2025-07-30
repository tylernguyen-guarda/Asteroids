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
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # Create group to manage objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # assign player object to both groups
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # calculate time difference between frames
        tick_time = clock.tick(60)
        print(tick_time)
        dt = tick_time / 1000

        # update game state
        player.update(dt)

        # clear screen
        screen.fill("black")

        # draw everything to screen
        player.draw(screen)

        # display frame
        pygame.display.flip()


if __name__ == "__main__":
    main()
