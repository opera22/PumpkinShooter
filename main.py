import pygame
import math
import random

pygame.init()

screen_width = 1088
screen_height = 640
fps = 120
clock = pygame.time.Clock()
cannon_x = screen_width // 2
cannon_y = 0
pumpkin_power = 10


bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (1088,640))
pumpkin_img = pygame.image.load("pumpkin.png")
pumpkin_width = 100
pumpkin_height = 100
pumpkin_img = pygame.transform.scale(pumpkin_img, (pumpkin_width, pumpkin_height))

spider_imgs = []
spider_width = 100
spider_height = 75
spider_speed = 2
spider_imgs.append(pygame.transform.scale(pygame.image.load("spider1.png"), (spider_width, spider_height)))
spider_imgs.append(pygame.transform.scale(pygame.image.load("spider2.png"), (spider_width, spider_height)))

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pumpkin Shooter")

pumpkins = []
spiders = []

class Pumpkin():
    def __init__(self, x, y):
        self.x = x - 50
        self.y = y - 50
        self.timeInAir = 0
        self.angle = getMouseAngle()
        self.hitbox = (self.x,self.y,pumpkin_width,pumpkin_height)
        
    def draw(self, game_window):
        game_window.blit(pumpkin_img, (self.x, self.y))
        self.hitbox = (self.x,self.y,pumpkin_width,pumpkin_height)
        pygame.draw.rect(game_window, (255,0,0), self.hitbox,2)

    def getNewPos(self, x, y, power, angle, time):
        velx = power * math.cos(angle)
        vely = power * math.sin(angle)
        dx = velx * time

        dy = -5 * (time**2) + vely * time

        newx = round(x + dx)
        newy = round(y - dy)
        return (newx, newy)

class Spider():
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = screen_height - 100
        self.animationCount = random.randint(0, 59)
        self.animationIndex = 0
        self.direction = random.choice([-1,1])
        self.hitbox = (self.x,self.y,spider_width,spider_height)
    def draw(self, game_window):
        if self.direction == -1:
            game_window.blit(spider_imgs[self.animationIndex], (self.x, self.y))
        if self.direction == 1:
            game_window.blit(pygame.transform.flip(spider_imgs[self.animationIndex], True, False), (self.x, self.y))
        self.animationCount += 1
        if self.animationCount > 30:
            self.animationIndex = 1
        if self.animationCount > 60:
            self.animationIndex = 0
            self.animationCount = 0
        self.hitbox = (self.x,self.y,spider_width,spider_height)
        pygame.draw.rect(game_window, (255,0,0), self.hitbox,2)
    def updatePos(self):
        self.x = self.x + self.direction * spider_speed
        if self.x < 0:
            self.direction = 1
        if self.x > screen_width:
            self.direction = -1

def redrawWindow():
    game_window.blit(bg,(0,0))

    # draw cannon
    mouse_pos = pygame.mouse.get_pos()
    line = [(cannon_x, cannon_y), mouse_pos]
    pygame.draw.line(game_window, (255,255,255), line[0], line[1])
    
    # draw spiders
    for spider in spiders:
        spider.draw(game_window)
    # draw pumpkins
    for pumpkin in pumpkins:
        pumpkin.draw(game_window)


    pygame.display.update()

def getMouseAngle():
    mouse_pos = pygame.mouse.get_pos()
    try:
        angle = math.atan( (cannon_y - mouse_pos[1]) / (cannon_x - mouse_pos[0])  )
    except:
        angle = - math.pi / 2

    if mouse_pos[1] < cannon_y and mouse_pos[0] > cannon_x:
        angle = abs(angle)
    elif mouse_pos[1] < cannon_y and mouse_pos[0] < cannon_x:
        angle = math.pi - angle
    elif mouse_pos[1] > cannon_y and mouse_pos[0] < cannon_x:
        angle = math.pi + abs(angle)
    elif mouse_pos[1] > cannon_y and mouse_pos[0] > cannon_x:
        angle = (math.pi * 2) - angle

    return angle


def checkCollisions():

    # check collisions between pumpkins and spiders
    for p_idx, pumpkin in enumerate(pumpkins):
        for s_idx, spider in enumerate(spiders):
            if pumpkin.y - pumpkin_height / 2 < spider.hitbox[1] + spider.hitbox[3] and pumpkin.y + pumpkin_height / 2> spider.hitbox[1]:
                if pumpkin.x + pumpkin_width / 2 > spider.hitbox[0] and pumpkin.x - pumpkin_width / 2 < spider.hitbox[0] + spider.hitbox[2]:
                    spiders.pop(s_idx)
                    #pumpkins.pop(p_idx)

    for p_idx, pumpkin in enumerate(pumpkins):
        if pumpkin.y > 5000:
            pumpkins.pop(p_idx)

    return


for i in range(0,10):
    spiders.append(Spider())


while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pumpkins.append(Pumpkin(cannon_x, cannon_y))

    for pumpkin in pumpkins:
        pumpkin.timeInAir += 0.03
        pos = pumpkin.getNewPos(pumpkin.x, pumpkin.y, pumpkin_power, pumpkin.angle, pumpkin.timeInAir)
        pumpkin.x = pos[0]
        pumpkin.y = pos[1]

    for spider in spiders:
        spider.updatePos()

    checkCollisions()

    redrawWindow()
