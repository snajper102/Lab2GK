import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
color = (255, 255, 255)

# Changing surface color
win.fill(color)
# deklarowanie kolorów
CZARNY = (0, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.draw.circle(win, CZARNY, (250, 250), 100, 100)
    pygame.draw.rect(win, ZOLTY, (200, 200, 100, 100))




    pygame.display.update()
