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

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                pos=pygame.mouse.get_pos()
                r1=rect(100,100,"orange",0,pos[0],pos[1])
                r1.draw()
            if event.button==3:
                pos=pygame.mouse.get_pos()
                r1=rect(25,20,"blue",0,pos[0],pos[1])
                r1.draw()
        if event.type==pygame.MOUSEWHEEL:
            pos=pygame.mouse.get_pos()
            r1=rect(20,40,"brown",0,pos[0],pos[1])
            r1.draw()
    pygame.display.update()