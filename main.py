import pygame
import random
import time
from pygame.locals import *


black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Platformer Game')



points = 0

def showText(msg,x,y,color):
    fontobj = pygame.font.SysFont('couriernew', 30)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x,y))

class Character():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.xchange = 5
        self.ychange = 5
        self.index = 0
        self.img = img


    def draw(self):
        self.p_rect = screen.blit(self.img, (self.x, self.y))
        # if p_rect.colliderect(c_rect):
        #     break


    def move(self):
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_a]:
        #     self.index = 1
        #     self.x -= self.xchange
        #
        #
        # elif keys[pygame.K_d]:
        #     self.index = 0
        #     self.x += self.xchange
        #
        # elif keys[pygame.K_LEFT]:
        #     self.index = 1
        #     self.x -= self.xchange
        #
        # elif keys[pygame.K_RIGHT]:
        #     self.index = 0
        #     self.x += self.xchange



        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         pygame.quit()
        #         exit()
        #     elif event.type == KEYDOWN:
        #         if event.key == K_SPACE:
        #             self.y -= self.ychange
        #
        #     elif event.type == KEYUP:
        #         if event.key == K_SPACE:
        #             self.y+=self.ychange

        # self.x+=self.xchange

        self.y += self.ychange


        #44,55

        # if self.x >= 595:
        #     #self.x = 0
        #     self.y = 320
        # elif self.x <= 0:
        #     #self.x = 0
        #     self.y = 320

        if self.y >= 595:
            self.y = 595
        elif self.y <= 0:
            self.y = 0




class Background(Character):
    def __init__(self, x, y, img):
        super().__init__(x,y, img)
    def bgdraw(self):
        screen.blit(self.img, (self.x, self.y))

    def bgmove(self):
        self.x-=5

        if self.x <= -640:
            self.x = 640




class Sprite(Character):
    def __init__(self,x, y, img):
        self.x = x
        self.y = y
        self.img = img
    def draw(self):
        self.rectangle = screen.blit(self.img, (self.x, self.y))


class Bullet(Sprite):
    def __init__(self,img):
        self.x = 617
        self.y = random.randint(46, 594)
        self.img = img
    def bdraw(self):
        for i in range(0, random.randint(0, 5)):
            self.c_rect = screen.blit(self.img, (self.x, self.y))
    def bulletmove(self):
        self.x-=random.randint(3, 6)

        if self.x <= -23:
            self.x = random.randint(540, 640)
            self.y = random.randint(0, 640)
            self.x -= random.randint(3, 6)

def menu():
    play = pygame.image.load('playbtns.png')
    playclass = Sprite(70, 200, play)

    while 1:
        isittrue = False
        pygame.display.update()

        screen.fill(black)
        playclass.draw()



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if playclass.rectangle.collidepoint(x, y):
                    isittrue = True

        if isittrue == True:
            play()





def p():
    sky = pygame.image.load('skybg.png')

    skybg = Background(0, 0, sky)
    while 1:
        screen.fill(black)
        skybg.draw()
        showText('Press "p" to play', 200, 200, white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    play()
        pygame.display.update()

def gameover():
    sky = pygame.image.load('skybg.png')

    skybg = Background(0, 0, sky)
    while 1:
        screen.fill(black)
        skybg.draw()
        showText('Press "p" to play', 200, 200, white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    play()
        pygame.display.update()




def play():
    mainghost = pygame.image.load('ghost.png')
    mainghost2 = pygame.image.load('ghost2.png')

    sword = pygame.image.load('swords.png')
    fireball = pygame.image.load('fireball.png')

    score = 0

    gameover = pygame.image.load('gameover.png')

    sky = pygame.image.load('skybg.png')

    skybg = Background(0, 0, sky)

    skybg2 = Background(640, 0, sky)

    player = Character(50, 320, mainghost)

    proj = Bullet(fireball)

    end = Character(200, 200, gameover)


    while 1:

        screen.fill(black)


        for i in range(0, random.randint(1, 5)):
            proj.bdraw()
            proj.bulletmove()

        skybg.bgdraw()
        skybg2.bgdraw()


        skybg.bgmove()
        skybg2.bgmove()

        player.draw()

        showText('{}'.format(score), 0, 0, white)



        proj.draw()
        proj.bulletmove()
        player. move()

        if player.p_rect.colliderect(proj.c_rect):
            score += 0
            print(score)
            break

            pygame.display.update()




        if player.x>proj.x+46:
            score+=1
            showText('{}'.format(score), 0, 0, white)
            pygame.display.update()







#46, 25

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    player.ychange = -5
                if event.key == K_p:
                    play()


            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    player.ychange = 5




            








        pygame.display.update()




#menu()
#play()
p()
