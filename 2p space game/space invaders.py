import pygame
pygame.init()
WIDTH=600
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
bg=pygame.image.load("2p space game/images/space.png")
TPS=60
bulletListY=[]
bulletListR=[]
timeStartY=pygame.time.get_ticks()-250
timeStartR=pygame.time.get_ticks()-250
healthY=3
healthR=3
gameover=False

spaceship1=pygame.image.load("2p space game/images/spaceship_yellow.png")
spaceship1=pygame.transform.scale(spaceship1,(58,50))
spaceship1=pygame.transform.rotate(spaceship1,90)
hitbox1=pygame.Rect(100,175,44,40)

spaceship2=pygame.image.load("2p space game/images/spaceship_red.png")
spaceship2=pygame.transform.scale(spaceship2,(58,50))
spaceship2=pygame.transform.rotate(spaceship2,270)
hitbox2=pygame.Rect(456,175,44,40)

bulletFire=pygame.mixer.Sound("2p space game/images/Gun+Silencer.mp3")
bulletHit=pygame.mixer.Sound("2p space game/images/Grenade+1.mp3")
bulletCollide=pygame.mixer.Sound("2p space game/images/Collide.mp3")

font=pygame.font.SysFont("impact",25)
gameoverTextY=font.render("Red WINS! WOW",True,"red")
gameoverTextR=font.render("Yellow WINS! WOW",True,"yellow")

def spaceship_move():
    if not gameover:
        if hitbox1.y>0:
            if keys_pressed[pygame.K_w]:
                hitbox1.y-=1
        if hitbox1.y<360:
            if keys_pressed[pygame.K_s]:
                hitbox1.y+=1
        if hitbox1.x>0:
            if keys_pressed[pygame.K_a]:
                hitbox1.x-=1
        if hitbox1.x<251:
            if keys_pressed[pygame.K_d]:
                hitbox1.x+=1

        if hitbox2.y>0:
            if keys_pressed[pygame.K_UP]:
                hitbox2.y-=1
        if hitbox2.y<360:
            if keys_pressed[pygame.K_DOWN]:
                hitbox2.y+=1
        if hitbox2.x>305:
            if keys_pressed[pygame.K_LEFT]:
                hitbox2.x-=1
        if hitbox2.x<556:
            if keys_pressed[pygame.K_RIGHT]:
                hitbox2.x+=1

clock=pygame.time.Clock()

while True:
    clock.tick(TPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if not gameover:
                if event.key==pygame.K_LCTRL:
                    if pygame.time.get_ticks()-timeStartY>250:
                        bulletY=pygame.Rect(hitbox1.x+44,hitbox1.y+18,10,4)
                        bulletListY.append(bulletY)
                        bulletFire.play()
                        timeStartY=pygame.time.get_ticks()
                if event.key==pygame.K_RCTRL:
                    if pygame.time.get_ticks()-timeStartR>250:
                        bulletR=pygame.Rect(hitbox2.x-10,hitbox2.y+18,10,4)
                        bulletListR.append(bulletR)
                        bulletFire.play()
                        timeStartR=pygame.time.get_ticks()
    keys_pressed=pygame.key.get_pressed()
    spaceship_move()
    screen.blit(bg,(0,0))
    pygame.draw.line(screen,"black",(300,0),(300,400),10)
    screen.blit(spaceship1,(hitbox1[0]-3,hitbox1[1]-9))
    pygame.draw.rect(screen,"red",hitbox1,2)
    screen.blit(spaceship2,(hitbox2[0]-3,hitbox2[1]-9))
    pygame.draw.rect(screen,"red",hitbox2,2)
    for i in bulletListY:
        if i.x>600:
            bulletListY.remove(i)
        pygame.draw.rect(screen,"yellow",i)
        i.x+=6
        if i.colliderect(hitbox2):
            bulletListY.remove(i)
            bulletHit.play()
            if not gameover:
                healthR-=1
        for j in bulletListR:
            if i.colliderect(j):
                bulletListY.remove(i)
                bulletListR.remove(j)
                bulletCollide.play()
    for i in bulletListR:
        if i.x<0:
            bulletListR.remove(i)
        pygame.draw.rect(screen,"red",i)
        i.x-=6
        if i.colliderect(hitbox1):
            bulletListR.remove(i)
            bulletHit.play()
            if not gameover:
                healthY-=1
    if healthY==0:
        gameover=True
        screen.blit(gameoverTextY,(200,250))
    if healthR==0:
        gameover=True
        screen.blit(gameoverTextR,(200,250))
    healthYT=font.render("Health = "+str(healthY),True,"Yellow")
    screen.blit(healthYT,(0,0))
    healthRT=font.render("Health = "+str(healthR),True,"Red")
    screen.blit(healthRT,(497,0))
    pygame.display.update()