# Import the required libraries
import pygame
import pygame_menu
from pygame import mixer
import random
from InputBox import InputBox
import time

# Constants
WINDOW_SIZE = WIDTH, HEIGHT = 600, 400

#Funció que crearà el menú principal del programa.
# Aquí s'estableix la mida, el títol i els colors.
def creamenus(surface):
    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        title='Projecte MatZanfe',
        width=WINDOW_SIZE[0],
        theme = pygame_menu.themes.THEME_SOLARIZED
    )
    #En aquest apartat, el que es farà és crear diversos botons.
    #Cadascun d'ells faran una funcionalitat.
    main_menu.add.text_input('Usuari: ', font_name = font1, font_color = 'blue')
    main_menu.add.text_input('Edat: ', font_name = font1, font_color ='black')
    main_menu.add.button('Jugar a sumes',jugar,"SUMA")
    main_menu.add.button('Jugar a multiplicacions',jugar,"MULTIPLICACIO")
    main_menu.add.button('Jugar a restes', jugar, "RESTA")
    main_menu.add.button('Jugar a àudios', jugaraudios)
    main_menu.add.button('Jugar amb imatges', jugarimatges)
    main_menu.add.button('Sortir',pygame_menu.events.EXIT, font_name = font, font_color = "red",)
    return main_menu

#A la següent funció, s'hi designa el procès que seguirà el programa per a realitzar els
#nivells infinits.
def jugar(operacio):
    #Assigna dos valors a x i y
    def start_the_game():
        x = random.randint(5, 10)
        y = random.randint(0, 5)
        is_correct = False
        return x, y

    #Fa aparèixer diverses coses en pantalla
    def display_the_game(x, y):
        #Fons i mostra els valors en pantalla ( a més del signe matemàtic entremig)
        surface.fill((255, 70, 90))
        #En comptes de crear una nova funció per a cada operació,
        #això fa canviar el títol i el signe que apareix en pantalla.
        if operacio=="SUMA":
            op="+"
            surface.fill((255,70,90))
        if operacio=="MULTIPLICACIO":
            op="x"
            surface.fill((70,255,70))
        if operacio=="RESTA":
            op="-"
            surface.fill((70,90,255))
        if operacio=="DIVISIO":
            op="/"
            surface.fill((222,184,135))

        #Fa aparèixer els números aleatoris en pantalla.
        text = font.render(str(x) + op + str(y), True, (255, 255, 255))
        #Fa aparèixer el text a la InputBox
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        surface.blit(text, (260, 120))
        input_box.draw(surface)
        #Fa aparèixer la puntació, el títol del nivell i el temps restant en pantalla
        punts = font.render("Puntuació: " +  str(points),True, (255,255,255))
        surface.blit(punts, (350,30))
        titolsuma = font.render(operacio, True, (0,0,0))
        surface.blit(titolsuma,(10,20))
        temps = font.render("Temps: " + str(t),True, (255,255,51))
        surface.blit(temps,(0,360))
    #El codi següent ensenya el temporitzador, i altres variables ja explicades.
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('comicsans', 50)
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    color_active = pygame.Color('lightskyblue3')
    #Punts, temps inicial i bucle principal
    running = True
    global pointsgeneral
    points=pointsgeneral
    t = 15

    #Assigna els valors de x i y a la funció un altre cop (per generar nous números)
    x, y = start_the_game()
    input_box = InputBox(190, 250, 200, 32)

    #Main loop
    while running:
        # Porta els esdeveniments al menú principal
        if main_menu.is_enabled():
            main_menu.update(events)
            clock.tick(60)
        #Aquest apartat és esencial.
        #Determina els diferents esdeveniments del programa.
        for event in pygame.event.get():
            #Si l'usuari apreta la x, tornarà al menú.
            if event.type == pygame.QUIT:
                running = False
            #Aquí es parla de tots els esdeveniments connectats
            #amb l'usuari.
            if event.type == pygame.USEREVENT:
                #Disminueix el temps cada segon
                t -= 1
                temps = font.render("Temps:" + str(t), True, (255, 255, 51))
                surface.blit(temps, (0, 360))
                pygame.display.flip()
                if t == 0:
                    #Si arriba a 0 el nivell es tanca
                    pointsgeneral=pointsgeneral + points
                    main_menu.enable()
                    return
            else:
                #Permet l'entrada de dades a la caixeta
                result = input_box.handle_event(event)
                if result != None:
                    #Si s'ha escollit fer una suma, l'enunciat tindrà el símbol "+"
                    if operacio=="SUMA":
                        resultat= int(x) + int(y)
                    #Si s'ha escollit fer una multiplicació, l'enunciat tindrà el símbol "*"
                    if operacio=="MULTIPLICACIO":
                        resultat= int(x) * int(y)
                    #Si s'ha escollit fer una resta, l'enunciat tindrà el símbol "-"
                    if operacio=="RESTA":
                        resultat = int(x) - int(y)
                    #Si s'ha escollit fer una divisió, l'enunciat tindrà el símbol "/"
                    if operacio=="DIVISIO":
                        resultat = int(x) / int(y)

                    #Si el resultat que s'ha introduit és el mateix que el correcte,
                    #es sumarà 5 punts a la puntuació del jugador i al temps del nivell
                    if int(result) == resultat:
                        points = points + 5
                        t = t + 5
                        #S'escoltarà música
                        #mixer.music.load('StarPost.wav')
                        #mixer.music.play(1)

                    # Crea nous números
                    x, y = start_the_game()

                    # Reinicia la InputBox
                    input_box = InputBox(190, 250, 200, 32)

        #Posiciona x/y en pantalla i l'actualitza perquè sorti efecte
        display_the_game(x, y)
        pygame.display.update()
    
