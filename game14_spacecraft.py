# create animation
import pygame
import random

pygame.init()

def get_image(sheet, frame, width, height, scale, color1):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet,(0, 0), (frame*width, 0, 96, 96))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color1)  
    
    return image

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
# BG = (10, 10, 20)
BG = (50, 100, 50)
BG = (10, 10, 20)
BG = (0, 0, 0)
BG = pygame.image.load("bg.jpg")
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Alex game 14')

sprite_sheet_image = pygame.image.load('bat.png').convert_alpha()
sprite_sheet_image = pygame.image.load('bird.png').convert_alpha()
sprite_sheet_image = pygame.image.load('spacecraft2.png').convert_alpha()
sprite_star_image = pygame.image.load('star.png').convert_alpha()
sprite_star_image.set_colorkey(BLACK)



animation_list = []
animation_steps = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

for i in range(animation_steps):
    # animation_list.append(get_image(sprite_sheet_image, i, 24, 24, 3, BLACK))
    animation_list.append(get_image(sprite_sheet_image, i, 96, 96, 1, BLACK))


run = True
x=0
y=200
d=20
x1=10
y1=0
dx1=30
dy1=40
flag = True
nhits = 0
while run:

	#update background
    # screen.blit(frame_0, (0,0))
    # screen.fill(BG)
    screen.blit(BG, (0,0))
    w1=24
    h1=24
    s1=1
    star1 = sprite_star_image
    star1 = pygame.transform.scale(star1, (w1 * s1, h1 * s1))
    star1.set_colorkey(BLACK)


    txt = "Number of hits: " + str(nhits)
    text_surface = my_font.render(txt, False, (250, 250, 250))
    screen.blit(text_surface, (0,0))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        if x>380:
            flag = False
        if x<0:
            flag = True
            # pygame.transform.rotate(animation_list[frame],180.)
        
        if flag==True:
            x = x + d
        else:
            x = x -d       

        if frame > len(animation_list)-1:
            frame = 0

        x1 = x1 + dx1
        y1 = y1 + dy1
        s1 = 3
        if abs(x-x1)<50 and abs (y-y1)<50:
            nhits = nhits + 1
            s1 = 10

        if y1 > 500 or x1 > 500 or x1 < 0:
            y1 = 0
            x1 = random.randint(50, 450)
            dx1 = random.randint(-20, 20)


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
            y = 200    
            if event.key == pygame.K_UP:
                y = 150
            if event.key == pygame.K_DOWN:
                y = 250                 

    star1 = pygame.transform.scale(star1, (w1 * s1, h1 * s1))
    star1.set_colorkey(BLACK)
    screen.blit(star1, (x1,y1))

    pygame.display.update()

pygame.quit()