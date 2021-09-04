import pygame

from random import randint
from Quadtree import *
from Particle import Particle
from pygame.math import Vector2
from range import *

Width, Height = 1000, 1000
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Quadtree")
clock = pygame.time.Clock()
fps = 60

Background = (0, 0, 0)
RADIUS = 10
particles = []

NODE_CAPACITY = 2

for i in range(150):
    offset = 50
    x = randint(offset, Width-offset)
    y = randint(offset, Height-offset)
    # col = (randint(0, 255), randint(0, 255),randint(0, 255))
    col = (255, 255, 255)
    particle = Particle(Vector2(x, y), RADIUS, col)
    particles.append(particle)


# print(points)
moveParticle = True
particleCollision = True
run = True
while run:
    screen.fill(Background)
    pygame.display.set_caption("QuadTree Fps: " + str(int(clock.get_fps())))
    clock.tick(fps)

    boundary = Rectangle(Vector2(0, 0), Vector2(Width, Height))
    quadtree = QuadTree(NODE_CAPACITY, boundary)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_e:
                moveParticle = not moveParticle
                particleCollision = moveParticle
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            particle = Particle(Vector2(x, y), RADIUS, (255, 255, 255))
            particles.append(particle)
            quadtree.insert(particle)


    for particle in particles:
        if moveParticle:
            particle.move()
        quadtree.insert(particle)
        particle.draw(screen)

    for particle in particles:
        xx, yy = particle.position
        r = RADIUS * 3
        rangeRect = Rectangle(Vector2(xx - r/2, yy - r/2), Vector2(r, r))
        rangeRect.color = (190, 210, 55)
        rangeRect.lineThickness = 3
        others = quadtree.queryRange(rangeRect)
        for other in others:
            if particle != other:
                if particle.collide(other) == True:
                    particle.Highlight((255, 42, 53))


    quadtree.Show(screen)
    

    pygame.display.flip()

pygame.quit()
