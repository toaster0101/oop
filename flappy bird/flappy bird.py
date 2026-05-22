import pygame
import random
pygame.init()
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
groundX=0
TPS=60
flying=False
score=0
gameover=False
pipeFrec=2000
lastPipe=pygame.time.get_ticks()-2000

background=pygame.image.load("flappy bird/images/bg.png")
ground=pygame.image.load("flappy bird/images/ground.png")
restart=pygame.image.load("flappy bird/images/restart.png")

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
        global flying, gameover
        if not gameover:
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
        if flying and not gameover:
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.velocity=0
                self.velocity-=7
                self.clicked=True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            if self.rect.y>460:
                flying=False
                gameover=True
                self.rect.y=470
        self.image=pygame.transform.rotate(self.images[self.index],self.velocity*-2)

class pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,pipePos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("flappy bird/images/pipe.png")
        self.rect=self.image.get_rect()
        if pipePos==-1:
            self.rect.topleft=[x,y]
        if pipePos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y]
        self.passed=False
    def update(self):
        if not gameover:
            self.rect.x-=2
        if self.rect.right<0:
            self.kill()


bird_group=pygame.sprite.Group()
mainBird=birdAnim(150,300)
bird_group.add(mainBird)

pipe_group=pygame.sprite.Group()

clock=pygame.time.Clock()

font1=pygame.font.SysFont("impact",25)

while True:
    clock.tick(TPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN and not gameover:
            flying=True
        if event.type==pygame.MOUSEBUTTONDOWN and gameover:
            pos=pygame.mouse.get_pos()
            r1=pygame.Rect(pos[0]-2,pos[1]+2,4,4)
            if r1.colliderect(restartHit):
                gameover=False
                flying=False
                bird_group=pygame.sprite.Group()
                mainBird=birdAnim(150,300)
                bird_group.add(mainBird)
                for i in pipe_group:
                    i.kill()
    screen.blit(background,(0,-100))
    currentTime=pygame.time.get_ticks()
    if (currentTime-lastPipe)>pipeFrec and flying and not gameover:
        pipeYDiff=random.randint(-100,100)
        mainPipe=pipes(800,400+pipeYDiff,-1)
        topPipe=pipes(800,200+pipeYDiff,1)
        pipe_group.add(mainPipe)
        pipe_group.add(topPipe)
        lastPipe=currentTime
    pipe_group.draw(screen)
    pipe_group.update()
    screen.blit(ground,(groundX,500))
    if not gameover:
        groundX-=2
    if groundX<-35:
        groundX=0
    text1=font1.render("Score = "+str(int(score)),True,"black")
    screen.blit(text1,(10,10))
    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False):
        gameover=True
    for i in pipe_group:
        if i.rect.right<bird_group.sprites()[0].rect.left and not i.passed:
            i.passed=True
            score+=0.5
    if gameover:
        restartHit=restart.get_rect(center=(400,300))
        screen.blit(restart,(restartHit))
    bird_group.draw(screen)
    bird_group.update()
    pygame.display.update()