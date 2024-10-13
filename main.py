import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

black = (0, 0, 0)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)
Shoot.containers = (updatable, drawable, shots)

def main():
    pygame.init()
    pygame.display.set_mode()
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()


    dt = 0

    

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(black, rect=None, special_flags=0)
        
        for _ in updatable:
            _.update(dt)

        for asteroid in asteroids:

            if player.collision_check(asteroid) == True:
                print("Game Over!")
                pygame.quit()
                exit()

            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    shot.kill()
                    asteroid.split()

        for _ in drawable:        
            _.draw(screen)


        pygame.display.flip()
        
        #clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

