import pygame
from pygame.math import Vector2

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
        if x > bx and x < bx+w and y > by and y < by+h:
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

class QuadTree:
    def __init__(self, capacity, boundary):
        self.capacity = capacity
        self.boundary = boundary
        self.particles = []
        self.color = (255, 255, 255)
        self.northWest = None
        self.northEast = None
        self.southWest = None
        self.southEast = None
    def subdivide(self):
        parent = self.boundary
        
        boundary_nw = Rectangle(
                Vector2(
                parent.position.x ,
                parent.position.y
                ),
            parent.scale/2
            )
        boundary_ne = Rectangle(
                Vector2(
                parent.position.x + parent.scale.x/2,
                parent.position.y
                ),
                parent.scale/2
            )
        boundary_sw = Rectangle(
                Vector2(
                parent.position.x,
                parent.position.y + parent.scale.y/2
                ),
                parent.scale/2
            )
        boundary_se = Rectangle(
                Vector2(
                parent.position.x + parent.scale.x/2,
                parent.position.y + parent.scale.y/2
                ),
                parent.scale/2
            )

        self.northWest = QuadTree(self.capacity, boundary_nw)
        self.northWest.insert(self.particles[0])

        self.northEast = QuadTree(self.capacity, boundary_ne)
        self.northEast.insert(self.particles[0])

        self.southWest = QuadTree(self.capacity, boundary_sw)
        self.southWest.insert(self.particles[0])

        self.southEast = QuadTree(self.capacity, boundary_se)
        self.southEast.insert(self.particles[0])


    def insert(self, particle):
        if self.boundary.containsParticle(particle) == False:
            return False

        if len(self.particles) < self.capacity and self.northWest == None:
            self.particles.append(particle)
            return True
        else:
            if self.northWest == None:
                self.subdivide()

            if self.northWest.insert(particle):
                return True
            if self.northEast.insert(particle):
                return True
            if self.southWest.insert(particle):
                return True
            if self.southEast.insert(particle):
                return True
            return False

    def queryRange(self, _range):
        particlesInRange = []

        if self.boundary.intersects(_range):
            return particlesInRange
        else:
            for particle in self.particles:
                if _range.containsParticle(particle):
                    particlesInRange.append(particle)

            if self.northWest != None:
                particlesInRange += self.northWest.queryRange(_range)
                particlesInRange += self.northEast.queryRange(_range)
                particlesInRange += self.southWest.queryRange(_range)
                particlesInRange += self.southEast.queryRange(_range)

            return particlesInRange

    def Show(self, screen):
        self.boundary.Draw(screen)
        if self.northWest != None:
            self.northWest.Show(screen)
            self.northEast.Show(screen)
            self.southWest.Show(screen)
            self.southEast.Show(screen)
