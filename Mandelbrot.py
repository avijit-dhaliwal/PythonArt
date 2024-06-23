import pygame
import numpy as np

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mandelbrot Set Explorer")

'''
Description: This program visualizes the Mandelbrot set, a famous fractal. 
Users can zoom in and out using the mouse wheel, exploring the intricate patterns of the set. 
The colors represent how quickly points escape to infinity, creating a visually striking representation of complex mathematical behavior.
'''

def mandelbrot(h, w, max_iter):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y*1j
    z = c
    divtime = max_iter + np.zeros(z.shape, dtype=int)
    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2
    return divtime

max_iter = 100
set = mandelbrot(height, width, max_iter)

scale = 1.0
offset_x, offset_y = -0.5, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # scroll up
                scale *= 0.9
            elif event.button == 5:  # scroll down
                scale /= 0.9

    mouse_x, mouse_y = pygame.mouse.get_pos()
    offset_x += (mouse_x - width/2) * scale / width
    offset_y += (mouse_y - height/2) * scale / height

    y, x = np.ogrid[offset_y-scale:offset_y+scale:height*1j, offset_x-scale:offset_x+scale:width*1j]
    c = x + y*1j
    set = mandelbrot(height, width, max_iter)

    surf = pygame.surfarray.make_surface(set)
    screen.blit(surf, (0, 0))
    pygame.display.flip()

pygame.quit()