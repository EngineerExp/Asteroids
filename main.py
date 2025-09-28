import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # make group containers for objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # put the class objects in the containers so they can be acted upon with methods
    # without calling the individual instances but using the groups
    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField() # make sure to make objects after containers are made

    Player.containers = (updateable,drawable) #container
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2) #object

    Shot.containers = (shots,updateable,drawable)
    

    dt = 0

    while True:
        # checks if the close button in the pygame console has closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
