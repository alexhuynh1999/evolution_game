import pygame
#test comment
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
y = 500
x_vel = 0
y_vel = 0

while switch:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            switch = not switch

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_vel = -5
            elif event.key == pygame.K_RIGHT:
                x_vel = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_vel = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_vel = -5
            elif event.key == pygame.K_DOWN:
                y_vel = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_vel = 0

    x += x_vel
    y += y_vel
    display.fill(white)
    ball(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()