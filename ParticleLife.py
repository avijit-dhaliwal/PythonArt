import pygame
import numpy as np

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle Life Simulation")

'''
Description: This simulation models a system of particles with different types, each interacting uniquely with other types. 
The particles move based on these interactions, creating emergent patterns and behaviors. 
A wavy gravity effect adds an additional layer of complexity to the system. 
The result is a dynamic, ever-changing ecosystem of particles with complex interactions and movements.
'''

class Particle:
    def __init__(self, x, y, particle_type):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.type = particle_type

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.99
        self.vy *= 0.99
        self.x %= width
        self.y %= height

particles = []
num_types = 5
colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255)]
interaction_matrix = np.random.rand(num_types, num_types) * 2 - 1

for _ in range(500):
    particles.append(Particle(np.random.rand() * width, np.random.rand() * height, np.random.randint(num_types)))

def force(r):
    return 1 / r if r > 1 else 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for p in particles:
        p.update()
        for other in particles:
            if p != other:
                dx = p.x - other.x
                dy = p.y - other.y
                r = np.sqrt(dx*dx + dy*dy)
                if r < 50:
                    f = force(r)
                    p.vx += f * dx * interaction_matrix[p.type, other.type] * 0.01
                    p.vy += f * dy * interaction_matrix[p.type, other.type] * 0.01

        pygame.draw.circle(screen, colors[p.type], (int(p.x), int(p.y)), 3)

    # Add environmental effects
    for p in particles:
        p.vy += np.sin(p.x / width * 2 * np.pi) * 0.01  # Wavy gravity effect

    pygame.display.flip()
    clock.tick(60)

pygame.quit()