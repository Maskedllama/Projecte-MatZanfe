# Import the required libraries
import pygame
import pygame_menu
from pygame import mixer
import random
from InputBox import InputBox


# Constants
WINDOW_SIZE = WIDTH, HEIGHT = 800, 600

def creamenus(surface):
    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        title='Projecte MatZanfe',
        width=WINDOW_SIZE[0] * 0.75,
        theme = pygame_menu.themes.THEME_SOLARIZED
    )
    main_menu.add.button('Jugar',jugar)
    main_menu.add.button('Jugar a àudios', jugaraudios)
    main_menu.add.button('Sortir', pygame_menu.events.EXIT)
    return main_menu

def jugar():

    #Assigna dos valors a x i y
    def start_the_game():
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        is_correct = False
        return x, y

    #Fa aparèixer diverses coses en pantalla
    def display_the_game(x, y):
        #Fons i mostra els valors en pantalla ( a més del signe matemàtic entremig)
        surface.fill((255, 70, 90))
        text = font.render(str(x) + "+" + str(y), True, (255, 255, 255))
        #Fa aparèixer el text a la InputBox
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        surface.blit(text, (260, 120))
        input_box.draw(surface)
        #Fa aparèixer la puntació, el títol del nivell i el temps restant en pantalla
        punts = font.render("Puntuació: " +  str(points),True, (255,255,255))
        surface.blit(punts, (350,30))
        titolsuma = font.render("SUMA (1)", True, (0,0,0))
        surface.blit(titolsuma,(10,20))
        temps = font.render("Temps: " + str(t),True, (255,255,51))
        surface.blit(temps,(0,360))

    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('comicsans', 50)
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    color_active = pygame.Color('lightskyblue3')
    #Punts, temps inicial i bucle principal
    running = True
    points = 0
    t = 15

    #Assigna els valors de x i y a la funció un altre cop (per generar nous números)
    x, y = start_the_game()
    input_box = InputBox(190, 250, 200, 32)

    #Main loop
    while running:
        # Pass events to main_menu
        if main_menu.is_enabled():
            main_menu.update(events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                #Disminueix el temps cada segon
                t -= 1
                temps = font.render("Temps:" + str(t), True, (255, 255, 51))
                surface.blit(temps, (0, 360))
                pygame.display.flip()
                if t == 0:
                    #Si arriba a 0 el programa es tanca
                    main_menu.enable()
                    return
            else:
                result = input_box.handle_event(event)
                if result != None:
                    #Si el resultat que es posa és el correcte, se li sumarà temps i sonarà un àudio
                    if int(result) == int(x) + int(y):
                        points = points + 5
                        t = t + 5
                        #mixer.music.load('StarPost.wav')
                        #mixer.music.play(1)

                    # Crea nous números
                    x, y = start_the_game()

                    # Reinicia la InputBox
                    input_box = InputBox(190, 250, 200, 32)


        display_the_game(x, y)
        pygame.display.update()
   
def jugaraudios():
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

    clock = pygame.time.Clock()
    imageaudio1 = pygame.image.load("ClickAudio1.png").convert()
    # Assigna quina és la posició de la imatge
    image_position = (190, 70)
    image_size = imageaudio1.get_rect().size
    # Quina és la tipografia, títol de la finestra i posiciona la InputBox
    font = pygame.font.SysFont('comicsans', 50)
    input_box = InputBox(190, 250, 200, 32)
    yousayrun = True
    points = 0

    # Main Loop
    while yousayrun:
        if main_menu.is_enabled():
            main_menu.update(events)
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
                    # Si la imatge ha estat clicada, sonarà un àudio
                    # els altres nivells tenen el mateix àudio (simplement perquè encara no els he gravat)
                    mixer.music.load("AudioSuma.wav")
                    mixer.music.play(1)
            result = input_box.handle_event(event)
            if result != None:
                # Si la resposta és correcta se li sumarà 5 punts
                if int(result) == int(12):
                    points = points + 5
        main3()
        pygame.display.update()

# -------------------------------------------------------------------------
# Variables Globals
# -------------------------------------------------------------------------
global clock
global main_menu
global surface
global font1,font2,font3
global points

pygame.init()
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Projecte MatZanfe")
#Logotip de la finestra
logotip = pygame.image.load("calculator.png")
pygame.display.set_icon(logotip)
font = pygame_menu.font.FONT_8BIT
font1 = pygame_menu.font.FONT_NEVIS
font2 = pygame_menu.font.FONT_BEBAS

main_menu=creamenus(surface)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Main menu
    if main_menu.is_enabled():
        main_menu.mainloop(surface)






