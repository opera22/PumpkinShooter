import pygame
import math

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
pumpkin_img = pygame.transform.scale(pumpkin_img, (100, 100))

spider_imgs = []
spider_imgs.append(pygame.image.load("spider1.png"))
spider_imgs.append(pygame.image.load("spider2.png"))

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
        
    def draw(self, game_window):
        game_window.blit(pumpkin_img, (self.x, self.y))

    def getNewPos(self, x, y, power, angle, time):
        velx = power * math.cos(angle)
        vely = power * math.sin(angle)
        dx = velx * time

        dy = -5 * (time**2) + vely * time

        newx = round(x + dx)
        newy = round(y - dy)
        return (newx, newy)

class Spider():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animationCount = 0
    def draw(self, game_window):
        game_window.blit(spider_imgs[animationCount], (self.x, self.y))

def redrawWindow():
    game_window.blit(bg,(0,0))

    # draw cannon
    mouse_pos = pygame.mouse.get_pos()
    line = [(cannon_x, cannon_y), mouse_pos]
    pygame.draw.line(game_window, (255,255,255), line[0], line[1])
    # draw pumpkins
    for pumpkin in pumpkins:
        pumpkin.draw(game_window)
    # draw spiders

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
    # check collisions with walls

    # check collisions between pumpkins and spiders

    return


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
        if pumpkin.x < 0 or pumpkin.x > screen_width:
            pumpkins.pop(pumpkins.index(pumpkin))
        if pumpkin.y < 0 or pumpkin.y > screen_height:
            pumpkins.pop(pumpkins.index(pumpkin))
    
    redrawWindow()
