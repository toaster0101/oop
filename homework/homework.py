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
score=0
scorable=True
cloud1speed=2+random.randint(-1,2)
cloud2speed=2+random.randint(-1,2)

dino=pygame.image.load("homework/images/dino.webp")
dino=pygame.transform.scale(dino,(75,75))
hitboxDino=pygame.Rect(100,225,75,75)
cactus=pygame.image.load("homework/images/cactus.webp")
cactus=pygame.transform.scale(cactus,(75,75))
hitboxcactus=pygame.Rect(500,230,75,75)
cloud1=pygame.image.load("homework/images/cloud1.png")
cloud2=pygame.image.load("homework/images/cloud2.png")
cloud1=pygame.transform.scale(cloud1,(100,100))
cloud2=pygame.transform.scale(cloud2,(75,75))
cloud1hitbox=pygame.Rect(700,50,100,100)
cloud2hitbox=pygame.Rect(700,100,75,75)

clock=pygame.time.Clock()

r1=pygame.Rect(0,300,600,100)

font1=pygame.font.SysFont("calisto",15)
font2=pygame.font.SysFont("impact",25)
gameoverText=font2.render("GAMEOVER",True,"red")

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
            scorable=True
    text1=font1.render("Score = "+str(score),True,"black")
    if hitboxDino.colliderect(hitboxcactus):
        gameover=True
    elif hitboxcactus.x<hitboxDino.x:
        if scorable:
            score+=1
        scorable=False
    screen.fill("white")
    pygame.draw.rect(screen,"black",r1,0)
    screen.blit(text1,(10,10))
    if gameover:
        screen.blit(gameoverText,(240,100))
    if not gameover:
        cloud1hitbox.x-=cloud1speed
        cloud2hitbox.x-=cloud2speed
        if cloud1hitbox.x<-100:
            cloud1hitbox.x=700+random.randint(-100,200)
            cloud1hitbox.y=75+random.randint(-75,75)
            cloud1speed=2+random.randint(-1,2)
        if cloud2hitbox.x<-75:
            cloud2hitbox.x=675+random.randint(-75,200)
            cloud2hitbox.y=75+random.randint(-75,75)
            cloud2speed=2+random.randint(-1,2)
    screen.blit(dino,(hitboxDino[0],hitboxDino[1]))
    screen.blit(cactus,(hitboxcactus[0],hitboxcactus[1]))
    screen.blit(cloud1,(cloud1hitbox[0],cloud1hitbox[1]))
    screen.blit(cloud2,(cloud2hitbox[0],cloud2hitbox[1]))
    pygame.display.update()