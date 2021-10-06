import pygame
from InputBox import InputBox


pygame.init()
# Variables
yousayrun = True
clock = pygame.time.Clock()
points= 0
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')

# Mida de la finestra i es carrega la imatge
surface = pygame.display.set_mode((600, 400))
imagefruit4 = pygame.image.load("FotoBanana.png").convert()
signedivisio = pygame.image.load("Fotodivisio.png").convert()

#Tipografia, títol i entrada de respostes
font = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption("Projecte MatZanfe")
input_box = InputBox(190, 250, 200, 32)


def main():
    #Fons
    surface.fill((222, 184, 135))

    # Aquí es genera la imatge, títols i puntuació
    surface.blit(imagefruit4,(25,150))
    surface.blit(imagefruit4,(120,150))
    surface.blit(imagefruit4,(120,60))
    surface.blit(imagefruit4,(25,60))
    surface.blit(signedivisio,(280,150))
    surface.blit(imagefruit4,(340,120))
    surface.blit(imagefruit4,(440,120))

    punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
    surface.blit(punts, (350, 30))
    titoldivisio2 = font.render("Divisió (2)", True, (0, 0, 0))
    surface.blit(titoldivisio2, (10, 20))

    input_box.draw(surface)
    pygame.display.flip()


# Main Loop
while yousayrun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yousayrun = False

        main()
        result = input_box.handle_event(event)
        if result != None:
            if int(result) == int(2):
                points = points + 5
        pygame.display.update()

pygame.quit()