import pygame
from Particle import GetDistance

class Rectangle:
    def __init__(self, position, scale):
        self.position = position
        self.scale = scale
        self.color = (255, 255, 255)
        self.lineThickness = 1

    def containsParticle(self, particle):
        x, y = particle.position
        bx, by = self.position
        w, h = self.scale
        if x >= bx and x <= bx+w and y >= by and y <= by+h:
            return True
        else:
            return False

    def intersects(self,_range):
        x, y = self.position
        w, h = self.scale
        xr, yr = _range.position
        wr, hr = _range.scale
        if xr > x + w or xr+wr < x-w or yr > y + h or yr+hr < y-h:
            return True
        else:
            return False

    def Draw(self, screen):
        x, y = self.position
        w, h = self.scale
        pygame.draw.rect(screen, self.color, [x, y, w, h], self.lineThickness)
