import pygame
pygame.init()
WIDTH=400
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
x=0

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

class line():
    def __init__(self,start,end,thickness,colour):
        self.start=start
        self.end=end
        self.thickness=thickness
        self.colour=colour
    def draw(self):
        pygame.draw.line(screen,self.colour,(self.start,self.end),self.thickness)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c:
                pos=pygame.mouse.get_pos()
                c1=circle(25,0,pos[0],pos[1],"blue")
                c1.draw()
            if event.key==pygame.K_r:
                pos=pygame.mouse.get_pos()
                r1=rect(50,25,"blue",0,pos[0],pos[1])
                r1.draw()
            if event.key==pygame.K_l:
                pos=pygame.mouse.get_pos()
                pygame.draw.circle(screen,"red",(pos[0],pos[1]),10,0)
                if x==0:
                    pos1=pygame.mouse.get_pos()
                if x==1:
                    pos2=pygame.mouse.get_pos()
                    pygame.draw.line(screen,"red",(pos1[0],pos1[1]),(pos2[0],pos2[1]),5)
                x+=1
                if x==2:
                    x=0
    pygame.display.update()