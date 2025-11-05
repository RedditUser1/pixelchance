import pygame
import random

pygame.init()

width, height = 1000, 850
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption("Pixel Chance")

class sprite:
    def __init__(self, image, pos=(0,0), size=5):
        self.original_image = pygame.image.load(f"{image}.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.original_image, size)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = pos[0]-(self.width)
        self.y = pos[1]-(self.height)
        self.pos = (self.x, self.y)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move(self, pos=(0,0)):
        self.x = pos[0]-(self.width)
        self.y = pos[1]-(self.height)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

MainButton = {}
for name in ["Idle", "Highlight", "Held"]:
    MainButton[name.lower()] = sprite(f'MainButtons/{name}', (width/2, height/2), 5)


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

    window.blit(MainButton[MainButtonType].image, MainButton[MainButtonType].pos)


    pygame.display.flip()

    clock.tick(60)
    