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

class circle():
    def __init__(self,radius,thickness,x,y,colour):
        self.radius=radius
        self.thickness=thickness
        self.x=x
        self.y=y
        self.colour=colour
    def draw(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius,self.thickness)
faceBG=circle(200,0,200,200,"yellow")
faceBG.draw()
eye1=circle(50,0,100,100,"black")
eye1.draw()
eye1W=circle(25,0,75,100,"white")
eye1W.draw()
eye2=circle(50,0,300,100,"black")
eye2.draw()
eye2W=circle(25,0,325,100,"white")
eye2W.draw()
mouthc1=circle(25,0,150,325,"white")
mouthc3=circle(27,0,150,325,"red")
mouthc3.draw()
mouthc4=circle(27,0,250,325,"red")
mouthc4.draw()
mouthc1.draw()
mouthc2=circle(25,0,250,325,"white")
mouthc2.draw()

mouth2=rect(100,54,"red",0,150,298)
mouth2.draw()
mouth=rect(100,50,"white",0,150,300)
mouth.draw()
mLine1=rect(5,50,"black",0,150,300)
mLine1.draw()
mLine2=rect(5,50,"black",0,200,300)
mLine2.draw()
mLine3=rect(5,50,"black",0,250,300)
mLine3.draw()
mLine4=rect(148,5,"black",0,126,322.5)
mLine4.draw()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()