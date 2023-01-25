import pygame
import sys
import random
import math

global liste
liste=["tas","kagit","makas"]


pygame.init()

pencere = pygame.display.set_mode((800,500), pygame.SWSURFACE)
pygame.display.set_caption("Taş Kağıt Makas")


def resimsec():
    x=random.choice(liste)
    if x=="tas":
        return "taş.png"
    elif x=="kagit":
        return "kağıt.png"
    elif x=="makas":
        return "makas.png"


while True:
    pencere.fill("white")
    resim = pygame.image.load(resimsec())
    pencere.blit(resim,(0,0))





    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    pygame.display.iconify()



    pygame.display.flip()
