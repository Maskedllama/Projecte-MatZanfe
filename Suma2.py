import pygame
from InputBox import InputBox


pygame.init()
# Variables pel main loop
yousayrun = True
clock = pygame.time.Clock()
points= 0
#Variables InputBox
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')

# Mida de la finestra i es carrega la imatge
surface = pygame.display.set_mode((600, 400))
imagefruit1 = pygame.image.load("FotoPera.png").convert()
signesuma = pygame.image.load("Fotosuma.png").convert()

#Tipografia, títol i entrada de respostes
font = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption("Projecte MatZanfe")
input_box = InputBox(190, 250, 200, 32)


def main2():
    #Fons
    surface.fill((255, 70, 90))

    # Aquí es genera les imatges, títols i puntuació
    surface.blit(imagefruit1,(30,120))
    surface.blit(imagefruit1,(120,120))
    surface.blit(signesuma,(250,120))
    surface.blit(imagefruit1,(340,120))
    surface.blit(imagefruit1,(440,120))

    punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
    surface.blit(punts, (350, 30))
    titolsuma2 = font.render("Suma (2)", True, (0, 0, 0))
    surface.blit(titolsuma2, (10, 20))
    #Es genera la inputbox i s'actualitza la pantalla
    input_box.draw(surface)
    pygame.display.flip()


# Main Loop
while yousayrun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yousayrun = False

        main2()
        result = input_box.handle_event(event)
        if result != None:
            if int(result) == int(4):
                points = points + 5
        pygame.display.update()

pygame.quit()