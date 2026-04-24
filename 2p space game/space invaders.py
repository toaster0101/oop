import pygame
pygame.init()
WIDTH=600
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
bg=pygame.image.load("2p space game/images/space.png")
TPS=60

spaceship1=pygame.image.load("2p space game/images/spaceship_yellow.png")
spaceship1=pygame.transform.scale(spaceship1,(58,50))
spaceship1=pygame.transform.rotate(spaceship1,90)
hitbox1=pygame.Rect(100,175,44,40)

spaceship2=pygame.image.load("2p space game/images/spaceship_red.png")
spaceship2=pygame.transform.scale(spaceship2,(58,50))
spaceship2=pygame.transform.rotate(spaceship2,270)
hitbox2=pygame.Rect(500,175,44,40)

def spaceship1_move():
    if hitbox1.y>1:
        if keys_pressed[pygame.K_w]:
            hitbox1.y-=1
    if hitbox1.y<256:
        if keys_pressed[pygame.K_s]:
            hitbox1.y+=1
    if hitbox1.x>1:
        if keys_pressed[pygame.K_a]:
            hitbox1.x-=1
    if hitbox1.x<255:
        if keys_pressed[pygame.K_d]:
            hitbox1.x+=1

clock=pygame.time.Clock()

while True:
    clock.tick(TPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    keys_pressed=pygame.key.get_pressed()
    spaceship1_move()
    screen.blit(bg,(0,0))
    pygame.draw.line(screen,"black",(295,0),(295,400),10)
    screen.blit(spaceship1,(hitbox1[0]-3,hitbox1[1]-9))
    #pygame.draw.rect(screen,"red",hitbox1,2)
    screen.blit(spaceship2,(hitbox2[0]-3,hitbox2[1]-9))
    #pygame.draw.rect(screen,"red",hitbox2,2)
    pygame.display.update()