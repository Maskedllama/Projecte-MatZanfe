# Import the required libraries
import pygame
import pygame_menu
import random
from InputBox import InputBox

from pygame import mixer

# Initialize pygame
pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Projecte MatZanfe")
#Logotip de la finestra
logotip = pygame.image.load("calculator.png")
pygame.display.set_icon(logotip)

font = pygame_menu.font.FONT_8BIT
font1 = pygame_menu.font.FONT_NEVIS
font2 = pygame_menu.font.FONT_BEBAS

def Sumes_infinites():
    # Variables:
    running = True
    # Temporitzador: 1000 significa un segon
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    # Tipografia  / complements InputBox
    font = pygame.font.SysFont('comicsans', 50)
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    color_active = pygame.Color('lightskyblue3')
    # Punts, temps inicial i bucle principal
    running = True
    points = 0
    t = 60
    def start_the_game():
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        is_correct = False
        return x, y
    def display_the_game(x, y):
        # Fons i mostra els valors en pantalla ( a més del signe matemàtic entremig)
        surface.fill((255, 70, 90))
        text = font.render(str(x) + "+" + str(y), True, (255, 255, 255))
        # Fa aparèixer el text a la InputBox
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        surface.blit(text, (260, 120))
        InputBox.draw(surface)
        # Fa aparèixer la puntació, el títol del nivell i el temps restant en pantalla
        punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
        surface.blit(punts, (350, 30))
        titolsuma = font.render("SUMA (1)", True, (0, 0, 0))
        surface.blit(titolsuma, (10, 20))
        temps = font.render("Temps: " + str(t), True, (255, 255, 51))
        surface.blit(temps, (0, 360))

    x, y = start_the_game()
    input_box = InputBox(190, 250, 200, 32)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                # Disminueix el temps cada segon
                t -= 1
                temps = font.render("Temps:" + str(t), True, (255, 255, 51))
                surface.blit(temps, (0, 360))
                pygame.display.flip()
                if t == 0:
                    # Si arriba a 0 el programa es tanca
                    pygame.display.quit()
                    pygame.quit()
            else:
                result = input_box.handle_event(event)
                if result != None:
                    # Si el resultat que es posa és el correcte, se li sumarà temps i sonarà un àudio
                    if int(result) == int(x) + int(y):
                        points = points + 5
                        t = t + 5
                        mixer.music.load('StarPost.wav')
                        mixer.music.play(1)
                    x, y = start_the_game()

                    # Reinicia la InputBox
                    input_box = InputBox(190, 250, 200, 32)


#Make menu Sumes
menu3 = pygame_menu.Menu('Sumes', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)

menu3.add.button('Sumes infinites', Sumes_infinites(), font_name = font1, font_color = 'green')
menu3.add.button('Sumes amb imatges', font_name = font1, font_color = 'blue')
menu3.add.button('Sumes dictades', font_name = font1,font_color = 'red')

#Make menu Restes
menu4 = pygame_menu.Menu('Restes', 600, 400,
                       theme=pygame_menu.themes.THEME_DEFAULT)

menu4.add.button('Restes infinites', font_name = font1, font_color = 'green')
menu4.add.button('Restes amb imatges', font_name = font1, font_color = 'blue')
menu4.add.button('Restes dictades', font_name = font1,font_color = 'red')

#Make menu Multiplicacions
menu5 = pygame_menu.Menu('Multiplicacions', 600, 400,
                       theme=pygame_menu.themes.THEME_ORANGE)

menu5.add.button('Multiplicacions infinites', font_name = font1, font_color = 'green')
menu5.add.button('Multiplicacions amb imatges', font_name = font1, font_color = 'blue')
menu5.add.button('Multiplicacions dictades', font_name = font1,font_color = 'red')

#Make menu Divisions
menu6 = pygame_menu.Menu('Divisions', 600, 400,
                       theme=pygame_menu.themes.THEME_GREEN)

menu6.add.button('Divisions infinites', font_name = font1, font_color = 'green')
menu6.add.button('Divisons amb imatges', font_name = font1, font_color = 'blue')
menu6.add.button('Divisions dictades', font_name = font1,font_color = 'red')

# Make menu 2
menu2 = pygame_menu.Menu('Selecció dels mòduls', 600, 400,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

menu2.add.button('Sumes',menu3, font_name = font2, font_color = 'green')
menu2.add.button('Restes',menu4, font_name = font2, font_color = 'blue')
menu2.add.button('Multiplicacions',menu5, font_name = font2,font_color = 'red')
menu2.add.button('Divisions',menu6, font_name = font2, font_color = 'purple' )

# Make main menu
menu = pygame_menu.Menu('Projecte MatZanfe', 600, 400,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

user_input = menu.add.text_input('Usuari: ', font_name = font1, font_color = 'blue')
age_input = menu.add.text_input('Edat: ', font_name = font1,font_color = 'Black')
menu.add.button('Comencem', menu2, font_name = font, font_color = 'green')
menu.add.button('Sortir', pygame_menu.events.EXIT, font_name = font,font_color = 'red')

# Run your menu
menu.mainloop(surface)
