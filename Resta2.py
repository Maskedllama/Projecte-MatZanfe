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
imagefruit2 = pygame.image.load("FotoPoma.png").convert()
signeresta = pygame.image.load("Fotoresta.png").convert()

#Tipografia, títol de la finestra i entrada de respostes
font = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption("Projecte MatZanfe")
input_box = InputBox(190, 250, 200, 32)


def main():
    #Pinta el fons del programa
    surface.fill((70, 90, 255))

    # Aquí es genera la imatge, títols i puntuació
    surface.blit(imagefruit2,(25,150))
    surface.blit(imagefruit2,(120,150))
    surface.blit(imagefruit2,(70,60))
    surface.blit(signeresta,(250,120))
    surface.blit(imagefruit2,(340,120))
    surface.blit(imagefruit2,(440,120))

    punts = font.render("Puntuació: " + str(points), True, (255, 255, 255))
    surface.blit(punts, (350, 30))
    titolresta2 = font.render("Resta (2)", True, (0, 0, 0))
    surface.blit(titolresta2, (10, 20))

    input_box.draw(surface)
    pygame.display.flip()


# Bucle principal
while yousayrun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yousayrun = False

        main()
        result = input_box.handle_event(event)
        if result != None:
            if int(result) == int(1):
                points = points + 5
        pygame.display.update()

pygame.quit()