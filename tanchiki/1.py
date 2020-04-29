import pygame
import random
from enum import Enum
#pylint:disable=no-member

pygame.init()
screen = pygame.display.set_mode((820,620))

firing = pygame.mixer.Sound('pew.wav')
popadanie = pygame.mixer.Sound('popadanie.wav')

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tank:

    def __init__(self,name, v, u, x, y, speed, color, lives, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN):
        self.u = u
        self.v = v
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 40
        self.direction = Direction.RIGHT
        self.lives = 3
        self.name = name
        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

    def draw(self):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT: pygame.draw.line(screen, self.color, tank_c, (self.x + self.width + int(self.width / 2), self.y + int(self.width / 2)), 4)
        if self.direction == Direction.LEFT: pygame.draw.line(screen, self.color, tank_c, (self.x - int(self.width / 2), self.y + int(self.width / 2)), 4)
        if self.direction == Direction.UP: pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 4)
        if self.direction == Direction.DOWN: pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)), 4)

    def change_direction(self, direction):
        self.direction = direction

    def move(self): #800 600
        if self.direction == Direction.LEFT:
            if self.x + self.width < 0: self.x = 800
            else: self.x -= self.speed
        if self.direction == Direction.RIGHT:
            if self.x > 800: self.x = 0
            else: self.x += self.speed
        if self.direction == Direction.UP:
            if self.y + self.width < 0: self.y = 600
            else: self.y -= self.speed
        if self.direction == Direction.DOWN:
            if self.y > 600: self.y = 0 - self.width
            else: self.y += self.speed
        self.draw()

    def chances(self):
        font = pygame.font.SysFont("monaco", 30)
        score = font.render(str(self.name) + " lives: " + str(self.lives), True, (self.color))
        screen.blit(score, (self.v, self.u))

    def dead(self):
        font = pygame.font.SysFont("monaco", 60)
        text = font.render(str(self.name) + ' died', True, (143, 188, 143)) 
        screen.blit(text, (250, 200))

class Bullet:

    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.radius = 5
        self.speedx = sx
        self.speedy = sy

    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)
    
    def move(self):
        
        self.x += self.speedx
        self.y += self.speedy

        self.draw()

mainloop = True
tank1 = Tank('Player 1', 600, 15, 300, 300, 2, (255, 182, 193), 3) #pink 
tank2 = Tank('Player 2', 50, 15, 100, 100, 2, (136, 122, 183), 3, pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s) #purple

FPS = 120
clock = pygame.time.Clock()

tanks = [tank1, tank2]
bullets = []

while mainloop:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])

            if event.key == pygame.K_RETURN:
                firing.play()
                if tank1.direction == Direction.LEFT:
                    bullet = Bullet(tank1.x - 20, tank1.y + 20, -10, 0)
                if tank1.direction == Direction.RIGHT:
                    bullet = Bullet(tank1.x + 60, tank1.y + 20, 10, 0)
                if tank1.direction == Direction.UP:
                    bullet = Bullet(tank1.x + 20, tank1.y - 20, 0, -10)
                if tank1.direction == Direction.DOWN:
                    bullet = Bullet(tank1.x + 20, tank1.y + 60, 0, 10)
                bullets.append(bullet)

            if event.key == pygame.K_SPACE:
                firing.play()
                if tank2.direction == Direction.LEFT:
                    bullet = Bullet(tank2.x - 20, tank2.y + 20, -10, 0)
                if tank2.direction == Direction.RIGHT:
                    bullet = Bullet(tank2.x + 60, tank2.y + 20, 10, 0)
                if tank2.direction == Direction.UP:
                    bullet = Bullet(tank2.x + 20, tank2.y - 20, 0, -10)
                if tank2.direction == Direction.DOWN:
                    bullet = Bullet(tank2.x + 20, tank2.y + 60, 0, 10)
                bullets.append(bullet)
    
    for b in bullets:
        if b.x < 0 or b.x > 800 or b.y < 0 or b.y > 600:
            bullets.pop(0)
    
        if b.x in range(tank2.x, tank2.x + 40) and b.y in range(tank2.y, tank2.y + 40):
            popadanie.play()
            bullets.pop(0)
            tank2.lives -= 1
        if b.x in range(tank1.x, tank1.x + 40) and b.y in range(tank1.y, tank1.y + 40):
            popadanie.play()
            bullets.pop(0)
            tank1.lives -= 1           
    
    screen.fill((255, 255, 255))
    
    for tank in tanks:
        tank.move()
        tank.chances()
        if tank.lives < 3:
            key = pygame.key.get_pressed()
            if key[pygame.K_1]:
                tank.lives = 3
        if tank.lives == 0:
            tank.dead()
            key = pygame.key.get_pressed()
    for bullet in bullets:
        bullet.move()

    pygame.display.flip()

pygame.quit()