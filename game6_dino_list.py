# create animation list
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
pygame.display.set_caption('Alex game 6')

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()

BG = (50, 100, 50)
BLACK = (0, 0, 0)

animation_list = []
animation_steps = 8
last_update = pygame.time.get_ticks()

for i in range(animation_steps):
    animation_list.append(get_image(sprite_sheet_image, i, 24, 24, 3, BLACK))




frame_0 = get_image(sprite_sheet_image, 0, 24, 24, 3, BLACK)
frame_1 = get_image(sprite_sheet_image, 1, 24, 24, 3, BLACK)
frame_2 = get_image(sprite_sheet_image, 2, 24, 24, 3, BLACK)
frame_3 = get_image(sprite_sheet_image, 3, 24, 24, 3, BLACK)

run = True
while run:

	#update background
    # screen.blit(frame_0, (0,0))
    screen.fill(BG)
    screen.blit(frame_0, (0,0))
    screen.blit(frame_1, (60,0))
    screen.blit(frame_2, (120,0)) 
    screen.blit(frame_3, (180,0))

    for i in range(animation_steps):
        screen.blit(animation_list[i], (60*i + 30, 80))
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()