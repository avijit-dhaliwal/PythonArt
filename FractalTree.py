import pygame
import math
import colorsys

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Tree Explorer")

'''
Description: This animation generates a dynamic fractal tree, demonstrating the concept of recursive geometry. 
The tree's branches split and grow based on mathematical rules, creating a complex, natural-looking structure. 
The color of the branches changes based on their depth in the tree, creating a vibrant rainbow effect. 
The entire tree sways gently, simulating the effect of wind, adding an organic feel to the geometric pattern. 
This visualization beautifully illustrates how complex, life-like structures can emerge from simple, repetitive rules, a key concept in the study of fractals and natural systems.
'''

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def draw_tree(x1, y1, angle, depth):
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        color = hsv_to_rgb(depth/12.0, 1, 1)
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)
        draw_tree(x2, y2, angle - 20, depth - 1)
        draw_tree(x2, y2, angle + 20, depth - 1)

angle = 0
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_tree(width // 2, height, -90 + math.sin(angle) * 20, 12)
    angle += 0.02

    pygame.display.flip()
    clock.tick(60)

pygame.quit()