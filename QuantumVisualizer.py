import pygame
import numpy as np

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Entanglement Visualizer")

'''
Description: This visualization attempts to represent the abstract concept of quantum entanglement. 
Particles move around the screen, forming connections with other particles when they come close to each other. 
These connections, represented by lines, symbolize quantum entanglement. 
The color and intensity of the connections change based on the distance between particles, creating a dynamic, web-like structure. 
Particles have different colors, representing different quantum states. 
The overall effect is a complex, interconnected system that constantly evolves, mirroring the mysterious and interconnected nature of quantum systems. 
While it's a simplified representation, it provides an intuitive visual metaphor for the complex phenomenon of quantum entanglement.
'''


particles = []
for _ in range(100):
    particles.append([np.random.rand(2), np.random.rand(2), np.random.rand(3)])

def update_particles():
    global particles
    for p in particles:
        p[0] += (p[1] - 0.5) * 0.01
        p[0] %= 1
        p[1] += (np.random.rand(2) - 0.5) * 0.01
        p[1] = np.clip(p[1], 0, 1)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    update_particles()
    
    for i, p1 in enumerate(particles):
        for p2 in particles[i+1:]:
            dist = np.linalg.norm(p1[0] - p2[0])
            if dist < 0.2:
                color = (int((1-dist/0.2)*255), 0, int((1-dist/0.2)*255))
                start = (int(p1[0][0]*width), int(p1[0][1]*height))
                end = (int(p2[0][0]*width), int(p2[0][1]*height))
                pygame.draw.line(screen, color, start, end, 1)
        
        pygame.draw.circle(screen, (int(p1[2][0]*255), int(p1[2][1]*255), int(p1[2][2]*255)),
                           (int(p1[0][0]*width), int(p1[0][1]*height)), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()