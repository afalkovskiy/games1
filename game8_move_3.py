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

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Alex game 8')

sprite_sheet_image = pygame.image.load('doux4.png').convert_alpha()

BG = (200, 255, 200)
BLACK = (0, 0, 0)

animation_list1 = []
animation_steps1 = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

for i in range(animation_steps1):
    animation_list1.append(get_image(sprite_sheet_image, i, 24, 24, 5, BLACK))




run = True
x=0
y=200
d=20
flag = True
while run:

	#update background
    # screen.blit(frame_0, (0,0))
    screen.fill(BG)
   

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        if x>SCREEN_WIDTH - 100 or x<0:
            d = d * (-1)
            if flag:
                flag = False
            else:
                flag = True
            # pygame.transform.rotate(animation_list[frame],180.)
            
        x = x + d

        if frame > len(animation_list1)-1:
            frame = 0

        last_update = current_time


    # print('frame = ', frame)
    if flag:    
        screen.blit(animation_list1[frame], (x,y))
    else:
        img=animation_list1[frame]
        img = pygame.transform.flip(surface=img, flip_x=True, flip_y=False)
        img.set_colorkey(BLACK)
        screen.blit(img, (x,y))
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()