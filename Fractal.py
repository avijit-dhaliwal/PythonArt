import pygame
import numpy as np

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Dimension Shifter")

'''
Description: This animation creates a morphing Sierpinski triangle, a famous fractal. 
The fractal's depth changes over time, creating a breathing effect. 
Additionally, the points of the fractal shift slightly based on a sine wave, adding a fluid, organic quality to the geometric shape. 
The entire fractal also rotates, creating a hypnotic, ever-changing pattern.
'''

def sierpinski(n, p1, p2, p3, shift):
    if n == 0:
        pygame.draw.polygon(screen, (255, 255, 255), [p1, p2, p3], 1)
    else:
        p12 = ((p1[0] + p2[0])/2 + shift*np.sin(t/10), (p1[1] + p2[1])/2 + shift*np.cos(t/10))
        p23 = ((p2[0] + p3[0])/2 + shift*np.sin(t/10), (p2[1] + p3[1])/2 + shift*np.cos(t/10))
        p31 = ((p3[0] + p1[0])/2 + shift*np.sin(t/10), (p3[1] + p1[1])/2 + shift*np.cos(t/10))
        sierpinski(n-1, p1, p12, p31, shift/2)
        sierpinski(n-1, p2, p23, p12, shift/2)
        sierpinski(n-1, p3, p31, p23, shift/2)

running = True
clock = pygame.time.Clock()
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    center = width // 2, height // 2
    radius = min(width, height) // 2 - 10
    angle = t * 0.01
    p1 = (center[0] + int(radius * np.cos(angle)), 
          center[1] + int(radius * np.sin(angle)))
    p2 = (center[0] + int(radius * np.cos(angle + 2*np.pi/3)), 
          center[1] + int(radius * np.sin(angle + 2*np.pi/3)))
    p3 = (center[0] + int(radius * np.cos(angle + 4*np.pi/3)), 
          center[1] + int(radius * np.sin(angle + 4*np.pi/3)))
    
    depth = int(6 + 2 * np.sin(t * 0.05))
    shift = 20 * np.sin(t * 0.1)
    sierpinski(depth, p1, p2, p3, shift)
    
    t += 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()