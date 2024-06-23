

import pygame
import numpy as np
import cmath

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Wave Function Visualization")

'''Description: This visualization represents a quantum wave function. 
The main wave (in color) shows the probability distribution and phase of a quantum particle. 
The white circles represent interference patterns. The wave function evolves over time, with changing quantum numbers (n and m) creating a dynamic, shifting pattern.
'''

def psi(x, t, n, m):
    return np.exp(-(x-2*t)**2/4) * np.exp(1j*n*x) + 0.5*np.exp(-(x+2*t)**2/4) * np.exp(1j*m*x)

x = np.linspace(-10, 10, width)
t = 0
n = 5
m = 3

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    wave = psi(x, t, n, m)
    prob = np.abs(wave)**2
    phase = np.angle(wave)

    for i in range(width-1):
        y1 = int(height/2 - prob[i]*height/4)
        y2 = int(height/2 - prob[i+1]*height/4)
        color = pygame.Color(0)
        color.hsva = (phase[i] % (2*np.pi) / (2*np.pi) * 360, 100, 100, 100)
        pygame.draw.line(screen, color, (i, y1), (i+1, y2), 2)

    # Add interference patterns
    for i in range(0, width, 20):
        pygame.draw.circle(screen, (255, 255, 255, 50), (i, int(height/2 + np.sin(t+i/50)*height/4)), 5)

    t += 0.05
    n = 5 + int(np.sin(t/2) * 3)
    m = 3 + int(np.cos(t/3) * 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()