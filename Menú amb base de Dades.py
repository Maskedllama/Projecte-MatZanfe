import pygame
import pygame_menu
import sqlite3

# Initialize pygame
pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Projecte MatZanfe")


font = pygame_menu.font.FONT_8BIT
font1 = pygame_menu.font.FONT_NEVIS
font2 = pygame_menu.font.FONT_BEBAS

#Make menu Sumes
menu3 = pygame_menu.Menu('Sums', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)

menu3.add.button('Infinite sums', font_name = font1, font_color = 'green')
menu3.add.button('Sums with images', font_name = font1, font_color = 'blue')
menu3.add.button('Sums with audio', font_name = font1,font_color = 'red')

#Make menu Restes
menu4 = pygame_menu.Menu('Subtraction', 600, 400,
                       theme=pygame_menu.themes.THEME_DEFAULT)

menu4.add.button('Infinite subtractions', font_name = font1, font_color = 'green')
menu4.add.button('Subtractions with images', font_name = font1, font_color = 'blue')
menu4.add.button('Subtratcions with audio', font_name = font1,font_color = 'red')

#Make menu Multiplicacions
menu5 = pygame_menu.Menu('Multiplications', 600, 400,
                       theme=pygame_menu.themes.THEME_ORANGE)

menu5.add.button('Infinite multiplications', font_name = font1, font_color = 'green')
menu5.add.button('Multiplications with images', font_name = font1, font_color = 'blue')
menu5.add.button('Multiplications with audio', font_name = font1,font_color = 'red')

#Make menu Divisions
menu6 = pygame_menu.Menu('Divisions', 600, 400,
                       theme=pygame_menu.themes.THEME_GREEN)

menu6.add.button('Infinite divisions', font_name = font1, font_color = 'black')
menu6.add.button('Divisions with images', font_name = font1, font_color = 'blue')
menu6.add.button('Divisions with audio', font_name = font1,font_color = 'red')

# Make menu 2
menu2 = pygame_menu.Menu('Module selection', 600, 400,
                       theme=pygame_menu.themes.THEME_SOLARIZED)


menu2.add.button('Sums',menu3, font_name = font2, font_color = 'green')
menu2.add.button('Subtractions',menu4, font_name = font2, font_color = 'blue')
menu2.add.button('Multiplications',menu5, font_name = font2,font_color = 'red')
menu2.add.button('Divisions',menu6, font_name = font2, font_color = 'purple' )

# Make main menu
menu = pygame_menu.Menu('Projecte MatZanfe', 600, 400,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

user_input = menu.add.text_input('User: ', font_name = font1, font_color = 'blue')
age_input = menu.add.text_input('Age: ', font_name = font1,font_color = 'Black')
menu.add.button('Start', menu2, font_name = font, font_color = 'green')
menu.add.button('Exit', pygame_menu.events.EXIT, font_name = font,font_color = 'red')

#Base de dades
miConexion = sqlite3.connect ("Base de Dades del Programa")
miCursor = miConexion.cursor()
miCursor.execute("CREATE TABLE DADES (user_input VARCHAR (50), age_input INTEGER)")

# Run the menu
menu.mainloop(surface)