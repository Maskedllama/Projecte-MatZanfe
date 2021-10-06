# S'importen les llibreries utilitzades
import pygame
import pygame_menu
from pygame import mixer
import random
from InputBox import InputBox
import time

# Constants que determinen l'altura i amplada del treball
WINDOW_SIZE = WIDTH, HEIGHT = 700, 500

#Funció que crearà el menú principal del programa.
# Aquí s'estableix la mida, el títol i els colors.
def creamenus(surface):

    # Crea el menú de les Sumes
    menu3 = pygame_menu.Menu('Sumes', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_BLUE)

    menu3.add.button('Sumes infinites',jugar,"SUMA", font_name=font1, font_color='green')
    menu3.add.button('Sumes amb imatges',jugarimatges, "SUMA",font_name=font1, font_color='blue')
    menu3.add.button('Sumes dictades', jugaraudios, "SUMA", font_name=font1, font_color='red')

    # Crea el menú de les Restes
    menu4 = pygame_menu.Menu('Restes', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_DEFAULT)

    menu4.add.button('Restes infinites',jugar,"RESTA", font_name=font1, font_color='green')
    menu4.add.button('Restes amb imatges', jugarimatges, "RESTA", font_name=font1, font_color='blue')
    menu4.add.button('Restes dictades',  jugaraudios, "RESTA", font_name=font1, font_color='red')

    # Crea el menú de les Multiplicacions
    menu5 = pygame_menu.Menu('Multiplicacions', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_ORANGE)

    menu5.add.button('Multiplicacions infinites',jugar,"MULTIPLICACIO", font_name=font1, font_color='green')
    menu5.add.button('Multiplicacions amb imatges', jugarimatges, "MULTIPLICACIO", font_name=font1, font_color='blue')
    menu5.add.button('Multiplicacions dictades', jugaraudios, "MULTIPLICACIO", font_name=font1, font_color='black')

    # Crea el menú de les Divisions
    menu6 = pygame_menu.Menu('Divisions', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_GREEN)

    menu6.add.button('Divisions infinites',jugar,"DIVISIO", font_name=font1, font_color='yellow')
    menu6.add.button('Divisons amb imatges', jugarimatges, "DIVISIO", font_name=font1, font_color='blue')
    menu6.add.button('Divisions dictades',  jugaraudios, "DIVISIO", font_name=font1, font_color='red')

    # Crea el segon menú del programa, que funciona com a entrada dels anteriors menus
    menu2 = pygame_menu.Menu('Selecció dels mòduls', WINDOW_SIZE[0], WINDOW_SIZE[1],
                             theme=pygame_menu.themes.THEME_SOLARIZED)

    #Fa sonar la música del programa
    # msele = mixer.music.load('LevelSelector.wav')
    # msele2 = mixer.music.play(-1)
    menu2.add.button('Sumes', menu3, font_name=font2, font_color='green')
    menu2.add.button('Restes', menu4, font_name=font2, font_color='blue')
    menu2.add.button('Multiplicacions', menu5, font_name=font2, font_color='red')
    menu2.add.button('Divisions', menu6, font_name=font2, font_color='purple')

    # És el principal menú del programa.
    main_menu = pygame_menu.Menu('Projecte MatZanfe', WINDOW_SIZE[0], WINDOW_SIZE[1],
                            theme=pygame_menu.themes.THEME_SOLARIZED)

    user_input = main_menu.add.text_input('Usuari: ', font_name=font1, font_color='blue')
    # mixer.music.load('MusicaMenu.wav')
    # mixer.music.play(-1)
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
#nivells infinits. Inclou la representació en pantalla.
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
        surface.blit(temps,(0,360))

    #Aquest apartat crea un temporitzador
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    #Defineix el tipus de lletre i l'espai on l'usuari pot escriure.
    font = pygame.font.SysFont('comicsans', 50)
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    #Determina el color d'algunes de les coses
    color_active = pygame.Color('lightskyblue3')
    #Punts, temps inicial i variable del bucle principal
    running = True
    global pointsgeneral
    points=pointsgeneral
    t = 60

    #Assigna els valors de x i y a la funció un altre cop (per generar nous números)
    if (poperacio=='RANDOM'):
        x=random.randint(0, 2)
        operacio=opernoms[x]
    else:
        operacio=poperacio
    #Tornem a assignar valors a les variables i posicionem la caixeta de respostes
    x, y = start_the_game(operacio,10)
    input_box = InputBox(190, 250, 200, 32)


    #Bucle principal
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
            #Aquí es parla de tots els esdeveniments connectats amb l'usuari.
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
                        #S'escoltarà un soroll de resposta correcta al fer-ho bé
                        mixer.music.load('StarPost.wav')
                        mixer.music.play(1)

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
    # Variables ja explicades i InputBox
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    color_active = pygame.Color('lightskyblue3')
    input_box = InputBox(190, 250, 200, 32)
    #Temps i puntuació global
    global pointsgeneral
    points = pointsgeneral
    t = 20
    font = pygame.font.SysFont('comicsans', 50)

    #La següent funció genera tots els assets del nivell
    def main2():
        #Es posen totes les imatges en un array, de manera que posteriorment es seleccionarà una aleatoriament
        fruites = ["FotoPera.png","FotoPoma.png","FotoMiquel.png", "FotoBanana.png"]
        imagefruit = pygame.image.load(fruites[idfruita]).convert()

        #Si es selecciona un determinat mòdul, es canvia el signe i el títol del nivell
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

        # Tipografia
        font = pygame.font.SysFont('comicsans', 50)

        # Fons
        surface.fill((255, 70, 90))

        # Sistema que s'ha creat per evitar que les imatges generades es posicionin
        #una sobre de l'altra, conseqüentment creant un espai entre elles
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

        #Aquestes variables s'encarreguen de mostrar cada cosa al seu lloc:
        #Puntuació actual, títol de cada cosa i el temps restant
        punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
        surface.blit(punts, (350, 30))
        titolsuma2 = font.render(titol, True, (0, 0, 0))
        surface.blit(titolsuma2, (10, 20))
        temps = font.render("Temps: " + str(t), True, (255, 255, 51))
        surface.blit(temps, (0, 360))

        
        # Es genera la inputbox i s'actualitza la pantalla
        input_box.draw(surface)
        pygame.display.flip()
    # Aquest apartat provoca un nivell on les imatges pateixen una operació matemàtica diferent
    # desprès de cada operació
    if (poperacio=='RANDOM'):
        x=random.randint(0, 2)
        operacio=opernoms[x]
    else:
        operacio=poperacio
    x, y = start_the_game(operacio,6)
    #Agafa una imatge qualsevol de les fruites i posiciona la caixeta de respostes
    idfruita = random.randint(0, 3)
    input_box = InputBox(190, 250, 200, 32)

    #Bucle principal dels segons nivells
    while corrent:
        # Activa el menú
        if main_menu.is_enabled():
            main_menu.update(events)
            clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corrent = False
            if event.type == pygame.USEREVENT:
                # Disminueix el temps cada segon
                t -= 1
                temps = font.render("Temps:" + str(t), True, (255, 255, 51))
                surface.blit(temps, (0, 360))
                pygame.display.flip()
                if t == 0:
                    #Si arriba a 0 el programa es tanca
                    pointsgeneral=pointsgeneral + points
                    main_menu.enable()
                    return
            # Permet introduir un resultat a la caixeta
            result = input_box.handle_event(event)
            #Si s'ha posat alguna resposta a la caixeta, es mira si és correcte
            if result != None:
                # Si s'ha escollit fer una suma, l'enunciat tindrà el símbol "+"
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
                    # S'escoltarà un soroll de resposta correcta al fer-ho bé
                    mixer.music.load('StarPost.wav')
                    mixer.music.play(1)
                # Si l'operació és aleatoria, el valor de x serà de 0 a 2 per precaució
                if (poperacio=='RANDOM'):
                    x=random.randint(0, 2)
                    operacio=opernoms[x]
                else:
                    operacio=poperacio
                # Assigna els valors de x i y a la funció un altra cop, posiciona la caixeta i genera una fruita
                x, y = start_the_game(operacio,6)
                idfruita = random.randint(0, 3)
                input_box = InputBox(190, 250, 200, 32)
        # Fa funcionar constantment la funció del segon nivell i actualitza la pantalla
        main2()
        pygame.display.update()


