import pygame
import random
pygame.init()
WIDTH=800
HEIGHT=600
TPS=60
score=0
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
strtTime=pygame.time.get_ticks()
gameover=False

bg=pygame.image.load("recycle/images/bg.webp")
bin=pygame.image.load("recycle/images/bin.png")
bin=pygame.transform.scale(bin,(bin.get_width()/4,bin.get_height()/4))
binBox=bin.get_rect()
bg=pygame.transform.scale(bg,(800,600))

class nonRecyle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("recycle/images/nonRecycle.png")
        self.image=pygame.transform.scale(self.image,(self.image.get_width()/10,self.image.get_height()/10))
        self.rect=self.image.get_rect()

class recyle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        rng=random.randint(0,1)
        if rng==0:
            self.image=pygame.image.load("recycle/images/recycle1.webp")
        if rng==1:
            self.image=pygame.image.load("recycle/images/recycle2.png")
        self.image=pygame.transform.scale(self.image,(self.image.get_width()/10,self.image.get_height()/10))
        self.rect=self.image.get_rect()

nonRecyleG=pygame.sprite.Group()
for i in range(30):
    while True:
        nonRecyleItem=nonRecyle(0,0)
        nonRecyleItem.rect.x=random.randint(0,790)
        nonRecyleItem.rect.y=random.randint(0,590)
        var1=0
        for j in nonRecyleG:
            if nonRecyleItem.rect.colliderect(j.rect):
                var1=1
        if var1==1:
            continue
        if var1==0:
            break
    nonRecyleG.add(nonRecyleItem)

recyleG=pygame.sprite.Group()
for i in range(30):
    while True:
        recyleItem=recyle(0,0)
        recyleItem.rect.x=random.randint(50,790)
        recyleItem.rect.y=random.randint(70,590)
        var2=0
        for j in recyleG:
            for k in nonRecyleG:
                if recyleItem.rect.colliderect(j.rect) or recyleItem.rect.colliderect(k.rect):
                    var2=1
        if var2==1:
            continue
        if var2==0:
            break
    recyleG.add(recyleItem)

def movement():
    if not gameover:
        if binBox.y>-1:
            if keys_pressed[pygame.K_w]:
                binBox.y-=2
        if binBox.y<530:
            if keys_pressed[pygame.K_s]:
                binBox.y+=2
        if binBox.x>-1:
            if keys_pressed[pygame.K_a]:
                binBox.x-=2
        if binBox.x<750:
            if keys_pressed[pygame.K_d]:
                binBox.x+=2

clock=pygame.time.Clock()

font1=pygame.font.SysFont("impact",25)

while True:
    clock.tick(TPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    keys_pressed=pygame.key.get_pressed()
    movement()
    for i in nonRecyleG:
        if binBox.colliderect(i):
            i.kill()
            score-=1
    for i in recyleG:
        if binBox.colliderect(i):
            i.kill()
            score+=1
    screen.blit(bg,(0,0))
    screen.blit(bin,(binBox))
    text1=font1.render("Score = "+str(score),True,"black")
    if not gameover:
        timeRemain=int(40-((pygame.time.get_ticks()-strtTime)/1000))
    timeText=font1.render("Time Remaining = "+str(timeRemain),True,"black")
    if timeRemain==0:
        gameover=True
    nonRecyleG.draw(screen)
    recyleG.draw(screen)
    screen.blit(text1,(10,10))
    screen.blit(timeText,(10,35))
    if gameover:
        if score>20:
            winText=font1.render("You Won!",True,"black")
            screen.blit(winText,(350,270))
        else:
            loseText=font1.render("You Lost!",True,"black")
            screen.blit(loseText,(350,270))
    pygame.display.update()