def jugarimatges():
    corrent = True
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    points = 0
    # Variables InputBox
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    color_active = pygame.Color('lightskyblue3')
    input_box = InputBox(190, 250, 200, 32)
    global pointsgeneral
    points = pointsgeneral
    t = 15
    font = pygame.font.SysFont('comicsans', 50)
    def main2():

        # Mida de la finestra i es carrega la imatge
        imagefruit1 = pygame.image.load("FotoPera.png").convert()
        signesuma = pygame.image.load("Fotosuma.png").convert()

        # Tipografia, títol i entrada de respostes
        font = pygame.font.SysFont('comicsans', 50)
        # Fons
        surface.fill((255, 70, 90))

        # Aquí es genera les imatges, títols i puntuació
        surface.blit(imagefruit1, (30, 120))
        surface.blit(imagefruit1, (120, 120))
        surface.blit(signesuma, (250, 120))
        surface.blit(imagefruit1, (340, 120))
        surface.blit(imagefruit1, (440, 120))

        punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
        surface.blit(punts, (350, 30))
        titolsuma2 = font.render("Suma (2)", True, (0, 0, 0))
        surface.blit(titolsuma2, (10, 20))
        temps = font.render("Temps: " + str(t), True, (255, 255, 51))
        surface.blit(temps, (0, 360))
        # Es genera la inputbox i s'actualitza la pantalla
        input_box.draw(surface)
        pygame.display.flip()

     # Main Loop

    while corrent:
        if main_menu.is_enabled():
            main_menu.update(events)
            clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corrent = False
            if event.type == pygame.USEREVENT:
                #Disminueix el temps cada segon
                t -= 1
                temps = font.render("Temps:" + str(t), True, (255, 255, 51))
                surface.blit(temps, (0, 360))
                pygame.display.flip()
                if t == 0:
                    #Si arriba a 0 el programa es tanca
                    pointsgeneral=pointsgeneral + points
                    main_menu.enable()
                    return
            result = input_box.handle_event(event)
            if result != None:
                if int(result) == int(4):
                    points = points + 5
        main2()
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
        temps = font.render("Temps: " + str(t),True, (255,255,51))
        surface.blit(temps,(0,360))

        input_box.draw(surface)
        pygame.display.flip()

    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    imageaudio1 = pygame.image.load("ClickAudio1.png").convert()
    # Assigna quina és la posició de la imatge
    image_position = (190, 70)
    image_size = imageaudio1.get_rect().size
    # Quina és la tipografia, títol de la finestra i posiciona la InputBox
    font = pygame.font.SysFont('comicsans', 50)
    input_box = InputBox(190, 250, 200, 32)
    yousayrun = True
    global pointsgeneral
    points=pointsgeneral
    t = 15

    
    # Main Loop
    while yousayrun:
        if main_menu.is_enabled():
            main_menu.update(events)
            clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                yousayrun = False
            if event.type == pygame.USEREVENT:
                #Disminueix el temps cada segon
                t -= 1
                temps = font.render("Temps:" + str(t), True, (255, 255, 51))
                surface.blit(temps, (0, 360))
                pygame.display.flip()
                if t == 0:
                    #Si arriba a 0 el programa es tanca
                    pointsgeneral=pointsgeneral + points
                    main_menu.enable()
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # troba la posició del clic
                click = pygame.mouse.get_pos()
                # es revisa si el clic ha estat a la imatge
                if image_position[0] < click[0] < image_position[0] + image_size[0] and image_position[1] < click[1] < \
                        image_position[1] + image_size[1]:
                    # Si la imatge ha estat clicada, sonarà un àudio
                    # els altres nivells tenen el mateix àudio (simplement perquè encara no els he gravat)
                    # mixer.music.load("AudioSuma.wav")
                    # mixer.music.play(1)
                    a=1
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
pointsgeneral=0


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






