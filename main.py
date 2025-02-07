from window import Window
from obj import Obj


class Game:

    def __init__(self):

        self.tela = Window(746, 716, "Jogo da Velha", self)

        self.bg = Obj("assets/tabuleiro.bmp", 0, 0)
        self.tela.add_obj(self.bg.drawing(self.tela.window))
        
        self.pecas = (
            Obj("assets/peca-neutra.bmp", 50, 60, 1),    # num_1
            Obj("assets/peca-neutra.bmp", 274, 60, 2),   # num_2
            Obj("assets/peca-neutra.bmp", 500, 60, 3),   # num_3
            Obj("assets/peca-neutra.bmp", 50, 270, 4),   # num_4
            Obj("assets/peca-neutra.bmp", 274, 270, 5),  # num_5
            Obj("assets/peca-neutra.bmp", 500, 270, 6),  # num_6
            Obj("assets/peca-neutra.bmp", 50, 480, 7),   # num_7
            Obj("assets/peca-neutra.bmp", 274, 480, 8),  # num_8
            Obj("assets/peca-neutra.bmp", 500, 480, 9)   # num_9
        )
        
        for peca in self.pecas:
            self.tela.add_obj(peca.drawing(self.tela.window)) # add peça à tela
        
        self.jogador = {'nome': 'Player 1', 'jogar': True, 'jogou': 0}
        self.jogada = 0
        self.msg_player1_win = Obj('assets/images/Player1_venceu.png', 140, 270)
        self.msg_pc_win = Obj('assets/images/pc_venceu.png', 140, 270)           
    def get_peca(self):
        return self.pecas
    
    def get_msg_p1(self):
        return self.msg_player1_win
    
    def get_msg_pc(self):
        return self.msg_pc_win

Game().tela.updates()