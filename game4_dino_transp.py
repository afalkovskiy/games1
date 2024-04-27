# show one frame whith scale transparency
import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Alex game 4')

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()

BG = (50, 100, 50)
BLACK = (0, 0, 0)

def get_image(sheet, width, height, scale, color1):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet,(0, 0), (0, 0, 24, 24))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color1)
    return image

frame_0 = get_image(sprite_sheet_image, 24, 24, 3, BLACK)
run = True
while run:

	#update background
    # screen.blit(frame_0, (0,0))
    screen.fill(BG)
    screen.blit(frame_0, (0,0))
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()