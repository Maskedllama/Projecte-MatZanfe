import pygame
import pygame_menu
from InputBox import InputBox
from pygame import mixer
import random

pygame.init()
# Variables
yousayrun = True
clock = pygame.time.Clock()
pointz = 0
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.set_caption("Projecte MatZanfe")
font = pygame.font.SysFont('comicsans', 50)
running = True
points = 0
t = 60

# Determina la medida de la imagen y sube una foto
surface = pygame.display.set_mode((600, 400))
imageaudio1 = pygame.image.load("ClickAudio1.png").convert()
# Ésto detecta el click del ratón
image_position = (190, 70)
image_size = imageaudio1.get_rect().size
pygame.display.set_caption("Projecte MatZanfe")
input_box = InputBox(190, 250, 200, 32)
pygame.init()

def getnumbers3():
    x = random.randint(0, 6)
    y = random.randint(0, 6)
    is_correct = False
    return x, y

def display_the_game3(x, y):
    # Variables
    z = x + y
    surface.fill((70, 255, 70))
    text = font.render(str(x) + " * " + str(y), True, (255, 255, 255))
    menu.disable()
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    surface.blit(text, (260, 120))
    input_box.draw(surface)
    punts = font.render("Puntuació: " +  str(points),True, (255,255,255))
    surface.blit(punts, (350,30))
    titolmultiplicacio= font.render("Multiplicació (1)", True, (0, 0, 0))
    surface.blit(titolmultiplicacio, (10, 20))
    temps = font.render("Temps: " + str(t), True, (255, 255, 51))
    surface.blit(temps, (0, 360))

x, y = getnumbers3()



#Función principal del juego
def start_the_game():
    menu.disable()
    surface.fill((255, 70, 90))

    # Aquí se genera la imagen
    surface.blit(imageaudio1, image_position)

    punts = font.render("Puntuació: " + str(pointz), True, (255, 255, 255))
    surface.blit(punts, (350, 30))
    titolsuma3 = font.render("Suma (3)", True, (0, 0, 0))
    surface.blit(titolsuma3, (10, 20))

    input_box.draw(surface)
    pygame.display.flip()

#Menú del juego
menu = pygame_menu.Menu('Prueba', 400, 300,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add.text_input('Usuario : ')
menu.add.button('Empezar',start_the_game)
menu.add.button("Proves", getnumbers3, display_the_game3)
menu.add.button('Salir', pygame_menu.events.EXIT)
menu.mainloop(surface)

while yousayrun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # encuentras la posición del click
            click = pygame.mouse.get_pos()
            # revisas si el click fue en la imágen
            if image_position[0] < click[0] < image_position[0] + image_size[0] and image_position[1] < click[1] < \
                    image_position[1] + image_size[1]:
                mixer.music.load("ha-gay.wav")
                mixer.music.play(1)

        start_the_game()
        result = input_box.handle_event(event)
        if result != None:
            if int(result) == int(12):
                pointz = pointz + 5
        pygame.display.update()

while running:
    clock.tick(60)
    yousayrun = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.USEREVENT:
            t -= 1
            temps = font.render("Temps:" + str(t), True, (255, 255, 51))
            surface.blit(temps, (0, 360))
            pygame.display.flip()
            if t == 0:
                pygame.quit()
        else:
            result = input_box.handle_event(event)
            if result != None:
                if int(result) == int(x) * int(y):
                    points = points + 5
                    t = t + 5
                    mixer.music.load('StarPost.wav')
                    mixer.music.play(1)

                # create new random numbers
                x, y = getnumbers3()

                # reset input box (just create a new box)
                input_box = InputBox(190, 250, 200, 32)

    display_the_game3(x, y)
    pygame.display.update()