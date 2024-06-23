import pygame
import numpy as np

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bioluminescent Ecosystem")
'''
Description: This simulation creates a dynamic ecosystem of bioluminescent creatures. 
Each creature has its own color, size, and pulsing pattern. 
They move around the screen, leaving trails behind them. 
Creatures have a lifespan, and when they die, they have a chance to spawn new creatures, simulating reproduction. 
Random bioluminescent particles add to the underwater atmosphere. This demonstrates concepts from ecology and bioluminescence in a visually captivating way.
'''
class Creature:
    def __init__(self):
        self.pos = np.random.rand(2)
        self.vel = (np.random.rand(2) - 0.5) * 0.01
        self.color = np.random.rand(3)
        self.size = np.random.randint(3, 10)
        self.pulse = 0
        self.lifespan = np.random.randint(300, 1000)

creatures = [Creature() for _ in range(100)]

def update_creatures():
    global creatures
    for c in creatures:
        c.pos += c.vel
        c.pos %= 1
        c.vel += (np.random.rand(2) - 0.5) * 0.001
        c.vel = np.clip(c.vel, -0.01, 0.01)
        c.pulse = (c.pulse + np.random.rand() * 0.1) % (2 * np.pi)
        c.lifespan -= 1
        if c.lifespan <= 0:
            creatures.remove(c)
            if np.random.rand() < 0.8:  # 80% chance to spawn two new creatures
                creatures.append(Creature())
                creatures.append(Creature())

running = True
clock = pygame.time.Clock()
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 10))
    
    update_creatures()
    
    for c in creatures:
        brightness = (np.sin(c.pulse) + 1) / 2
        color = (int(c.color[0]*255*brightness), 
                 int(c.color[1]*255*brightness), 
                 int(c.color[2]*255*brightness))
        pygame.draw.circle(screen, color, 
                           (int(c.pos[0]*width), int(c.pos[1]*height)), 
                           int(c.size * brightness))
        
        # Add bioluminescent trails
        for i in range(5):
            trail_pos = c.pos - c.vel * i * 10
            trail_pos %= 1
            trail_color = (int(c.color[0]*255*brightness*0.5), 
                           int(c.color[1]*255*brightness*0.5), 
                           int(c.color[2]*255*brightness*0.5))
            pygame.draw.circle(screen, trail_color, 
                               (int(trail_pos[0]*width), int(trail_pos[1]*height)), 
                               int(c.size * brightness * 0.5))

    # Add random bioluminescent particles
    for _ in range(50):
        pos = np.random.rand(2)
        color = (np.random.randint(0, 100), np.random.randint(100, 200), np.random.randint(200, 256))
        pygame.draw.circle(screen, color, (int(pos[0]*width), int(pos[1]*height)), 1)

    t += 0.1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()