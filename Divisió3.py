import pygame
from InputBox import InputBox
from pygame import mixer

pygame.init()
# Variables
yousayrun = True
clock = pygame.time.Clock()
points = 0
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')

# Mida de la finestra i carrega imatge
surface = pygame.display.set_mode((600, 400))
imageaudio4 = pygame.image.load("ClickAudio4.png").convert()
# esto lo vas a necesitar para detectar el click
image_position = (190, 70)
image_size = imageaudio4.get_rect().size

font = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption("Projecte MatZanfe")
input_box = InputBox(190, 250, 200, 32)


def main():
    surface.fill((222, 184, 135))

    # Es genera la imatge
    surface.blit(imageaudio4, image_position)

    punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
    surface.blit(punts, (350, 30))
    titoldivisio3 = font.render("Divisió (3)", True, (0, 0, 0))
    surface.blit(titoldivisio3, (10, 20))

    input_box.draw(surface)
    pygame.display.flip()


# Main Loop
while yousayrun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yousayrun = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # encuentras la posición del click
            click = pygame.mouse.get_pos()
            # revisas si el click fue en la imágen
            if image_position[0] < click[0] < image_position[0] + image_size[0] and image_position[1] < click[1] < \
                    image_position[1] + image_size[1]:
                #Aquest àudio és el mateix que el de la suma, és provisional
                mixer.music.load("AudioDivisio.wav")
                mixer.music.play(1)

        main()
        result = input_box.handle_event(event)
        if result != None:
            if int(result) == int(6):
                points = points + 5
        pygame.display.update()

pygame.quit()