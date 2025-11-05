import pygame
import random

pygame.init()

width, height = 1000, 850
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption("Pixel Chance")

class sprite:
    def __init__(self, image, size):
        self.original_image = pygame.image.load(f"{image}.png")
        self.image = pygame.transform.scale_by(self.original_image, size)
        self.rect = self.image.get_rect()


MainButton = [sprite('MainButtons/Idle', 5),
              sprite('MainButtons/Highlighted', 5),
              sprite('MainButtons/Held', 5)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouseHeld = pygame.mouse.get_pressed()[0]
    mousePos = pygame.mouse.get_pos()
    
    if MainButton[0].rect.collidepoint(mousePos) and mouseHeld:
        print("touchy")
    window.blit(MainButton[0].image, (0,0))

    #pygame.draw.rect(window, 'red', )

    pygame.display.flip()

    clock.tick(60)
    