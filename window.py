import pygame
import random

class Window:

    def __init__(self, x, y, title, game):

        pygame.init()

        self.window = pygame.display.set_mode([x, y])
        self.title = pygame.display.set_caption(title)

        self.loop = True

        self.list_obj = []
        self.play_player1 = True # para controlar quando o player 1 pode jogar
        # Criamos uma instância do jogo para acessar as peças
        self.game = game
        
    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if events.type == pygame.MOUSEBUTTONDOWN: #Consertar aqui: quem clica é só o player 1, o player 2 deve jogar logo em seguida do player 1
                # Percorre todas as peças e verifica qual foi clicada
                for i, peca in enumerate(self.game.get_peca(), start=1):
                    if peca.rect.collidepoint(events.pos):  
                        if self.game.jogador['jogar'] and self.game.jogada < 9:
                            self.n_to_x(i)
                            pygame.time.delay(200) # tempo para o 'pc pensar e jogar'
                            self.pc_jogar()
                        elif self.game.jogador['jogar'] and self.game.jogada == 9:
                            print(f'elif self.game.jogada == {self.game.jogada}')
                            self.n_to_x(i)
                        
                        

    def n_to_x(self, peca):
        if self.game.jogada < 9:
            if self.game.jogador['jogar']:
                todas = self.game.get_peca()
                if todas[peca-1].status == 'n':  # Se a peça for neutra
                    todas[peca-1].status = 'x'   # Marca a peça como 'x'
                    todas[peca-1].image = pygame.image.load('assets/peca-x.bmp')  # Altera a imagem
                    
                    # Redesenha a peça
                    self.game.tela.add_obj(todas[peca-1].drawing(self.game.tela.window))
                self.game.jogador['jogar'] = False
                self.game.jogada += 1
                self.checagem()

        elif self.game.jogada == 9:
            if self.game.jogador['jogar']:
                todas = self.game.get_peca()
                if todas[peca-1].status == 'n':  # Se a peça for neutra
                    todas[peca-1].status = 'x'   # Marca a peça como 'x'
                    todas[peca-1].image = pygame.image.load('assets/peca-x.bmp')  # Altera a imagem
                    
                    # Redesenha a peça
                    self.game.tela.add_obj(todas[peca-1].drawing(self.game.tela.window))
                    self.game.jogada += 1
            self.play_player1 = False    
            self.checagem()
    def n_to_o(self, peca):
        todas = self.game.get_peca()
        if todas[peca-1].status == 'n':  # Se a peça for neutra
            todas[peca-1].status = 'o'   # Marca a peça como 'x'
            todas[peca-1].image = pygame.image.load('assets/peca-o.bmp')  # Altera a imagem
                
            # Redesenha a peça
            self.game.tela.add_obj(todas[peca-1].drawing(self.game.tela.window))
            self.game.jogador['jogar'] = True
            self.game.jogada += 1
            self.checagem()

    
    def pc_jogar(self):
        if self.game.jogada < 9:
            while True:
                o = random.randint(1, 9)
                if self.game.pecas[o - 1].status == 'n':
                    self.n_to_o(o)
                    break
        print(f'jogada = {self.game.jogada}')
    
    def add_obj(self, item):
        self.list_obj.append(item)

    def checagem(self):
        todas = self.game.get_peca()
        # Confere se x venceu
        if todas[0].status == 'x' and todas[1].status == 'x' and todas[2].status == 'x':
            self.player1_venceu()  
        if todas[3].status == 'x' and todas[4].status == 'x' and todas[5].status == 'x':
            self.player1_venceu()
        if todas[6].status == 'x' and todas[7].status == 'x' and todas[8].status == 'x':
            self.player1_venceu()  
        if todas[0].status == 'x' and todas[3].status == 'x' and todas[6].status == 'x':
            self.player1_venceu()  
        if todas[1].status == 'x' and todas[4].status == 'x' and todas[7].status == 'x':
            self.player1_venceu()  
        if todas[2].status == 'x' and todas[5].status == 'x' and todas[8].status == 'x':
            self.player1_venceu()  
        if todas[0].status == 'x' and todas[4].status == 'x' and todas[8].status == 'x':
            self.player1_venceu()  
        if todas[2].status == 'x' and todas[4].status == 'x' and todas[6].status == 'x':
            self.player1_venceu()  
        # Confere se o venceu
        if todas[0].status == 'o' and todas[1].status == 'o' and todas[2].status == 'o':
            self.pc_venceu()  
        if todas[3].status == 'o' and todas[4].status == 'o' and todas[5].status == 'o':
            self.pc_venceu()
        if todas[6].status == 'o' and todas[7].status == 'o' and todas[8].status == 'o':
            self.pc_venceu()  
        if todas[0].status == 'o' and todas[3].status == 'o' and todas[6].status == 'o':
            self.pc_venceu()  
        if todas[1].status == 'o' and todas[4].status == 'o' and todas[7].status == 'o':
            self.pc_venceu()  
        if todas[2].status == 'o' and todas[5].status == 'o' and todas[8].status == 'o':
            self.pc_venceu()  
        if todas[0].status == 'o' and todas[4].status == 'o' and todas[8].status == 'o':
            self.pc_venceu()  
        if todas[2].status == 'o' and todas[4].status == 'o' and todas[6].status == 'o':
            self.pc_venceu()
    
    def player1_venceu(self):
        self.game.tela.add_obj(self.game.msg_player1_win.drawing(self.game.tela.window))
        # pygame.time.delay(2000) # colocar depois do update
        # self.loop = False
        
    def pc_venceu(self):
        self.game.tela.add_obj(self.game.msg_pc_win.drawing(self.game.tela.window))
        # pygame.time.delay(2000) # Isto tem que ir depois da atualização, não antes
        # self.loop = False

    def updates(self):

        while self.loop:
            self.events()
            pygame.display.update()
