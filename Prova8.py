# Import the required libraries
import pygame
import pygame_menu
from pygame import mixer
import random
from InputBox import InputBox
import time

# Constants
WINDOW_SIZE = WIDTH, HEIGHT = 700, 500

#Funció que crearà el menú principal del programa.
# Aquí s'estableix la mida, el títol i els colors.
def creamenus(surface):
    """main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        title='Projecte MatZanfe',
        width=WINDOW_SIZE[0],
        theme = pygame_menu.themes.THEME_SOLARIZED
    )"""

    # Make menu Sumes
    menu3 = pygame_menu.Menu('Sumes', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_BLUE)

    menu3.add.button('Sumes infinites',jugar,"SUMA", font_name=font1, font_color='green')
    menu3.add.button('Sumes amb imatges',jugarimatges, "SUMA",font_name=font1, font_color='blue')
    menu3.add.button('Sumes dictades', jugaraudios, font_name=font1, font_color='red')

    # Make menu Restes
    menu4 = pygame_menu.Menu('Restes', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_DEFAULT)

    menu4.add.button('Restes infinites',jugar,"RESTA", font_name=font1, font_color='green')
    menu4.add.button('Restes amb imatges', jugarimatges, "RESTA", font_name=font1, font_color='blue')
    menu4.add.button('Restes dictades', font_name=font1, font_color='red')

    # Make menu Multiplicacions
    menu5 = pygame_menu.Menu('Multiplicacions', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_ORANGE)

    menu5.add.button('Multiplicacions infinites',jugar,"MULTIPLICACIO", font_name=font1, font_color='green')
    menu5.add.button('Multiplicacions amb imatges', jugarimatges, "MULTIPLICACIO", font_name=font1, font_color='blue')
    menu5.add.button('Multiplicacions dictades', font_name=font1, font_color='black')

    # Make menu Divisions
    menu6 = pygame_menu.Menu('Divisions', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_GREEN)

    menu6.add.button('Divisions infinites',jugar,"DIVISIO", font_name=font1, font_color='yellow')
    menu6.add.button('Divisons amb imatges', jugarimatges, "DIVISIO", font_name=font1, font_color='blue')
    menu6.add.button('Divisions dictades', font_name=font1, font_color='red')

    # Make menu 2
    menu2 = pygame_menu.Menu('Selecció dels mòduls', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_SOLARIZED)

    # msele = mixer.music.load('LevelSelector.wav')
    # msele2 = mixer.music.play(-1)
    menu2.add.button('Sumes', menu3, font_name=font2, font_color='green')
    menu2.add.button('Restes', menu4, font_name=font2, font_color='blue')
    menu2.add.button('Multiplicacions', menu5, font_name=font2, font_color='red')
    menu2.add.button('Divisions', menu6, font_name=font2, font_color='purple')

    # Make main menu
    main_menu = pygame_menu.Menu('Projecte MatZanfe', WINDOW_SIZE[0], WINDOW_SIZE[1],
                            theme=pygame_menu.themes.THEME_SOLARIZED)

    user_input = main_menu.add.text_input('Usuari: ', font_name=font1, font_color='blue')
    #mixer.music.load('MusicaMenu.wav')
    #mixer.music.play(-1)
    age_input = main_menu.add.text_input('Edat: ', font_name=font1, font_color='Black')
    main_menu.add.button('Comencem', menu2, font_name=font, font_color='green')
    main_menu.add.button('Sortir', pygame_menu.events.EXIT, font_name=font, font_color='red')

    return main_menu

#Assigna dos valors a x i y
def start_the_game(operacio,maxnum):
    if (operacio=='RESTA'):
        x = random.randint(int(maxnum/2), maxnum)
        y = random.randint(0, int(maxnum/2))
        is_correct = False
    if (operacio=='SUMA'):
        x = random.randint(0, maxnum)
        y = random.randint(0, maxnum)
        is_correct = False
    if (operacio=='MULTIPLICACIO'):
        x = random.randint(0,maxnum)
        y = random.randint(0,2)
        is_correct = False
    if (operacio=='DIVISIO'):
        x = random.randint(1, maxnum)
        y = random.randint(1, maxnum)
        while (x/y != int(x/y)):
            x = random.randint(1, maxnum)
            y = random.randint(1, maxnum)
    return x, y

