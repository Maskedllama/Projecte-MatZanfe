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

# Mida de la imatge i assigna la imatge
surface = pygame.display.set_mode((600, 400))
imageaudio1 = pygame.image.load("ClickAudio1.png").convert()
# Assigna quina és la posició de la imatge
image_position = (190, 70)
image_size = imageaudio1.get_rect().size
#Quina és la tipografia, títol de la finestra i posiciona la InputBox
font = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption("Projecte MatZanfe")
input_box = InputBox(190, 250, 200, 32)


def main3():
    surface.fill((255, 70, 90))

    # Aquí se genera la imagen
    surface.blit(imageaudio1, image_position)

    punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
    surface.blit(punts, (350, 30))
    titolsuma3 = font.render("Suma (3)", True, (0, 0, 0))
    surface.blit(titolsuma3, (10, 20))

    input_box.draw(surface)
    pygame.display.flip()


# Main Loop
while yousayrun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yousayrun = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # troba la posició del clic
            click = pygame.mouse.get_pos()
            # es revisa si el clic ha estat a la imatge
            if image_position[0] < click[0] < image_position[0] + image_size[0] and image_position[1] < click[1] < \
                    image_position[1] + image_size[1]:
                #Si la imatge ha estat clicada, sonarà un àudio
                #els altres nivells tenen el mateix àudio (simplement perquè encara no els he gravat)
                mixer.music.load("AudioSuma.wav")
                mixer.music.play(1)

        main3()
        result = input_box.handle_event(event)
        if result != None:
            #Si la resposta és correcta se li sumarà 5 punts
            if int(result) == int(12):
                points = points + 5
        pygame.display.update()

pygame.quit()