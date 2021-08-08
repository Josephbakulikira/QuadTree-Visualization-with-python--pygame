import pygame
from pygame.math import Vector2

class Particle:
    def __init__(self, position = Vector2(0, 0), radius=6, color=(255, 255, 255)):
        self.position = position
        self.color = color
        self.radius = radius

    def draw(self, screen, color=(255, 255, 255), radius=None):
        _radius = self.radius
        if radius != None:
            _radius = radius
        surface = pygame.Surface((_radius*2, _radius*2), pygame.SRCALPHA, 32)
        r,g, b = color
        pygame.draw.circle(surface, (r, g, b, 100), (int(_radius), int(_radius)), _radius)
        pygame.draw.circle(surface, (r, g, b, 255), (int(_radius), int(_radius)), _radius, 1)
        # pygame.draw.circle(screen, (0, 255, 0), self.position, 3)

        screen.blit(surface, ( int(self.position.x) - _radius, int(self.position.y) - _radius))
        # pygame.draw.circle(screen, self.color, self.position, self.radius)
