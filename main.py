import pygame
import random
pygame.init()
WIDTH=850
HEIGHT=750
flying=False
game_over=False
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FLAPPY BIRD")
bg=pygame.image.load("C:\Aahana\Game Dev 2\lesson8\Things\city.png")
ground=pygame.image.load("C:\Aahana\Game Dev 2\lesson8\Things\ground.png")
pipe_freq=1500
last_pipe=pygame.time.get_ticks()-pipe_freq
game=True
ground_x=0
class Flappy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.img=["C:\Aahana\Game Dev 2\lesson8\Things\Flappy up.png","C:\Aahana\Game Dev 2\lesson8\Things\Flappy middle.png","C:\Aahana\Game Dev 2\lesson8\Things\Flappy down.png"]
        self.index=0
        self.images=[]
        for i in self.img:
            img=pygame.image.load(i)
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=x,y
        self.count=0
        self.vel=0
        self.click=False
    def update(self):
        #gravity|
        #       \/
        if flying==True:
            self.vel+=0.2
            if self.vel >5:
                self.vel=5

            if self.rect.bottom <680: 
                self.rect.y+=self.vel
        # jump |
        #      V
        if game_over==False:
            if pygame.mouse. get_pressed()[0]==1 and self.click ==False:
                self.vel=-7
                self.click=True
            if pygame.mouse.get_pressed()[0]==0:
                self.click=False   
            self.count=0
            self.index=self.index+1
            if self.index>=3:
                self.index=0
            self.image=self.images[self.index]
class Pipe (pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        super().__init__()
        self.image=pygame.image.load("C:\Aahana\Game Dev 2\lesson8\Things\pipe.png")
        self.index=0
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=x,y-180/2
        if pos==-1:
            self.rect.topleft=x,y+18/2
    def update(self): 
        self.rect.x-=5
        if self.rect.x<0:
            self.kill()         
bird=Flappy(100,375)
birdgroup=pygame.sprite.Group()
birdgroup.add (bird)
pipegroup=pygame.sprite.Group()
clock=pygame.time.Clock() 
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN and game_over==False and flying==False:
            flying=True
    screen.blit(bg,(0,0))
    screen.blit(ground,(ground_x,680))
    birdgroup.draw(screen)
    birdgroup.update()
    pipegroup.draw(screen)
    if bird.rect.bottom >680:
        game_over=True
        flying=False

    if game_over==False and flying==True:
        time_now=pygame.time.get_ticks()
        if time_now-last_pipe>pipe_freq:
            btm_pipe=Pipe(WIDTH,HEIGHT/2+random.randint(-100,100),-1)
            top_pipe=Pipe(WIDTH,HEIGHT/2+random.randint(-100,100),1)
            pipegroup.add(btm_pipe)
            pipegroup.add(top_pipe)
            last_pipe=time_now
        ground_x=ground_x-0.5
        if abs(ground_x)>35:
            ground_x=0
        pipegroup.update()

    pygame.display.update()
    #Homework:
#You can try out the animation for your own game with the collected images
#Build the score and display it on the screen
