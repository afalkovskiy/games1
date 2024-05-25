# create animation
import pygame

pygame.init()

def get_image(sheet, frame, width, height, scale, color1):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet,(0, 0), (frame*width, 0, 24, 24))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color1)
    # image = pygame.transform.flip(surface=image, flip_x=True, flip_y=False)
    
    
    return image

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Alex game anim list4')

sprite_sheet_image = pygame.image.load('img/doux4.png').convert_alpha()

BG = (200, 255, 200)
BLACK = (0, 0, 0)

animation_list1 = []
animation_steps = 30
animation_steps1 = 4
animation_list2 = []
animation_steps2 = 10

animation_list5 = []
animation_steps5 = 6
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

for i in range(animation_steps1):
    animation_list1.append(get_image(sprite_sheet_image, i, 24, 24, 5, BLACK))

for i in range(5,15):
    animation_list2.append(get_image(sprite_sheet_image, i, 24, 24, 5, BLACK))

for i in range(25,31):
    animation_list5.append(get_image(sprite_sheet_image, i, 24, 24, 5, BLACK))    

run = True
x=0
y=200
d=20
dy=0

xRect = 200
yRect = 230
flag = True
flagRun = False
flagSummersault = False



while run:

    screen.fill(BG)
    if flagRun == True:
        animation_list =  animation_list2
        animation_cooldown = 100

    if flagRun == False:
        animation_list =  animation_list1
        animation_cooldown = 200 

    if flagSummersault == True:
        animation_list =  animation_list5
        animation_cooldown = 200         

    pygame.draw.rect(screen, (0,100,0), pygame.Rect(xRect, yRect, 60, 60))
   
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

        if abs(x - xRect) < 60 and abs(y - yRect) < 40:
            d = 0
        else:
            d = 20

        y = y + dy      

        if y >=200:
            y = 200
            dy = 0

        if abs(x - xRect) >= 60 and abs(y - yRect) >= 40:
            d = 20
            # y = 200
            dy = 20

         

        print("len anim list = ", len(animation_list))
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
            if event.key == pygame.K_r:
                flagRun = True
                frame = 0
            if event.key == pygame.K_w:
                flagRun = False
                frame = 0 
            if event.key == pygame.K_s:
                flagSummersault = True
                flagRun = False
                frame = 0                        

    pygame.display.update()

pygame.quit()