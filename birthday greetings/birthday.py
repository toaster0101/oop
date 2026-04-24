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

image3=pygame.image.load("birthday greetings/images/birthday3.jpg")
image3Sca=pygame.transform.scale(image3,(400,400))
font3=pygame.font.SysFont("harrington",25)
text4=font3.render("You've made it through another year",True,"blue")

image4=pygame.image.load("birthday greetings/images/birthday4.jpg")
image4Sca=pygame.transform.scale(image4,(400,400))
font4=pygame.font.SysFont("broadway",25)
text5=font4.render("Have a Lovely Day",True,"blue")

image5=pygame.image.load("birthday greetings/images/birthday5.png")
image5Sca=pygame.transform.scale(image4,(400,400))
font5=pygame.font.SysFont("script",25)
text6=font5.render("Have a Great Year Ahead",True,"blue")
text6r=pygame.transform.rotate(text2,15)

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
    screen.blit(image3Sca,(0,0))
    screen.blit(text4,(110,150))
    pygame.display.update()
    pygame.time.wait(5000)
    screen.blit(image4Sca,(0,0))
    screen.blit(text5(110,150))
    pygame.display.update()
    pygame.time.wait(5000)
    screen.blit(image5Sca,(0,0))
    screen.blit(text6r(110,150))
    pygame.display.update()
    pygame.time.wait(5000)