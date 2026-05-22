import pygame
import random
pygame.init()
WIDTH=800
HEIGHT=600
TPS=60
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")

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

nonRecyleG=pygame.sprite.Group()
for i in range(30):
    nonRecyleItem=nonRecyle(0,0)
    nonRecyleItem.rect.x=random.randint(0,790)
    nonRecyleItem.rect.y=random.randint(0,590)
    nonRecyleG.add(nonRecyleItem)

def movement():
    if binBox.y>0:
        if keys_pressed[pygame.K_w]:
            binBox.y-=1
    if binBox.y<530:
        if keys_pressed[pygame.K_s]:
            binBox.y+=1
    if binBox.x>0:
        if keys_pressed[pygame.K_a]:
            binBox.x-=1
    if binBox.x<730:
        if keys_pressed[pygame.K_d]:
            binBox.x+=1

clock=pygame.time.Clock()

while True:
    clock.tick(TPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    keys_pressed=pygame.key.get_pressed()
    movement()
    screen.blit(bg,(0,0))
    screen.blit(bin,(binBox))
    nonRecyleG.draw(screen)
    pygame.display.update()