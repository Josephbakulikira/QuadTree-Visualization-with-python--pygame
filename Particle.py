import pygame
from math import sqrt
from pygame.math import Vector2
from random import uniform
from range import *

class Particle:
    def __init__(self, position = Vector2(0, 0), radius=6, color=(255, 255, 255)):
        self.position = position
        self.color = color
        self.radius = radius
        self.highlighted = False
        self.HighlightColor = None

    def move(self):
        self.position.x += uniform(-2, 2)
        self.position.y += uniform(-2, 2)

    def collide(self, other):
        dist = GetDistance(self.position.x, self.position.y, other.position.x, other.position.y)
        if dist < self.radius + other.radius:
            return True
        else:
            return False

    def Highlight(self, color=(0, 255, 255)):
        self.highlighted = True
        self.highlightColor = color

    def draw(self, screen, radius=None):
        _radius = self.radius
        if radius != None:
            _radius = radius

        surface = pygame.Surface((_radius*2, _radius*2), pygame.SRCALPHA, 32)
        r,g, b = self.color
        if self.highlighted == True:
            r, g, b = self.highlightColor
        pygame.draw.circle(surface, (r, g, b, 100), (int(_radius), int(_radius)), _radius)
        pygame.draw.circle(surface, (r, g, b, 255), (int(_radius), int(_radius)), _radius, 1)
        # pygame.draw.circle(screen, (0, 255, 0), self.position, 3)

        screen.blit(surface, ( int(self.position.x) - _radius, int(self.position.y) - _radius))
        # pygame.draw.circle(screen, self.color, self.position, self.radius)
        self.highlighted = False
def GetDistance(x1, y1, x2, y2):
    return sqrt( (x2 - x1) * (x2-x1) + (y2 - y1) * (y2 - y1) )
