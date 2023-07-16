from piece import Piece 

class Plateau():
    def __init__(self):
        self.cases = [
            [Piece("Tour", "noir"), Piece("Cavalier", "noir"), Piece("Fou", "noir"), Piece("Reine", "noir"),
             Piece("Roi", "noir"), Piece("Fou", "noir"), Piece("Cavalier", "noir"), Piece("Tour", "noir")],
            [Piece("Pion", "noir") for _ in range(8)],
            [" "]*8, [" "]*8, [" "]*8, [" "]*8,
            [Piece("Pion", "blanc") for _ in range(8)],
            [Piece("Tour", "blanc"), Piece("Cavalier", "blanc"), Piece("Fou", "blanc"), Piece("Reine", "blanc"),
             Piece("Roi", "blanc"), Piece("Fou", "blanc"), Piece("Cavalier", "blanc"), Piece("Tour", "blanc")]
        ]
        self.joueur_actif = "blanc"
        self.en_passant = None
        self.roque = {"blanc": {"petit": True, "grand": True},
                      "noir": {"petit": True, "grand": True}}
    
    def display_screen(self):
        for i in range(8):
            for j in range(8):
                if self.cases[i][j] == " ":
                    print(self.cases[i][j] + '  |', end='')
                else:
                    print("n" + "  |", end='')
            print("\n", end="")
            for k in range(8):
                print("____", end="")
            print("\n")

    def move_piece(self, piece, cord):
        pass

    def check_mate(self):
        pass

game = Plateau()
game.display_screen()