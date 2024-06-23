import pygame
import math
import random
from perlin_noise import PerlinNoise

pygame.init()

'''
Description: The Cosmic Bloom animation creates a mesmerizing, flower-like pattern that evolves over time. 
It uses Perlin noise to generate organic, flowing movements, combined with polar coordinates to create a radial pattern. 
The animation draws lines that radiate from the center, with their length and angle determined by noise functions. 
The color of the lines shifts gradually, creating a subtle rainbow effect. 
The result is a dynamic, ever-changing pattern that resembles a blooming flower or an expanding galaxy, showcasing the beauty that can emerge from combining simple mathematical concepts.
'''


width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cosmic Bloom")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

noise = PerlinNoise(octaves=4, seed=1)

particles = []
for _ in range(100):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(1, 3)
    speed = random.uniform(0.1, 0.5)
    particles.append([x, y, size, speed])

t = 0
num_arms = 5
max_radius = 350

def draw_arm(angle, t):
    points = []
    for i in range(100):
        r = i * 3.5
        # Fix: Use a single value for noise instead of two
        theta = angle + 0.1 * i + 0.1 * noise([t * 0.01, i * 0.01])
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
    return points

def color_shift(t):
    r = int(128 + 127 * math.sin(t * 0.023))
    g = int(128 + 127 * math.sin(t * 0.037))
    b = int(128 + 127 * math.sin(t * 0.051))
    return (r, g, b)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    for particle in particles:
        particle[1] += particle[3]
        if particle[1] > height:
            particle[1] = 0
        pygame.draw.circle(screen, (50, 50, 50), (int(particle[0]), int(particle[1])), particle[2])

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_angle = math.atan2(mouse_y - height/2, mouse_x - width/2)

    for i in range(num_arms):
        angle = 2 * math.pi * i / num_arms + t * 0.01 + mouse_angle
        arm_points = draw_arm(angle, t)
        color = color_shift(t + i * 10)
        pygame.draw.lines(screen, color, False, [(p[0] + width/2, p[1] + height/2) for p in arm_points], 2)

    pygame.draw.circle(screen, WHITE, (width//2, height//2), 5)

    pygame.display.flip()
    t += 1
    clock.tick(60)

pygame.quit()