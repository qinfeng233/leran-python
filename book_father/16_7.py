import pygame,sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
plot = []
for x in range(0,640):
    y = int(math.sin(x/640.0 * 4 *math.pi) * 200 + 240)
    plot.append([x,y])
    #pygame.draw.rect(screen,[0,0,0],[x,y,1,1],1)
pygame.draw.lines(screen,[0,0,0],False,plot,2)
pygame.display.flip()
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
pygame.quit()