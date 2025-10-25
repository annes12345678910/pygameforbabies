import pygame

bobby = pygame.Surface((100,100))
pygame.draw.circle(bobby, "red", (50,50), 50)

pygame.draw.circle(bobby, "white", (25,25), 10)
pygame.draw.circle(bobby, "white", (75,25), 10)

pygame.draw.circle(bobby, "black", (75,25), 5)
pygame.draw.circle(bobby, "black", (25,25), 5)

pygame.draw.line(bobby, "black", (25,75), (75, 75), 10)