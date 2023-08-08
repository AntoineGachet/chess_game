from piece import Piece 
from mouvement import Mouvements
from joueurs import Joueurs

class Plateau(Joueurs):
    def __init__(self):
        self.height = 8
        self.width = 8
        self.grid = None
        self.white_pieces= {
            "♚", "♛", "♜", "♝", "♞", "♟",
            }
        self.black_pieces = {
            "♔", "♕", "♖", "♗", "♘", "♙",
            }
    
    def set_grid(self, white_pieces, black_pieces):
        grid = [        
                [pieces for pieces in black_pieces[:8:]],
                [pawns for pawns in black_pieces[8::]],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [pawns for pawns in white_pieces[8::]],
                [pieces for pieces in white_pieces[:8:]],
            ]
        self.grid = grid
        
    def update_grid(self, from_, to_):
        lines = self.grid[::]

        # Update the board with the new piece position
        lines[8 - from_[0]] = lines[8 - from_[0]][:from_[1]] + None + lines[8 - from_[0]][from_[1] + 2:]
        lines[8 - to_[0]] = lines[8 - to_[0]][:to_[1]] + lines[8 - from_[0]][from_[1]:from_[1] + 2] + lines[8 - to_[0]][to_[1] + 2:]

    def display_grid(self):
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        print("    " + "    ".join(files))
        print("  +" + "+".join(["----"] * 8) + "+")
        for rank, row in enumerate(self.grid):
            rank_display = str(8 - rank)
            row_display = " | ".join([piece[1] if piece is not None else "  " for piece in row])
            # [" " if pi]
            print(f"{rank_display} | {row_display} | {rank_display}")
            print("  +" + "+".join(["----"] * 8) + "+")
        print("    " + "    ".join(files))
    
    def __repr__(self):
       return self.display_grid()

grid = Plateau()
