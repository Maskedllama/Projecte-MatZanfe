import pygame
import pygame_menu
from InputBox import InputBox
from pygame import mixer

pygame.init()
# Variables
yousayrun = True
clock = pygame.time.Clock()
points= 0
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')

# Mida finestra i puja la imatge
surface = pygame.display.set_mode((600, 400))
imageaudio1 = pygame.image.load("ClickAudio1.png").convert()
# Detectar el clic del ratolí
image_position = (190, 70)
image_size = imageaudio1.get_rect().size

font = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption("Projecte MatZanfe")
input_box = InputBox(190, 250, 200, 32)
pygame.init()

#Funció principal
def start_the_game():
    menu.disable()
    surface.fill((255, 70, 90))

    # Aquí se genera la imagen
    surface.blit(imageaudio1, image_position)

    punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
    surface.blit(punts, (350, 30))
    titolsuma3 = font.render("Suma (3)", True, (0, 0, 0))
    surface.blit(titolsuma3, (10, 20))

    input_box.draw(surface)
    pygame.display.flip()

#Menú del joc (simplificat)
menu = pygame_menu.Menu('Demostració', 400, 300,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add.text_input('Usuari : ')
menu.add.button('Començar',start_the_game)
menu.add.button('Sortir', pygame_menu.events.EXIT)
menu.mainloop(surface)

while yousayrun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yousayrun = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # trobar posició del clic
            click = pygame.mouse.get_pos()
            # revisa si el clic és a la imatge
            if image_position[0] < click[0] < image_position[0] + image_size[0] and image_position[1] < click[1] < \
                    image_position[1] + image_size[1]:
                mixer.music.load("AudioSuma.wav")
                mixer.music.play(1)

        start_the_game()
        result = input_box.handle_event(event)
        if result != None:
            if int(result) == int(12):
                points = points + 5
        pygame.display.update()
