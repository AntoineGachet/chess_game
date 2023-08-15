from piece import Rook, Knight, Bishop, King, Queen, Pawn
from joueurs import Joueurs

class Plateau:
    def __init__(self):
        self.grid = [        
                [Rook('b', 'R '), Knight('b', 'N '), Bishop('b', 'B '), Queen('b', 'Q '), King('b', 'K '), Bishop('b', 'B '), Knight('b', 'N '), Rook('b', 'R ')],
                [Pawn('b', 'P '), Pawn('b', 'P '), None, Pawn('b', 'P '), Pawn('b', 'P '), Pawn('b', 'P '), Pawn('b', 'P '), Pawn('b', 'P ')],
                [None, None, None, None, None, None, None, None],
                [None, Pawn('w', 'P '), Pawn('b', 'P ', True, True), None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Pawn('w', 'P '), None, Pawn('w', 'P '), Pawn('w', 'P '), Pawn('w', 'P '), Pawn('w', 'P '), Pawn('w', 'P '), Pawn('w', 'P ')],
                [Rook('w', 'R '), Knight('w', 'N '), Bishop('w', 'B '), Queen('w', 'Q '), King('w', 'K '), Bishop('w', 'B '), Knight('w', 'N '), Rook('w', 'R ')],
            ]
        self.joueur_1 = Joueurs('w')
        self.joueur_2 = Joueurs('b')

    def castle(self, grid, from_x, from_y, to_x, to_y, vector):
        vect_x = vector[0]

        if vect_x < 0:
            if grid[from_y][0].team != grid[from_y][from_x].team:
                print('You cannot castle with an enemy piece')
                return False
            if grid[from_y][0].played:
                print('Your rook was already moved')
                return False
            self.update_grid(from_x, from_y, to_x, from_y)
            self.update_grid(0, from_y, 3, from_y)
            
        elif vect_x > 0:
            if grid[from_y][7].team != grid[from_y][from_x].team:
                print('You cannot castle with an enemy piece')
                return False
            if grid[from_y][7].played:
                print('Your rook was already moved')
                return False
            self.update_grid(from_x, from_y, to_x, from_y)
            self.update_grid(7, from_y, 5, from_y)

        return True
    
    def reset_en_passant(self, joueur):
        for y in range(0, 8):
            for x in range(0, 8):
                tile = self.grid[y][x]
                if type(tile) != type(Pawn('','')):
                    continue
                if tile.team != joueur.team:
                    continue
                tile.en_passant = False
                return 
        return

    def update_grid(self, from_x, from_y, to_x, to_y):
        # Update the board with the new piece position
        self.grid[to_y][to_x] = self.grid[from_y][from_x]
        self.grid[from_y][from_x] = None

    def display_grid(self):
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        print("    " + "    ".join(files))
        print("  +" + "+".join(["----"] * 8) + "+")

        for rank, row in enumerate(self.grid):
            rank_display = str(8 - rank)
            row_display = " | ".join([piece.type if piece is not None else "  " for piece in row])

            print(f"{rank_display} | {row_display} | {rank_display}")
            print("  +" + "+".join(["----"] * 8) + "+")

        print("    " + "    ".join(files))
    
    def translate_move(self, pos):
        x, y = pos
        try:
            x_int = 8 - int(x)
        except ValueError:
            x_int = None
            
        if x_int is None:
            x = ord(x) - 97  # Adjusted for lowercase letters
            y = 8 - int(y)
            
            return x, y
        else:
            x = x_int
            y = ord(y) - 97  # Adjusted for lowercase letters
            
            return x, y
        
    def move(self, team, from_x, from_y, to_x, to_y, vector):
        piece = self.grid[from_y][from_x]
        if piece.team != team:
            print('error: You are trying to move an enemy piece')
            return False

        if not piece.valid_move(vector):
            print("error: this piece cannot move like that")
            return False
    
        if not piece.piece_in_between(self.grid, from_x, from_y, to_x, to_y, vector):
            # the only one returning an empty string is the king trying to castle
            if piece.piece_in_between(self.grid, from_x, from_y, to_x, to_y, vector) == '':
                self.castle(self.grid, from_x, from_y, to_x, to_x, vector)
                return True

            else:
                print("error: your piece cannot jump other pieces")
                return False

        if not piece.valid_tile(self.grid, to_x, to_y):
            print("error: this piece is already occupied by one of your piece")
            return False
                
        self.update_grid(from_x, from_y, to_x, to_y)
        return True

    def __repr__(self):
       return self.display_grid()
