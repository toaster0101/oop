import pygame
pygame.init()
WIDTH=400
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")

class rect():
    def __init__(self,width,height,colour,thickness,x,y):
        self.width=width
        self.height=height
        self.colour=colour
        self.thickness=thickness
        self.x=x
        self.y=y
    def draw(self):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,self.width,self.height),self.thickness)
r1=rect(80,40,"white",5,160,180)
r1.draw()
r2=rect(40,80,"white",0,0,0)
r2.draw()

class circle():
    def __init__(self,radius,thickness,x,y,colour):
        self.radius=radius
        self.thickness=thickness
        self.x=x
        self.y=y
        self.colour=colour
    def draw(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)
c1=circle(100,5,200,200,"white")
c1.draw()
c2=circle(50,0,350,50,"white")
c2.draw()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()