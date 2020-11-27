import pygame

pygame.init()

screen_width = 1088
screen_height = 640
fps = 120
clock = pygame.time.Clock()
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (1088,640))
pumpkin_img = pygame.image.load("pumpkin.png")
pumpkin_img = pygame.transform.scale(pumpkin_img, (100, 100))

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pumpkin Shooter")

class Pumpkin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pumpkin_img
        self.rect = self.image.get_rect()
        self.rect.left = 25
        self.rect.centery = screen_height / 2

test_pumpkin = Pumpkin()

all_sprites = pygame.sprite.Group()

all_sprites.add(test_pumpkin)

while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    game_window.blit(bg,(0,0))
    all_sprites.draw(game_window)
    pygame.display.flip()