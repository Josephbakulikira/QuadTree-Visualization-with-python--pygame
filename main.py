import pygame

from random import randint
from Quadtree import *
from Particle import Particle
from pygame.math import Vector2

Width, Height = 1000, 1000
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Quadtree")
clock = pygame.time.Clock()
fps = 60

Background = (0, 0, 0)
particles = []

NODE_CAPACITY = 1

rangeRect = Rectangle(Vector2(250, 250), Vector2(300, 300))
rangeRect.color = (190, 210, 55)
rangeRect.lineThickness = 3

boundary = Rectangle(Vector2(0, 0), Vector2(Width, Height))

quadtree = QuadTree(NODE_CAPACITY, boundary)

# for i in range(500):
#     offset = 50
#     x = randint(offset, Width-offset)
#     y = randint(offset, Height-offset)
#     # col = (randint(0, 255), randint(0, 255),randint(0, 255))
#     col = (255, 255, 255)
#     particle = Particle(Vector2(x, y), 6, col)
#     quadtree.insert(particle)
#     particles.append(particle)


# print(points)
showRange = False
run = True
while run:
    screen.fill(Background)
    pygame.display.set_caption("QuadTree Fps: " + str(int(clock.get_fps())))
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                showRange = not showRange
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            particle = Particle(Vector2(x, y), 6, (255, 255, 255))
            particles.append(particle)
            quadtree.insert(particle)


    quadtree.Show(screen)
    for particle in particles:
        particle.draw(screen)

    rangeRect.position.x, rangeRect.position.y = pygame.mouse.get_pos()
    points = quadtree.queryRange(rangeRect)
    if showRange == True:
        for point in points:
            point.draw(screen, (245, 80, 225), 10)
        rangeRect.Draw(screen)
    pygame.display.flip()

pygame.quit()
