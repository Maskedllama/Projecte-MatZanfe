# Importar librerías
import pygame
import pygame_menu

# Iniciar pygame y otras variables
pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Project MatZanfe")

font = pygame_menu.font.FONT_8BIT
font1 = pygame_menu.font.FONT_NEVIS
font2 = pygame_menu.font.FONT_BEBAS

#menu Sumas
menu3 = pygame_menu.Menu('Sumas', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)

menu3.add.button('Sumas infinitas', font_name = font1, font_color = 'green')
menu3.add.button('Sumas difíciles', font_name = font1, font_color = 'blue')
menu3.add.button('Sumas con voz', font_name = font1,font_color = 'red')


#menu 2
menu2 = pygame_menu.Menu('Selección del mòdulo', 600, 400,
                       theme=pygame_menu.themes.THEME_SOLARIZED)


menu2.add.button('Sumas',menu3, font_name = font2, font_color = 'green')

#main menu
menu = pygame_menu.Menu('Project MatZanfe', 600, 400,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

user_input = menu.add.text_input('Usuario: ', font_name = font1, font_color = 'blue')
age_input = menu.add.text_input('Edad: ', font_name = font1,font_color = 'Black')
menu.add.button('Empezar', menu2, font_name = font, font_color = 'green')
menu.add.button('Salir', pygame_menu.events.EXIT, font_name = font,font_color = 'red')

# Correr el menú
menu.mainloop(surface)
