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

# Create color palettes
palette1 = np.array([(0, 0, 0.5), (0, 0.5, 1), (0, 1, 1), (1, 1, 0), (1, 0, 0)])
palette2 = np.array([(0.5, 0, 0.5), (1, 0, 1), (1, 0.5, 0.5), (1, 1, 0.5), (0.5, 1, 0.5)])

def update_fluid(t):
    global fluid
    
    # Create moving sources
    x1 = int(width/2 + np.sin(t*0.01) * width/3)
    y1 = int(height/2 + np.cos(t*0.017) * height/3)
    x2 = int(width/2 + np.sin(t*0.022) * width/4)
    y2 = int(height/2 + np.cos(t*0.013) * height/4)
    
    fluid[max(0, x1-20):min(width, x1+20), max(0, y1-20):min(height, y1+20)] += palette1[int(t/10) % 5]
    fluid[max(0, x2-15):min(width, x2+15), max(0, y2-15):min(height, y2+15)] += palette2[int(t/12) % 5]
    
    # Add some randomness
    fluid += np.random.randn(width, height, 3) * 0.03
    
    # Apply diffusion
    fluid = gaussian_filter(fluid, sigma=(1, 1, 0))
    
    # Clip values
    fluid = np.clip(fluid, 0, 1)

running = True
clock = pygame.time.Clock()
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_fluid(t)
    
    # Convert fluid to RGB for display
    display_fluid = (fluid ** 0.5 * 255).astype(np.uint8)
    surf = pygame.surfarray.make_surface(display_fluid.swapaxes(0, 1))
    screen.blit(surf, (0, 0))
    
    pygame.display.flip()
    t += 1
    clock.tick(60)

pygame.quit()