import pygame,sys
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
size = width,height = 640,480
screen = pygame.display.set_mode(size)
image_file = 'beach_ball.png'
screen.fill([255,255,255])
balls = []
for row in range(0,3):
    for column in range(0,3):
        location = [column * 180 +10,row * 180 + 10]
        ball = MyBallClass(image_file,location)
        balls.append(ball)

while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for ball in balls :
        screen.blit(ball.image,ball.rect)
        pygame.display.flip()
pygame.quit()