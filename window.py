import pygame
import random

class Window:

    def __init__(self, x, y, title, game):

        pygame.init()

        self.window = pygame.display.set_mode([x, y])
        self.title = pygame.display.set_caption(title)

        self.loop = True

        self.list_obj = []

        # Criamos uma instância do jogo para acessar as peças
        self.game = game
        
    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if events.type == pygame.MOUSEBUTTONDOWN:
                # Percorre todas as peças e verifica qual foi clicada
                for i, peca in enumerate(self.game.get_peca(), start=1):
                    if peca.rect.collidepoint(events.pos):  
                        self.n_to_x(i)
                        #print(f'Peca {i} alterada ')

    def n_to_x(self, peca):
        if self.game.jogador['jogar']:
            todas = self.game.get_peca()
            if todas[peca-1].status == 'n':  # Se a peça for neutra
                todas[peca-1].status = 'x'   # Marca a peça como 'x'
                todas[peca-1].image = pygame.image.load('assets/peca-x.bmp')  # Altera a imagem
                
                # Redesenha a peça
                self.game.tela.add_obj(todas[peca-1].drawing(self.game.tela.window))
            self.game.jogador['jogar'] = False
                
    def n_to_o(self, peca):
        if self.game.jogador['jogar']:
            todas = self.game.get_peca()
            if todas[peca-1].status == 'n':  # Se a peça for neutra
                todas[peca-1].status = 'o'   # Marca a peça como 'x'
                todas[peca-1].image = pygame.image.load('assets/peca-o.bmp')  # Altera a imagem
                
                # Redesenha a peça
                self.game.tela.add_obj(todas[peca-1].drawing(self.game.tela.window))
            self.game.jogador['jogar'] = False
    
    def pc_jogar(self):
        pass
    
    def add_obj(self, item):
        self.list_obj.append(item)

    def updates(self):

        while self.loop:
            self.events()
            pygame.display.update()