#Aquesta funció defineix el funcionament dels tercers nivells (àudios)
def jugaraudios(poperacio):

    #Temporitzador i es puja la imatge que serà clickable
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    imageaudio1 = pygame.image.load("ClickAudio1.png").convert()
    # Assigna quina és la posició de la imatge
    image_position = (190, 70)
    image_size = imageaudio1.get_rect().size
    # Quina és la tipografia i posiciona la InputBox
    font = pygame.font.SysFont('comicsans', 50)
    input_box = InputBox(190, 250, 200, 32)
    #Variable que farà que el bucle funcioni, a més del temps i els punts
    yousayrun = True
    global pointsgeneral
    points=pointsgeneral
    t = 20
    #S'inicia el mòdul de mixer
    mixer.init()
    # Es crea un array dels diferents àudios gravats meus que diuen els números
    sonum=[0,1,2,3,4,5,6,7,8,9]
    # Es crea un array dels diferents àudios gravats que dictaminen una operació
    soope=[0,1,2,3]
    # Assigna un so a cadascun dels valors de l'array
    sonum[0]=pygame.mixer.Sound('Audio0.wav')
    sonum[1]=pygame.mixer.Sound('Audio1.wav')
    sonum[2]=pygame.mixer.Sound('Audio2.wav')
    sonum[3]=pygame.mixer.Sound('Audio3.wav')
    sonum[4]=pygame.mixer.Sound('Audio4.wav')
    sonum[5]=pygame.mixer.Sound('Audio5.wav')
    sonum[6]=pygame.mixer.Sound('Audio6.wav')
    sonum[7]=pygame.mixer.Sound('Audio7.wav')
    sonum[8]=pygame.mixer.Sound('Audio8.wav')
    sonum[9]=pygame.mixer.Sound('Audio9.wav')
    soope=[0,1,2,3]
    soope[0]=pygame.mixer.Sound('Mes.wav')
    soope[1]=pygame.mixer.Sound('Menys.wav')
    soope[2]=pygame.mixer.Sound('Multiplicat.wav')
    soope[3]=pygame.mixer.Sound('Dividit.wav')

    # Aquesta funció determina tot allò que apareix en pantalla
    def pantalla():
        #Fons de la pantalla
        surface.fill((255, 70, 90))
        #Es genera la imatge
        surface.blit(imageaudio1, image_position)
        #Escenifica en pantalla els punts, nom del nivell i el temps
        punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
        surface.blit(punts, (350, 30))
        titolsuma3 = font.render(operacio, True, (0, 0, 0))
        surface.blit(titolsuma3, (10, 20))
        temps = font.render("Temps: " + str(t),True, (255,255,51))
        surface.blit(temps,(0,360))
        #Fa aparèixer la caixeta de respostes i la actualitza la pantalla
        input_box.draw(surface)
        pygame.display.flip()
    # Aquesta funció el que fa és seleccionar un dels àudios, dir un tipus d'operació, i llavors un altra àudio
    def so():
        # Sona el primer valor
        sonum[x].play()
        print(x)
        # s'espera 1 segon
        time.sleep(1)
        # Si l'operació és una suma, el títol canvia i sonarà "Més" entremig
        if operacio=="SUMA":
            titol = "Suma (3)"
            soope[0].play()
            # Si l'operació és una resta, el títol canvia i sonarà "Menys" entremig
        if operacio=="RESTA":
            soope[1].play()
            titol = "Resta (3)"
        # Si l'operació és una multiplicació, el títol canvia i sonarà "Multiplicat per" entremig
        if operacio=="MULTIPLICACIO":
            titol = "Multiplicació (3)"
            soope[2].play()
        # Si l'operació és una divisió, el títol canvia i sonarà "Dividit per" entremig
        if operacio=="DIVISIO":
            titol = "Divisió (3)"
            soope[3].play()
        # S'espera 1,5 segons
        time.sleep(1.5)
        print(y)
        # Sona el segon valor i es pausa 1 segon
        sonum[y].play()
        time.sleep(1)
    # Si és del mòdul aleatori, x estarà compresa entre 0 i 2 per seguretat
    if (poperacio=='RANDOM'):
        x=random.randint(0, 2)
        operacio=opernoms[x]
    else:
        operacio=poperacio
    # Assigna nous valors a x i y. Crida les diferents funcions del nivell i posiciona la caixeta de respostes
    x, y = start_the_game(operacio,9)
    pantalla()
    so()
    input_box = InputBox(200, 250, 200, 32)
    
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
                # Troba la posició del clic
                click = pygame.mouse.get_pos()
                # Es revisa si el clic ha estat a la imatge
                if image_position[0] < click[0] < image_position[0] + image_size[0] and image_position[1] < click[1] < image_position[1] + image_size[1]:
                    so()
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
                #Si l'operació és aleatori, x es limita a estar compresa entre 0 i 2 per seguretat
                if (poperacio=='RANDOM'):
                    x=random.randint(0, 2)
                    operacio=opernoms[x]
                else:
                    operacio=poperacio
                #Torna a assignar-se valors a x i y, es criden les funcions del tercer nivell i es posiciona la caixeta
                x, y = start_the_game(operacio,9)
                so()
                input_box = InputBox(200, 250, 200, 32)
        #Fa aparèixer tot en pantalla i l'actualitza
        pantalla()
        pygame.display.update()

