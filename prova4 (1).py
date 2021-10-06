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
        width=WINDOW_SIZE[0] * 0.75
    )
    main_menu.add.button('Jugar',jugar)
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
   

# -------------------------------------------------------------------------
# Variables Globals
# -------------------------------------------------------------------------
global clock
global main_menu
global surface
global font1,font2,font3

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