#A la següent funció, s'hi designa el procès que seguirà el programa per a realitzar els
#nivells infinits.
def jugar(poperacio):
    #Fa aparèixer diverses coses en pantalla
    def display_the_game(x, y):
        #Fons i mostra els valors en pantalla ( a més del signe matemàtic entremig)
        surface.fill((255, 70, 90))
        #En comptes de crear una nova funció per a cada operació,
        #això fa canviar el títol i el signe que apareix en pantalla.
        if operacio=="SUMA":
            titol = "Suma (1)"
            op="+"
            surface.fill((255, 70, 90))
        if operacio=="MULTIPLICACIO":
            titol = "Multiplicació (1)"
            op="x"
            surface.fill((70, 255, 70))
        if operacio=="RESTA":
            titol = "Resta (1)"
            op="-"
            surface.fill((70, 90, 255))
        if operacio=='DIVISIO':
            titol = "Divisió (1)"
            op = "/"
            surface.fill((222, 184, 135))

        #Fa aparèixer els números aleatoris en pantalla.
        text = font.render(str(x) + op + str(y), True, (255, 255, 255))
        #Fa aparèixer el text a la InputBox
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        surface.blit(text, (260, 120))
        input_box.draw(surface)
        #Fa aparèixer la puntació, el títol del nivell i el temps restant en pantalla
        punts = font.render("Puntuació: " +  str(points),True, (255,255,255))
        surface.blit(punts, (350,30))
        titolsuma = font.render(titol, True, (0,0,0))
        surface.blit(titolsuma,(10,20))
        temps = font.render("Temps: " + str(t),True, (255,255,51))
        surface.blit(temps,(0,420))
  
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
    if (poperacio=='RANDOM'):
        x=random.randint(0, 2)
        operacio=opernoms[x]
    else:
        operacio=poperacio
    x, y = start_the_game(operacio,10)
    input_box = InputBox(190, 250, 200, 32)


    #Main loop
    while running:
        # Porta els esdeveniments al menú principal
        if main_menu.is_enabled():
            main_menu.update(events)
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

                    #Aquesta part del codi va destinada a la creació
                    #del nivell "random", que les operacions van canviant per cada resposta
                    if (poperacio=='RANDOM'):
                        x=random.randint(0, 2)
                        print(x)
                        operacio=opernoms[x]
                    else:
                        operacio=poperacio
                    x, y = start_the_game(operacio,10)

                    # Reinicia la InputBox
                    input_box = InputBox(190, 250, 200, 32)
        #Fa aparèixer x/y en pantalla i l'actualitza
        display_the_game(x, y)
        pygame.display.update()

