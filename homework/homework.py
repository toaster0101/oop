import pygame
import random
pygame.init()
WIDTH=600
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
strtTime=(pygame.time.get_ticks())+2000
TPS=60
n=0
jumping=False
gameover=False

dino=pygame.image.load("homework/images/dino.webp")
dino=pygame.transform.scale(dino,(75,75))
hitboxDino=pygame.Rect(100,225,75,75)
cactus=pygame.image.load("homework/images/cactus.webp")
cactus=pygame.transform.scale(cactus,(75,75))
hitboxcactus=pygame.Rect(500,230,75,75)

clock=pygame.time.Clock()

r1=pygame.Rect(0,300,600,100)

while True:
    clock.tick(TPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if hitboxDino.colliderect(r1):
                    jumping=True
    if gameover==False:
        if not hitboxDino.colliderect(r1) and jumping==False:
            hitboxDino.y+=2.5*(hitboxDino.y/100)
        if jumping:
            if pygame.time.get_ticks()-strtTime<1000:
                hitboxDino.y-=2*(hitboxDino.y/100)
            else:
                strtTime=pygame.time.get_ticks()
                jumping=False
        else:
            strtTime=pygame.time.get_ticks()
        hitboxcactus.x-=3
        if hitboxcactus.x<-75:
            hitboxcactus.x=(700+random.randint(-100,100))
    if hitboxDino.colliderect(hitboxcactus):
        gameover=True
    screen.fill("white")
    pygame.draw.rect(screen,"black",r1,0)
    screen.blit(dino,(hitboxDino[0],hitboxDino[1]))
    screen.blit(cactus,(hitboxcactus[0],hitboxcactus[1]))
    pygame.display.update()