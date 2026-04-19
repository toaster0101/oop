import pygame
pygame.init()
WIDTH=400
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("black")
#print(pygame.font.get_fonts())

image1=pygame.image.load("birthday greetings/images/birthday.png")
image1Sca=pygame.transform.scale(image1,(400,400))
font1=pygame.font.SysFont("calisto",15)
text1=font1.render("Happy Birthday",True,"black")
text1r=pygame.transform.rotate(text1,28.15)
text2=font1.render("-Stick bug the third xx",True,"black")
text2r=pygame.transform.rotate(text2,28.15)

image2=pygame.image.load("birthday greetings/images/birthday2.png")
image2Sca=pygame.transform.scale(image2,(400,400))
font2=pygame.font.SysFont("magneto",25)
text3=font2.render("Birthday Wishes",True,"blue")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(image1Sca,(0,0))
    screen.blit(text1r,(160,250))
    screen.blit(text2r,(160,260))
    pygame.display.update()
    pygame.time.wait(5000)
    screen.blit(image2Sca,(0,0))
    screen.blit(text3,(110,326))
    pygame.display.update()
    pygame.time.wait(5000)