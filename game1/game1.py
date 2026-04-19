import pygame
pygame.init()
WIDTH=400
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#clock=pygame.time.Clock()
timeStart=pygame.time.get_ticks()
bg=pygame.image.load("game1/images/bg.png")
screen.blit(bg,(0,0))
x=0
y=0
gameover=True

rocket=pygame.image.load("game1/images/rocket.png")
font=pygame.font.SysFont("wingdings",25)
text=font.render("Gameover",True,"white")
font2=pygame.font.SysFont("broadway",25)
text2=font2.render("(Gameover)",True,"white")

star=pygame.image.load("game1/images/star.png")
#print(pygame.font.get_fonts())

while gameover:
    y+=0.01
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                screen.blit(bg,(0,0))
                y-=10
            if event.key==pygame.K_s:
                screen.blit(bg,(0,0))
                y+=10
            if event.key==pygame.K_a:
                screen.blit(bg,(0,0))
                x-=10
            if event.key==pygame.K_d:
                screen.blit(bg,(0,0))
                x+=10
    if y>350:
        screen.blit(bg,(0,0))
        screen.blit(text,(0,0))
        screen.blit(text2,(0,30))
        pygame.display.update()
        pygame.time.wait(10000)
        gameover=False
    else:
        if pygame.time.get_ticks()-timeStart>2000:
            
            screen.blit(bg,(0,0))
            screen.blit(star,(0,0))
            pygame.display.update()
            pygame.time.wait(10000)
            gameover=False
        else:
            screen.blit(bg,(0,0))
        screen.blit(rocket,(x,y))
    pygame.display.update()