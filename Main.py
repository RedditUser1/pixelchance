import pygame
import random

pygame.init()

width, height = 1000, 850
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption("Pixel Chance")

class sprite:
    def __init__(self, image, size):
        self.original_image = pygame.image.load(f"{image}.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.original_image, size)

        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()


MainButton = {"idle": sprite('MainButtons/Idle', 5),
              "highlight": sprite('MainButtons/Highlighted', 5),
              "held": sprite('MainButtons/Held', 5)}

MainButtonType = "idle"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouseHeld = pygame.mouse.get_pressed()[0]
    mousePos = pygame.mouse.get_pos()
    
    if MainButton[MainButtonType].rect.collidepoint(mousePos):
        if mouseHeld:
            MainButtonType = "held"
        else:
            MainButtonType = "highlight"
    else: MainButtonType = "idle"

    window.blit(MainButton[MainButtonType].image,
                (width/2+(MainButton[MainButtonType].width/2),
                 height/2+(MainButton[MainButtonType].height/2)))

    pygame.display.flip()

    clock.tick(60)
    