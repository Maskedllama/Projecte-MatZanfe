import pygame
from InputBox import InputBox


pygame.init()
# Variables
yousayrun = True
clock = pygame.time.Clock()
pointsM2= 0
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')

# Mida de la finestra i es carrega la imatge
surface = pygame.display.set_mode((600, 400))
imagefruit3 = pygame.image.load("FotoMiquel.png").convert()
signemultiplicacio = pygame.image.load("Fotomultiplicació.png").convert()

#Tipografia, títol i entrada de respostes
font = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption("Projecte MatZanfe")
input_box = InputBox(190, 250, 200, 32)


def main():
    surface.fill((70, 255, 70))

    # Aquí es genera la imatge, títols i puntuació
    surface.blit(imagefruit3,(10,140))
    surface.blit(imagefruit3,(10,60))
    surface.blit(imagefruit3,(120,140))
    surface.blit(imagefruit3,(120,60))
    surface.blit(signemultiplicacio,(270,150))
    surface.blit(imagefruit3,(340,120))
    surface.blit(imagefruit3,(460,120))

    punts = font.render("Puntuació: " + str(pointsM2), True, (255, 255, 255))
    surface.blit(punts, (350, 30))
    titolmultiplicacio2 = font.render("Multiplicació (2)", True, (0, 0, 0))
    surface.blit(titolmultiplicacio2, (10, 20))

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
            if int(result) == int(8):
                pointsM2 = pointsM2 + 5
        pygame.display.update()

pygame.quit()