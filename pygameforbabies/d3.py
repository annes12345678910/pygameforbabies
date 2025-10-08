import pygame
import math
d3queue = []
def project_3d_to_2d(x, y, z, width, height, fov=200, viewer_distance=5):
    factor = fov / (viewer_distance + z)
    x2d = x * factor + width / 2
    y2d = -y * factor + height / 2
    return int(x2d), int(y2d)

class Cube:
    def __init__(self, size=1):
        s = size / 2
        self.vertices = [
            [-s, -s, -s],
            [ s, -s, -s],
            [ s,  s, -s],
            [-s,  s, -s],
            [-s, -s,  s],
            [ s, -s,  s],
            [ s,  s,  s],
            [-s,  s,  s],
        ]
        self.edges = [
            (0,1),(1,2),(2,3),(3,0),
            (4,5),(5,6),(6,7),(7,4),
            (0,4),(1,5),(2,6),(3,7)
        ]
        self.angle = 0
    def add(self):
        d3queue.append(self)
    def _update(self):
        self.angle += 1
        cos, sin = math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle))
        for i, (x, y, z) in enumerate(self.vertices):
            # Rotate around Y axis
            xz = x * cos - z * sin
            zz = z * cos + x * sin
            self.vertices[i] = [xz, y, zz]

    def _draw(self, screen, width, height):
        points = [project_3d_to_2d(x, y, z, width, height) for (x, y, z) in self.vertices]
        for a, b in self.edges:
            pygame.draw.line(screen, (255, 255, 255), points[a], points[b], 2)
