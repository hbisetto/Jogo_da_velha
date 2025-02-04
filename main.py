from window import Window
from obj import Obj


class Game:

    def __init__(self):

        self.tela = Window(746, 716, "Jogo da Velha", self)

        self.bg = Obj("assets/tabuleiro.bmp", 0, 0)
        self.tela.add_obj(self.bg.drawing(self.tela.window))

        '''self.num_1 = Obj("assets/peca-neutra.bmp", 50, 60)
        self.tela.add_obj(self.num_1.drawing(self.tela.window))

        self.num_2 = Obj("assets/peca-neutra.bmp", 274, 60)
        self.tela.add_obj(self.num_2.drawing(self.tela.window))
       
        self.num_3 = Obj("assets/peca-neutra.bmp", 500, 60)
        self.tela.add_obj(self.num_3.drawing(self.tela.window))
       
        self.num_4 = Obj("assets/peca-neutra.bmp", 50, 270)
        self.tela.add_obj(self.num_4.drawing(self.tela.window))

        self.num_5 = Obj("assets/peca-neutra.bmp", 274, 270)
        self.tela.add_obj(self.num_5.drawing(self.tela.window))
       
        self.num_6 = Obj("assets/peca-neutra.bmp", 500, 270)
        self.tela.add_obj(self.num_6.drawing(self.tela.window))
        
        self.num_7 = Obj("assets/peca-neutra.bmp", 50, 480)
        self.tela.add_obj(self.num_7.drawing(self.tela.window))

        self.num_8 = Obj("assets/peca-neutra.bmp", 274, 480)
        self.tela.add_obj(self.num_8.drawing(self.tela.window))
       
        self.num_9 = Obj("assets/peca-neutra.bmp", 500, 480)
        self.tela.add_obj(self.num_9.drawing(self.tela.window))'''

        self.pecas = (
            Obj("assets/peca-neutra.bmp", 50, 60),    # num_1
            Obj("assets/peca-neutra.bmp", 274, 60),   # num_2
            Obj("assets/peca-neutra.bmp", 500, 60),   # num_3
            Obj("assets/peca-neutra.bmp", 50, 270),   # num_4
            Obj("assets/peca-neutra.bmp", 274, 270),  # num_5
            Obj("assets/peca-neutra.bmp", 500, 270),  # num_6
            Obj("assets/peca-neutra.bmp", 50, 480),   # num_7
            Obj("assets/peca-neutra.bmp", 274, 480),  # num_8
            Obj("assets/peca-neutra.bmp", 500, 480)   # num_9
        )
        
        for peca in self.pecas:
            self.tela.add_obj(peca.drawing(self.tela.window)) # add peça à tela
        
        self.jogador = {'nome': 'Player 1', 'jogar': True, 'jogou': 0}
                    
    def get_peca(self):
        return self.pecas

Game().tela.updates()