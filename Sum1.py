import pygame
import random
from InputBox import InputBox
from pygame import mixer
import time

pygame.init()

pygame.time.set_timer(pygame.USEREVENT, 1000)
clock = pygame.time.Clock()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Projecte MatZanfe")
font = pygame.font.SysFont('comicsans', 50)
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')
running = True
points = 0
t = 60
def TimeFunction():
    t = 60
    while True:
        time.sleep(1)
        t = t - 1
        return t

def start_the_game():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    is_correct = False
    return x, y

def display_the_game(x, y):
    # Variables
    z = x + y
    surface.fill((255, 70, 90))
    text = font.render(str(x) + "+" + str(y), True, (255, 255, 255))

    text_surface = base_font.render(user_text, True, (255, 255, 255))
    surface.blit(text, (260, 120))
    input_box.draw(surface)
    punts = font.render("Puntuació: " +  str(points),True, (255,255,255))
    surface.blit(punts, (350,30))
    titolsuma = font.render("SUMA (1)", True, (0,0,0))
    surface.blit(titolsuma,(10,20))
    temps = font.render("Temps: " + str(t),True, (255,255,51))
    surface.blit(temps,(0,360))

x, y = start_the_game()
input_box = InputBox(190, 250, 200, 32)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            t -= 1
            temps = font.render("Temps:" + str(t), True, (255, 255, 51))
            surface.blit(temps, (0, 360))
            pygame.display.flip()
            if t == 0:
                pygame.quit()
        else:
            result = input_box.handle_event(event)
            if result != None:
                if int(result) == int(x) + int(y):
                    points = points + 5
                    t = t + 5
                    mixer.music.load('StarPost.wav')
                    mixer.music.play(1)


                # create new random numbers
                x, y = start_the_game()

                # reset input box (just create a new box)
                input_box = InputBox(190, 250, 200, 32)


    display_the_game(x, y)
    pygame.display.update()

pygame.quit()