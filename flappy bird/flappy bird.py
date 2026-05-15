import pygame
pygame.init()
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
groundX=0
TPS=60
flying=False

background=pygame.image.load("flappy bird/images/bg.png")
ground=pygame.image.load("flappy bird/images/ground.png")

class birdAnim(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        for i in range(1,4):
            image=pygame.image.load(f"flappy bird/images/bird{i}.png")
            self.images.append(image)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.counter=0
        self.velocity=0
        self.clicked=False
    def update(self):
        global flying
        self.counter+=1
        if self.counter==5:
            self.index+=1
            if self.index==3:
                self.index=0
            self.image=self.images[self.index]
            self.counter=0
        if flying:
            self.velocity+=0.2
            self.rect.y+=self.velocity
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.velocity=0
                self.velocity-=7
                self.clicked=True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            if self.rect.y>460:
                flying=False

bird_group=pygame.sprite.Group()
mainBird=birdAnim(75,300)
bird_group.add(mainBird)

clock=pygame.time.Clock()

while True:
    clock.tick(TPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            flying=True
    screen.blit(background,(0,-100))
    screen.blit(ground,(groundX,500))
    groundX-=1
    if groundX<-35:
        groundX=0
    bird_group.draw(screen)
    bird_group.update()
    pygame.display.update()