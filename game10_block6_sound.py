# create animation
import pygame
import random
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

def get_image(sheet, frame, width, height, scale, color1):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet,(0, 0), (frame*width, 0, 24, 24))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color1)
    # image = pygame.transform.flip(surface=image, flip_x=True, flip_y=False)
    
    return image

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

#load sounds
# 
sound1 = pygame.mixer.Sound('img/ts_hammertime.wav')   
sound1.set_volume(0.8)
sound2 = pygame.mixer.Sound('img/bodyhit1.wav')   
sound2.set_volume(0.0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Alex game 10-6')

sprite_sheet_image = pygame.image.load('img/doux4.png').convert_alpha()

BG = (200, 255, 200)
BLACK = (0, 0, 0)

animation_list = []
animation_steps = 30
animation_steps = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

for i in range(animation_steps):
    animation_list.append(get_image(sprite_sheet_image, i, 24, 24, 5, BLACK))


run = True
x=0
y=200
d=20

xRect = 200
xRect = random.randint(50, 300)
yRect = 220
flag = True
flagStop = False

score = 0



while run:

    screen.fill(BG)
    sound1.play()
    sound2.play(loops=-1, maxtime=2000)
    
    text_font = pygame.font.SysFont(None, 30, bold=True)
    draw_text("Score: " + str(score), text_font, (100,100,100), 10, 10)

    pygame.draw.rect(screen, (0,100,0), pygame.Rect(xRect, yRect, 100, 80))
    pygame.draw.rect(screen, (0,100,0), pygame.Rect(0, 300, SCREEN_WIDTH, 10))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        if x>SCREEN_WIDTH - 120:
            flag = False
            xRect = random.randint(50, SCREEN_WIDTH - 200)
        if x<0:
            flag = True
            xRect = random.randint(50, SCREEN_WIDTH - 200)
            # pygame.transform.rotate(animation_list[frame],180.)
        
        xCorr = 0
        if flag==True:
            x = x + d
            xCorr = 10
        else:
            xCorr = -10
            x = x -d   

        if abs(x - xRect) < 90 + xCorr and abs(y - yRect) < 40:
            d = 0
            flagStop = True
            sound1.set_volume(0.0)
            sound2.set_volume(0.8)
        else:
            d = 20

        if abs(x - xRect) >= 90 - xCorr and abs(y - yRect) >= 40:
            d = 20
            y = 200
            if flagStop == True:
                flagStop = False
                score = score + 1
                sound1.set_volume(0.8)
                sound2.set_volume(0.0)
         

        if frame > len(animation_list)-1:
            frame = 0

        last_update = current_time


    # print('frame = ', frame)
    if flag:    
        screen.blit(animation_list[frame], (x,y))
    else:
        img=animation_list[frame]
        img = pygame.transform.flip(surface=img, flip_x=True, flip_y=False)
        img.set_colorkey(BLACK)
        screen.blit(img, (x,y))
        #image = pygame.transform.flip(surface=image, flip_x=True, flip_y=False)

    # for i in range(animation_steps):
    #     screen.blit(animation_list[i], (60*i + 30, 80))
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flag = False
            if event.key == pygame.K_RIGHT:
                flag = True
            if event.key == pygame.K_UP:
                y = 120    

    if y==120:
        sound1.set_volume(0.2)                    

    pygame.display.update()

pygame.quit()