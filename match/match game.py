import pygame
import random
pygame.init()
WIDTH=650
HEIGHT=650
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
posList=[50,200,350,500]
n=random.choice(posList)

candyNohitbox=pygame.image.load("match/images/candycrush.jpg")
ludoNohitbox=pygame.image.load("match/images/ludo.png")
templeNohitbox=pygame.image.load("match/images/templerun.png")
subwayNohitbox=pygame.image.load("match/images/subwaysurfer.png")

candy=pygame.Rect(100,n,100,100)
posList.remove(n)
n=random.choice(posList)
ludo=pygame.Rect(100,n,100,100)
posList.remove(n)
n=random.choice(posList)
temple=pygame.Rect(100,n,100,100)
posList.remove(n)
n=random.choice(posList)
subway=pygame.Rect(100,n,100,100)

font1=pygame.font.SysFont("calisto",30)
candyNohitboxTEXT=font1.render("Candy Crush",True,"black")
ludoNohitboxTEXT=font1.render("Ludo",True,"black")
templeNohitboxTEXT=font1.render("Temple Run",True,"black")
subwayNohitboxTEXT=font1.render("Subway Surfers",True,"black")

posList=[50,200,350,500]
candyTEXT=pygame.Rect(400,n,100,100)
posList.remove(n)
n=random.choice(posList)
ludoTEXT=pygame.Rect(400,n,100,100)
posList.remove(n)
n=random.choice(posList)
templeTEXT=pygame.Rect(400,n,100,100)
posList.remove(n)
n=random.choice(posList)
subwayTEXT=pygame.Rect(400,n,100,100)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.fill("white")
    screen.blit(candyNohitbox,(candy))
    screen.blit(ludoNohitbox,(ludo))
    screen.blit(templeNohitbox,(temple))
    screen.blit(subwayNohitbox,(subway))
    screen.blit(candyNohitboxTEXT,(candyTEXT))
    screen.blit(ludoNohitboxTEXT,(ludoTEXT))
    screen.blit(templeNohitboxTEXT,(templeTEXT))
    screen.blit(subwayNohitboxTEXT,(subwayTEXT))
    pygame.display.update()