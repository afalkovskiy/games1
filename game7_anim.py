# create animation
import pygame

pygame.init()

def get_image(sheet, frame, width, height, scale, color1):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet,(0, 0), (frame*width, 0, 24, 24))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color1)
    return image

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Alex game 7')

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()

BG = (200, 255, 200)
BLACK = (0, 0, 0)

animation_list = []
animation_steps = 24
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0

for i in range(animation_steps):
    animation_list.append(get_image(sprite_sheet_image, i, 24, 24, 4, BLACK))




run = True
while run:

	#update background
    # screen.blit(frame_0, (0,0))
    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        if frame > len(animation_list)-1:
            frame = 0

        last_update = current_time


    print('frame = ', frame)
    screen.blit(animation_list[frame], (0,0))

    # for i in range(animation_steps):
    #     screen.blit(animation_list[i], (60*i + 30, 80))
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()