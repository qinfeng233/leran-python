import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
r = pygame.Rect([100,100,200,300])
pygame.draw.rect(screen,[255,0,0],r,1)
pygame.draw.circle(screen,[255,0,0],[r.top],30,0)
pygame.display.flip()
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
pygame.quit()