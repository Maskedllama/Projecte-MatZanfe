#Llibreries
import pygame
import random
from InputBox import InputBox
from pygame import mixer

#Inicia pygame
pygame.init()
#Variables:
#Temporitzador: 1000 significa un segon
pygame.time.set_timer(pygame.USEREVENT, 1000)
clock = pygame.time.Clock()
#Mida i Nom pantalla
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Projecte MatZanfe")
#Tipografia  / complements InputBox
font = pygame.font.SysFont('comicsans', 50)
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')
#Punts, temps inicial i bucle principal
running = True
points = 0
t = 60


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

#Assigna els valors de x i y a la funció un altre cop (per generar nous números)
x, y = start_the_game()
input_box = InputBox(190, 250, 200, 32)

#Main loop
while running:
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
                pygame.display.quit()
                pygame.quit()
        else:
            result = input_box.handle_event(event)
            if result != None:
                #Si el resultat que es posa és el correcte, se li sumarà temps i sonarà un àudio
                if int(result) == int(x) + int(y):
                    points = points + 5
                    t = t + 5
                    mixer.music.load('StarPost.wav')
                    mixer.music.play(1)

                # Crea nous números
                x, y = start_the_game()

                # Reinicia la InputBox
                input_box = InputBox(190, 250, 200, 32)


    display_the_game(x, y)
    pygame.display.update()

pygame.quit()