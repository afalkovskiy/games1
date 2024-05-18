import pygame

from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

pygame.init()


# Main function
def main():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500

    #load sounds
    sound1 = pygame.mixer.Sound('img/ts_hammertime.wav')   
    sound1.set_volume(0.8)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('My game')

    BG = (255, 165, 50)
    BLACK = (0, 0, 0)

    run = True
    while run:
        sound1.play()
        #update background
        screen.fill(BG)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()