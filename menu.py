import pygame, pygame_gui, sys
from pygame.locals import *
from RayCaster import Game


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((1000, 500))


width = 1000
height = 500


#background = pygame.image.load('Sources/fondo.jpg')
betaversion = pygame.image.load('Sources/beta.png')
background = pygame.image.load('Sources/fondo2.jpg')

class Menu(object):
    
    def __init__(self):
        super().__init__()

        self.mainClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('STREETS')
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL)
        self.screen.set_alpha(None)

        self.titleFont = pygame.font.Font("Sources/pricedown.bl-regular.otf", 90)
        self.buttonFont = pygame.font.Font("Sources/arcadeclassic.regular.ttf", 35)

        self.click = False
        self.mouse_hover = False

        self.start()



    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    def draw_background(self):
        tex = pygame.transform.scale(background, (width, height))
        rect = tex.get_rect()
        self.screen.blit(tex, rect)


    def add_image(self):
        tex = pygame.transform.scale(betaversion, (100, 50))
        rect = tex.get_rect()
        self.screen.blit(tex, rect)


    def create_rect(self, width, height, border, color, border_color):
        surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, color, (border, border, width, height), 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
        return surf


    def start(self):

        while 1:

            self.screen.fill((0, 0, 0))
            self.draw_background()
            self.add_image()
            self.draw_text('STREETS', self.titleFont, (255, 185, 203), self.screen, 360, 50)

            mx, my = pygame.mouse.get_pos()

            # 1. X | 2. Y | 3. Largo | 4. Alto
            button_1 = pygame.Rect(425, 210, 140, 55)
            button_2 = pygame.Rect(425, 320, 140, 55)


            button_1_is_hover = False
            button_2_is_hover = False


            if button_1.collidepoint((mx, my)):
                if self.click:
                    Game(self.screen, self.mainClock, width, height)

                elif self.mouse_hover:
                    button_1_is_hover = True

            if button_2.collidepoint((mx, my)):
                if self.click:
                    pygame.quit()
                    sys.exit()
                elif self.mouse_hover:
                    button_2_is_hover = True

            button_color = (218, 97, 36)
            button_color_hover = (205, 107, 107)

            button_1_color = button_color if button_1_is_hover else button_color_hover  
            button_2_color = button_color if button_2_is_hover else button_color_hover 

            # 1
            pygame.draw.rect(self.screen, button_1_color, button_1,  border_radius=10)
            self.draw_text('start', self.buttonFont, (0, 0, 0), self.screen, 450, 218)

            # 2
            pygame.draw.rect(self.screen, button_2_color, button_2,  border_radius=10)
            self.draw_text('exit', self.buttonFont, (0, 0, 0), self.screen, 450, 328)


            self.click = False
            self.mouse_hover = False

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == button_1:
                    Game()

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

                elif event.type == MOUSEMOTION:
                    self.mouse_hover = True


            pygame.display.update()
            self.mainClock.tick(60)