import pygame


class Obj:

    def __init__(self, image, x, y, peca=0):

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        self.status = 'n'
        self.peca = peca

    def drawing(self, window):

        window.blit(self.image, (self.rect[0], self.rect[1]))