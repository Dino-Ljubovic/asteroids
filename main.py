# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ast_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        for entity in shots:
            entity.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player_instance):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.kill()
                    bullet.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()