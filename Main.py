""""""""""""""""""""""""""""""""""
PixelChance Version 1.2

Made by the oblivion and masterRahj

"""""""""""""""""""""""""""""""""""
#------------------------------
# Imports and Initialization
#------------------------------
import pygame
import random

pygame.init()

#------------------------------
# Window setup
#------------------------------
width, height = 1000, 850
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption("Pixel Chance")

#------------------------------------------------
# Buttons Sprite Class (For main Rolling Button)
#------------------------------------------------
class Sprite:
    def __init__(self, image, pos=(0, 0), size=5):
        self.original_image = pygame.image.load(f"{image}.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.original_image, size)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = pos[0] - self.width/2
        self.y = pos[1] - self.height/2
        self.pos = (self.x, self.y)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self, pos=(0, 0)):
        self.x = pos[0] - self.width/2
        self.y = pos[1] - self.height/2
        self.pos = (self.x, self.y)
        self.rect.center = pos

#-----------------------------
# Main button setup
#-----------------------------
MainButton = {}
for name in ["Idle", "Highlight", "Held"]:
    MainButton[name.lower()] = Sprite(f"MainButtons/{name}", (width / 2, height / 2), 5, )

MainButtonType = "idle"

#-----------------------------
# Main loop
#-----------------------------

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
    else:
        MainButtonType = "idle"

    window.blit(MainButton[MainButtonType].image, MainButton[MainButtonType].pos)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()