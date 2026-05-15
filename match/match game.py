import pygame
import random
pygame.init()
WIDTH=650
HEIGHT=650
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
posList=[50,200,350,500]
n=random.choice(posList)
score=0

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
candyTEXT=pygame.Rect(400,n,180,40)
posList.remove(n)
n=random.choice(posList)
ludoTEXT=pygame.Rect(400,n,80,40)
posList.remove(n)
n=random.choice(posList)
templeTEXT=pygame.Rect(400,n,160,40)
posList.remove(n)
n=random.choice(posList)
subwayTEXT=pygame.Rect(400,n,210,40)

matchList=[(candy,candyTEXT),(ludo,ludoTEXT),(subway,subwayTEXT),(temple,templeTEXT)]
strtPos=None
endPos=None
strtRect=None
endRect=None
clickedImgRect=False
clickedTxtRect=False
lineColor=None
correct=False

screen.fill("white")
screen.blit(candyNohitboxTEXT,(candyTEXT))
screen.blit(ludoNohitboxTEXT,(ludoTEXT))
screen.blit(templeNohitboxTEXT,(templeTEXT))
screen.blit(subwayNohitboxTEXT,(subwayTEXT))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            strtPos=pygame.mouse.get_pos()
            for I,T in matchList:
                if I.collidepoint(strtPos):
                    clickedImgRect=True
                    strtRect=I
                    break
            if clickedImgRect:
                pygame.draw.circle(screen,"black",strtPos,10,2)
        if event.type==pygame.MOUSEBUTTONUP:
            endPos=pygame.mouse.get_pos()
            for I,T in matchList:
                if T.collidepoint(endPos):
                    clickedTxtRect=True
                    endRect=T
                    break
            if clickedTxtRect:
                pygame.draw.circle(screen,"black",endPos,10,2)
            if clickedImgRect and clickedTxtRect:
                correct=False
                for I,T in matchList:
                    if I==strtRect and T==endRect:
                        lineColor="green"
                        correct=True
                        score+=1
                if not correct:
                    lineColor="red"
                    score-=1
                pygame.draw.line(screen,lineColor,strtPos,endPos,10)
            clickedTxtRect=False
            clickedImgRect=False
    scoreNoHitbox=font1.render("Score = "+str(score),True,"black")
    scoreText=pygame.Rect(10,10,1,1)
    whiteB=pygame.Rect(0,0,200,50)
    screen.blit(scoreNoHitbox,(scoreText))
    pygame.draw.rect(screen,"white",whiteB)
    screen.blit(scoreNoHitbox,(scoreText))
    screen.blit(candyNohitbox,(candy))
    screen.blit(ludoNohitbox,(ludo))
    screen.blit(templeNohitbox,(temple))
    screen.blit(subwayNohitbox,(subway))
    pygame.display.update()