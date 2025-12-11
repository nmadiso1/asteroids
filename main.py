import pygame # type: ignore
from player import Player
from asteroid import Asteroid
from logger import log_state
from logger import log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroidfield import AsteroidField


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        dt = clock.tick(60)/1000



if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
