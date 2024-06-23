import pygame
import numpy as np

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hyperdimensional Wormhole")

'''
Description: The Hyperdimensional Wormhole creates an otherworldly, pulsating pattern that seems to draw the viewer into another dimension. 
It uses trigonometric functions and distance calculations to generate a circular, tunnel-like effect. 
The pattern evolves over time, with waves of intensity radiating outward from the center. 
The resulting visualization resembles a wormhole or a portal, with depth and movement that create an illusion of 3D space on a 2D screen. 
This animation demonstrates how complex, seemingly 3D effects can be achieved with 2D mathematics, touching on concepts from physics and higher-dimensional geometry.
'''

def create_wormhole(t):
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R * 10 + t) / (R + 1)
    return Z

running = True
clock = pygame.time.Clock()
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    wormhole = create_wormhole(t)
    wormhole = (wormhole - wormhole.min()) / (wormhole.max() - wormhole.min())
    
    surf = pygame.surfarray.make_surface((wormhole * 255).astype(np.uint8))
    screen.blit(surf, (0, 0))
    
    t += 0.1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()