# Llibreries
import pygame
import pygame_menu
from pygame import mixer
import sqlite3

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

#Make menu Sumes
menu3 = pygame_menu.Menu('Sumes', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)

menu3.add.button('Sumes infinites', font_name = font1, font_color = 'green')
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

mixer.music.load('MusicaMenu.wav')
mixer.music.play(-1)
#Aquí hi ha el problema, ja que lo que demana les dades per a la base és un widget d'una llibreria externa.
#Els següents inputs haurien de guardar el que s'ha escrit, però no ho guarden correctament.
user_input = menu.add.text_input('Usuari: ', font_name = font1, font_color = 'blue')
age_input = menu.add.text_input('Edat: ', font_name = font1,font_color = 'Black')
menu.add.button('Comencem', menu2, font_name = font, font_color = 'green')
menu.add.button('Sortir', pygame_menu.events.EXIT, font_name = font,font_color = 'red')

miConexion = sqlite3.connect ("Base Dades")
miCursor = miConexion.cursor()

#Crea la taula si no existeix. Si existeix, deixar d'aquesta manera.
#miCursor.execute("CREATE TABLE DADES (Usuari VARCHAR (50), Edat INTEGER)")

#Inserta les dades a les columnes d'usuari i edat.
miCursor.execute("INSERT INTO DADES (Usuari, Edat) VALUES (?, ?)",
                 (str(user_input),str(age_input)))

miConexion.commit()

miConexion.close()

# Acciona el menú
menu.mainloop(surface)
