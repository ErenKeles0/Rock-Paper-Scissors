import pygame
import sys
import random
import math


global liste
liste=["tas","kagit","makas"]

global playerskor
global aiskor

aiskor=0
playerskor=0
airesim=0
playerresim=1







pygame.init()
pencere = pygame.display.set_mode((1000,650), pygame.SWSURFACE)
pygame.display.set_caption("Taş Kağıt Makas")




font=pygame.font.SysFont("ComicSansMs",72)
font2=pygame.font.SysFont("ComicSansMs",24)
font3=pygame.font.SysFont("ComicSansMs",48)







secildi=False

arttiralimmi=True


finish=font.render("CHOOSE ONE",2,("black"),("white"))


def resimsec():
    global airesim
    x=random.choice(liste)
    if x=="tas":
        airesim=1
        return "taş.png"
    elif x=="kagit":
        airesim=2
        return "kağıt.png"
    elif x=="makas":
        airesim=3
        return "makas.png"


resim = pygame.image.load("soruisareti.png")
resim2 = pygame.image.load("taş1.png")
while True:
    pencere.fill("white")
    #resim = pygame.image.load(resimsec())
    pencere.blit(resim,(100,100))

    ai=font.render("AI",2,("black"),("white"))
    pencere.blit(ai,(150,0))
    you=font.render("YOU",2,("black"),("white"))
    pencere.blit(you,(675,0))

    A=font2.render("A:ROCK",2,("black"),("white"))
    S=font2.render("S:PAPER",2,("black"),("white"))
    D=font2.render("D:SCİSSORS",2,("black"),("white"))
    R=font2.render("R:READY",2,("black"),("white"))
    pencere.blit(A,(100,400))
    pencere.blit(S,(100,450))
    pencere.blit(D,(100,500))

    pencere.blit(R,(100,550))

    aiskortitle=font3.render(("AI:"+str(aiskor)),2,("black"),("white"))
    playerskortitle=font3.render(("PLAYER:"+str(playerskor)),2,("black"),("white"))



    pencere.blit(aiskortitle,(500,550))
    pencere.blit(playerskortitle,(700,550))


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    pygame.display.iconify()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    playerresim=1
                    resim2 = pygame.image.load("taş1.png")

                elif event.key == pygame.K_s:
                    playerresim=2
                    resim2 = pygame.image.load("kağıt1.png")

                elif event.key == pygame.K_d:
                    playerresim=3
                    resim2 = pygame.image.load("makas1.png")
                elif event.key == pygame.K_r:
                    for i in range(20):
                        finish=font.render("WAİTİNG...",2,("black"),("white"))
                        resim = pygame.image.load(resimsec())
                        pencere.blit(resim,(100,100))
                        pencere.blit(resim2,(650,100))
                        pencere.blit(finish,(450,400))
                        pygame.time.wait(50)
                        pygame.display.flip()
                    arttiralimmi=True
                    secildi=True


    if secildi:


        if airesim==1 and playerresim==1:
            finish=font.render("DRAW",2,("black"),("white"))

        elif airesim==2 and playerresim==2:
            finish=font.render("DRAW",2,("black"),("white"))

        elif airesim==3 and playerresim==3:
            finish=font.render("DRAW",2,("black"),("white"))

        elif airesim==1 and playerresim==2:
            finish=font.render("PLAYER WİN",2,("black"),("white"))
            if arttiralimmi:
                playerskor=playerskor+1
                arttiralimmi=False
        elif airesim==2 and playerresim==1:
            finish=font.render("AI WİN",2,("black"),("white"))
            if arttiralimmi:
                aiskor=aiskor+1
                arttiralimmi=False
        elif airesim==1 and playerresim==3:
            finish=font.render("AI WİN",2,("black"),("white"))
            if arttiralimmi:
                aiskor=aiskor+1
                arttiralimmi=False
        elif airesim==3 and playerresim==1:
            finish=font.render("PLAYER WİN",2,("black"),("white"))
            if arttiralimmi:
                playerskor=playerskor+1
                arttiralimmi=False

        elif airesim==2 and playerresim==3:
            finish=font.render("PLAYER WİN",2,("black"),("white"))
            if arttiralimmi:
                playerskor=playerskor+1
                arttiralimmi=False

        elif airesim==3 and playerresim==2:
            finish=font.render("AI WİN",2,("black"),("white"))
            if arttiralimmi:
                aiskor=aiskor+1
                arttiralimmi=False
        secildi=False

    pencere.blit(finish,(450,400))
    pencere.blit(resim2,(650,100))



    pygame.display.flip()
