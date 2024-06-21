# create animation
import pygame

from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

def get_image(sheet, frame, width, height, scale, color1):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet,(0, 0), (frame*width, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color1)
    # image = pygame.transform.flip(surface=image, flip_x=True, flip_y=False)
      
    return image

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BLACK = (0, 0, 0)

#load sounds
sound1 = pygame.mixer.Sound('img/ts_hammertime.wav') 
sound2 = pygame.mixer.Sound('img/bodyhit1.wav') 
# sound1 = pygame.mixer.Sound('img/cricketb.wav')  
sound1.set_volume(0.4)
sound2.set_volume(0.)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fire Jumper 11')

sprite_sheet_image = pygame.image.load('img/doux4.png').convert_alpha()
sprite_sheet_flame = pygame.image.load('img/flame_48x48_7.png').convert_alpha()
# sprite_sheet_flame = pygame.image.load('img/fire_24x24_4.png').convert_alpha()
# sprite_sheet_flame = pygame.image.load('img/flamegiffer.png').convert_alpha() #to remove
# sprite_sheet_flame = pygame.image.load('img/flamegiffer96x96_19.png').convert_alpha()
sprite_sheet_blust = pygame.image.load('img/blust4.png').convert_alpha()

BG = (200, 255, 200)
bg_img = pygame.image.load("img/bg2.png")
# rock_img = pygame.image.load("img/flame_48x48.png").convert_alpha()
# rock_img = pygame.transform.scale(rock_img, (120,120))
# rock_img.set_colorkey(BLACK)

animation_list1 = []
animation_steps1 = 4
animation_list2 = []
animation_steps2 = 10
# to add animation_steps3 - blust
animation_list3 = []
animation_steps3 = 3

animation_list6 = []
animation_steps6 = 4

last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

action = 1

for i in range(animation_steps1):
    animation_list1.append(get_image(sprite_sheet_image, i, 24, 24, 5, BLACK))

for i in range(5,15):
    animation_list2.append(get_image(sprite_sheet_image, i, 24, 24, 5, BLACK))

# to add animatio_list3 - jump, ...list4 - quick run  

for i in range(animation_steps6):
    # animation_list6.append(get_image(sprite_sheet_flame, i, 96, 96, 1, BLACK))
    animation_list6.append(get_image(sprite_sheet_flame, i, 48, 48, 3, BLACK))
    # animation_list6.append(get_image(sprite_sheet_flame, i, 24, 24, 5, BLACK))

for i in range(animation_steps3):
    animation_list3.append(get_image(sprite_sheet_blust, i, 96, 96, 1, BLACK))    

run = True
x=0
y=200
d=20
dy=0

xRect = 200
yRect = 230
flag = True

njumps = 0
nfails = 0

while run:
    sound1.play()
    sound2.play()
    # screen.fill(BG)
    screen.blit(bg_img, (0,0))
    # screen.blit(rock_img, (xRect,yRect-20))
    screen.blit(animation_list6[frame%animation_steps6], (xRect,yRect-40))
    txt = "Number of jumps: " + str(njumps) + "  fails: " + str(nfails)
    text_surface = my_font.render(txt, False, (0, 0, 250))
    screen.blit(text_surface, (0,0))

    if action==1:
        animation_list =  animation_list1
        animation_cooldown = 200 
        d=20

    if action == 2:
        animation_list =  animation_list2
        animation_cooldown = 100
        d=30

    if abs(x - xRect) < 60 and abs(y - yRect) < 40:
            # d = 0
            animation_list =  animation_list3
            sound1.fadeout(1)
            sound2.play()
            sound2.set_volume(0.6)
    else:
        sound1.set_volume(0.4)
        sound2.fadeout(1)            

    # pygame.draw.rect(screen, (0,100,0), pygame.Rect(xRect, yRect, 60, 60))
   
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        if x>SCREEN_WIDTH-50:
            flag = False
        if x<0:
            flag = True
            # pygame.transform.rotate(animation_list[frame],180.)
        
        if flag==True:
            x = x + d
        else:
            x = x -d   

        if abs(x - xRect) < 60 and abs(y - yRect) < 40:
            # d = 0
            animation_list =  animation_list3
            nfails = nfails + 1
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

        last_update = current_time

    # print("len anim list = ", len(animation_list))
    if frame > len(animation_list)-1:
        frame = 0

    # print('frame = ', frame)
    if flag:    
        screen.blit(animation_list[frame], (x,y))
    else:
        img=animation_list[frame]
        img = pygame.transform.flip(surface=img, flip_x=True, flip_y=False)
        img.set_colorkey(BLACK)
        screen.blit(img, (x,y))
	
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
                njumps +=1   
            if event.key == pygame.K_r:
                action = 2
                frame = 0
            if event.key == pygame.K_w:
                action = 1
                frame = 0                       

    pygame.display.update()

pygame.quit()