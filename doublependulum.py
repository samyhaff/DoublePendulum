import pygame
from pygame.locals import *
from numpy import pi, linspace, cos, sin

g = 1
m1 = 40
m2 = 40
L1 = 200 
L2 = 200
theta1 = pi / 2 
theta2 = pi / 2 
theta1_v = 0
theta2_v = 0
theta1_a = 0
theta2_a = 0
old_positions = []

pygame.init()
window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True 

def processInput():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            break 

while running:
    processInput()
    window.fill((0, 0, 0))

    x1 = L1 * sin(theta1) + 400
    y1 = L1 * cos(theta1) + 400
    x2 = x1 + L2 * sin(theta2)
    y2 = y1 + L2 * cos(theta2)

    for position in old_positions:
        pygame.draw.circle(window, (255, 255, 0), position, 1)
    pygame.draw.line(window, (255, 255, 255), (400, 400), (x1, y1), 3)
    pygame.draw.line(window, (255, 255, 255), (x1, y1), (x2, y2), 3)
    pygame.draw.circle(window, (255, 255, 255), (x1, y1), 5)
    pygame.draw.circle(window, (255, 255, 255), (x2, y2), 5)

    old_positions.append((x2, y2))

    theta1_a = (-g * (2 * m1 + m2) * sin(theta1) - m2 * g * sin(theta1 - 2 * theta2) + (-2 * sin(theta1  - theta2) * m2) * (theta2_v * theta2_v * L2 + theta1_v * theta1_v * L1 * cos(theta1 - theta2))) / (L1 * (2 * m1 + m2 - m2 * cos(2 * theta1- 2 * theta2)))
    theta2_a = (2 * sin(theta1 - theta2) * (theta1_v * theta1_v * L1 * (m1 + m2) + g * (m1 + m2) * cos(theta1) + theta2_v * theta2_v * L2 * m2 * cos(theta1 - theta2))) / (L2 * (2 * m1 + m2 -m2 * cos(2 * theta1 - 2 * theta2)))

    theta1_v += theta1_a
    theta2_v += theta2_a
    theta1 += theta1_v
    theta2 += theta2_v

    pygame.display.update()
    clock.tick(60)

pygame.quit()
