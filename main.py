import pygame
import math

pygame.init()

screen_width = 1088
screen_height = 640
fps = 120
pumpkin_vel = 10
clock = pygame.time.Clock()
cannon_x = screen_width // 2
cannon_y = 0


bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (1088,640))
pumpkin_img = pygame.image.load("pumpkin.png")
pumpkin_img = pygame.transform.scale(pumpkin_img, (100, 100))

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pumpkin Shooter")

class Pumpkin():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, game_window):
        game_window.blit(pumpkin_img, (self.x, self.y))

    @staticmethod
    def ballPath(self, startx, starty, power, angle, time):
        pass

def redrawWindow():
    game_window.blit(bg,(0,0))

    # draw cannon
    mouse_pos = pygame.mouse.get_pos()
    line = [(cannon_x, cannon_y), mouse_pos]
    pygame.draw.line(game_window, (255,255,255), line[0], line[1])
    # draw pumpkins

    # draw spiders

    pygame.display.update()

""" test_pumpkin = Pumpkin(60)

pumpkins = pygame.sprite.Group()

pumpkins.add(test_pumpkin) """

while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    
    redrawWindow()
"""     test_pumpkin.updatePos()
    pumpkins.add(test_pumpkin)
    pumpkins.draw(game_window)
    pygame.display.flip() """