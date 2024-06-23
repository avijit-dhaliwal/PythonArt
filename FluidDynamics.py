import pygame
import numpy as np
from scipy.ndimage import gaussian_filter

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Neon Fluid Dynamics")

'''
Description: This simulation creates a fluid-like effect with neon colors. 
The fluid constantly shifts and evolves, creating mesmerizing patterns. 
The mouse interaction now creates a circular glow effect, simulating the injection of energy into the fluid system.
'''

fluid = np.zeros((width, height, 3), dtype=np.float32)

def update_fluid():
    global fluid
    fluid += np.random.randn(width, height, 3) * 0.1
    fluid = gaussian_filter(fluid, sigma=(1, 1, 0))
    fluid = np.clip(fluid, 0, 1)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_fluid()
    
    surf = pygame.surfarray.make_surface((fluid * 255).astype(np.uint8))
    screen.blit(surf, (0, 0))
    
    mx, my = pygame.mouse.get_pos()
    radius = 30
    for i in range(-radius, radius):
        for j in range(-radius, radius):
            if i*i + j*j <= radius*radius:
                x, y = mx + i, my + j
                if 0 <= x < width and 0 <= y < height:
                    intensity = 0.5 * (1 - (i*i + j*j) / (radius*radius))
                    fluid[x, y] += np.array([intensity, intensity, intensity])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()