# -------------------------------------------------------------------------
# Variables Globals
# -------------------------------------------------------------------------
global clock
global main_menu
global surface
global font1,font2,font3
pointsgeneral=0

#Dessigna el nom de les diverses operacions que podem trobar dins del programa
opernoms=['SUMA','MULTIPLICACIO','RESTA', 'DIVISIO']
#Inicialitza la llibreria Pygame
pygame.init()
#Determina la mida de la pantalla
surface = pygame.display.set_mode(WINDOW_SIZE)
#Hi posa un títol al programa
pygame.display.set_caption("Projecte MatZanfe")
#Logotip de la finestra
logotip = pygame.image.load("calculator.png")
pygame.display.set_icon(logotip)
#Estableix alguns tipus de lletra emprats al programa
font = pygame_menu.font.FONT_8BIT
font1 = pygame_menu.font.FONT_NEVIS
font2 = pygame_menu.font.FONT_BEBAS
#La variable de main_menu s'assigna a la funció creamenus per mantenir-la oberta
main_menu=creamenus(surface)

# És el bucle més important del programa, ja que mentre aquest nucli estigui obert tot estarà obert
while True:
    # Tots els diferents esdeveniments del programa estaran disponibles
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            #Si apretem "SORTIR" o la x del programa, sortirem d'aquest
            exit()

    # Mentre el menú estigui habilitat, la pantalla podrà obrir-se
    if main_menu.is_enabled():
        main_menu.mainloop(surface)

    # ----------------------------------------------------------------------------
    # Fins aquí arriba el projecte. He de dir que, al ser la meva primera vegada
    # programant (de fet, aquest serà ha estat meu primer programa!!!), mai podré
    # oblidar tota aquesta experiència. Ha estat difícil, però crec que he
    # après coses que poques persones que conec arriben a saber. Ens veiem!!!!
    # ----------------------------------------------------------------------------






