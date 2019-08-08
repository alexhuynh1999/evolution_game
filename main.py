import pygame

pygame.init()

width = 800
height = 600

display = pygame.display.set_mode((width,height))
pygame.display.set_caption('caption')
black = (0,0,0)
white = (255,255,255)

char = pygame.image.load('green ball.png')
clock = pygame.time.Clock()
switch = True

def ball (x,y):
    display.blit(char, (x,y))

x = width * 0.45
y = height * 0.8

while switch:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            switch = not switch
    display.fill(white)
    ball(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()