#Aquesta funció està destinada a explicar el funcionament de l'apartat dels nivells d'imatges
def jugarimatges(poperacio):
    #Variable del bucle principal, temporitzador i punts del nivell
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
    #La funció següent genera tots els assets del nivell

    def main2():
        #Es posen totes les imatges en un array, de manera que posteriorment es seleccionarà una aleatoriament
        fruites = ["FotoPera.png","FotoPoma.png","FotoMiquel.png", "FotoBanana.png"]
        imagefruit = pygame.image.load(fruites[idfruita]).convert()
        
        if operacio=='SUMA':
            titol = 'Suma (2)'
            signe = pygame.image.load("Fotosuma.png").convert()
        if operacio=='RESTA':
            titol = 'Resta (2)'
            signe = pygame.image.load("Fotoresta.png").convert()
        if operacio=='MULTIPLICACIO':
            titol = 'Multiplicació (2)'
            signe = pygame.image.load("Fotomultiplicació.png").convert()
        if operacio=='DIVISIO':
            titol = 'Divisió (2)'
            signe = pygame.image.load("Fotodivisio.png").convert()

        # Tipografia, títol i entrada de respostes
        font = pygame.font.SysFont('comicsans', 50)
        # Fons
        surface.fill((255, 70, 90))

        # Aquí és el lloc on es generen les dieferents imatges
        espai=90
        lloc=0
        for i in range(x):
            lloc=lloc+espai
            surface.blit(imagefruit, (lloc, 120))
        lloc=lloc+espai
        surface.blit(signe, (lloc, 120))
        for i in range(y):
            lloc=lloc+espai
            surface.blit(imagefruit, (lloc, 120))

        #Aquestes variables s'encarreguen de mostrar cada cosa al seu lloc
        punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
        surface.blit(punts, (350, 30))
        titolsuma2 = font.render(titol, True, (0, 0, 0))
        surface.blit(titolsuma2, (10, 20))
        temps = font.render("Temps: " + str(t), True, (255, 255, 51))
        surface.blit(temps, (0, 360))

        
        # Es genera la inputbox i s'actualitza la pantalla
        input_box.draw(surface)
        pygame.display.flip()

    if (poperacio=='RANDOM'):
        x=random.randint(0, 2)
        operacio=opernoms[x]
    else:
        operacio=poperacio
    x, y = start_the_game(operacio,6)
    #Agafa una imatge qualsevol de les fruites
    idfruita = random.randint(0, 3)
    input_box = InputBox(190, 250, 200, 32)

    #Bucle principal dels segons nivells
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
                #Assigna els valors de x i y a la funció un altre cop (per generar nous números)
                if (poperacio=='RANDOM'):
                    x=random.randint(0, 2)
                    operacio=opernoms[x]
                else:
                    operacio=poperacio
                x, y = start_the_game(operacio,6)
                idfruita = random.randint(0, 3)
                input_box = InputBox(190, 250, 200, 32)

        main2()
        pygame.display.update()


#Aquesta funció defineix el funcionament dels tercers nivells (àudios)
def jugaraudios():
    #La funció següent pinta el fons del programa i fa aparèixer diverses coses en pantalla
    def main3():
        audios = ["Audio1.wav", "Audio2.wav", "Audio3.wav"]
        surface.fill((255, 70, 90))

        #Es genera la imatge
        surface.blit(imageaudio1, image_position)
        #Escenifiquen en pantalla els punts, nom del nivell i el temps
        punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
        surface.blit(punts, (350, 30))
        titolsuma3 = font.render("Suma (3)", True, (0, 0, 0))
        surface.blit(titolsuma3, (10, 20))
        temps = font.render("Temps: " + str(t),True, (255,255,51))
        surface.blit(temps,(0,360))
        #Fa aparèixer la caixeta de respostes i actualitza la pantalla
        input_box.draw(surface)
        pygame.display.flip()
    #Temporitzador i es puja la imatge
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    imageaudio1 = pygame.image.load("ClickAudio1.png").convert()
    # Assigna quina és la posició de la imatge
    image_position = (190, 70)
    image_size = imageaudio1.get_rect().size
    # Quina és la tipografia, títol de la finestra i posiciona la InputBox
    font = pygame.font.SysFont('comicsans', 50)
    input_box = InputBox(190, 250, 200, 32)
    #Variable que farà que el bucle funcioni, a més del temps i els punts
    yousayrun = True
    global pointsgeneral
    points=pointsgeneral
    t = 15

    
    # Bucle principal del tercer nivell
    while yousayrun:
        #Transporta els esdeveniments del menú al programa (els enllaça)
        if main_menu.is_enabled():
            main_menu.update(events)
            clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Si s'apreta la "X", es surt del nivell
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
                    # Si la imatge ha estat clicada, sonarà un àudio aleatori

                    mixer.music.load("Audio1.wav")
                    mixer.music.play(1)
                    time.sleep(1)
                    mixer.music.load("Mes.wav")
                    mixer.music.play(1)
                    time.sleep(1)
                    mixer.music.load("Audio2.wav")
                    mixer.music.play(1)
                    a=1

            result = input_box.handle_event(event)
            if result != None:
                # Si la resposta és correcta se li sumarà 5 punts
                if int(result) == int(12):
                    points = points + 5
                    t = t + 5
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


opernoms=['SUMA','MULTIPLICACIO','RESTA', 'DIVISIO']

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






