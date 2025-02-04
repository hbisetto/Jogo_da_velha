import pygame


class Obj:

    def __init__(self, image, x, y):

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        self.status = 'n'

    def drawing(self, window):

        window.blit(self.image, (self.rect[0], self.rect[1]))