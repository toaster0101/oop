import pygame
import random
pygame.init()
WIDTH=400
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")

class circle():
    def __init__(self,radius,thickness,x,y,colour):
        self.radius=radius
        self.thickness=thickness
        self.x=x
        self.y=y
        self.colour=colour
    def draw(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)
    def grow(self):
        self.radius+=1
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)
    def shrink(self):
        self.radius-=1
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)
    def moveUP(self):
        self.y-=1
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)
    def moveDOWN(self):
        self.y+=1
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)
    def moveLEFT(self):
        self.x-=1
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)
    def moveRIGHT(self):
        self.x+=1
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)

c1=circle(25,0,200,200,"blue")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                c1.grow()
            if event.button==3:
                screen.fill("black")
                c1.shrink()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                screen.fill("black")
                c1.moveUP()
            if event.key==pygame.K_s:
                screen.fill("black")
                c1.moveDOWN()
            if event.key==pygame.K_a:
                screen.fill("black")
                c1.moveLEFT()
            if event.key==pygame.K_d:
                screen.fill("black")
                c1.moveRIGHT()
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            c2=circle(15,5,pos[0],pos[1],(r,g,b))
            c2.draw()
    pygame.display.update()