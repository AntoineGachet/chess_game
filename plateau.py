from piece import Rook, Knight, Bishop, King, Queen, Pawn
from joueurs import Joueurs

class Plateau:
    def __init__(self):
        self.grid = [        
                [None, None, None, None, None, Pawn('b', 'P '), None, None],
                [None, None, None, None, None, None, None, None],
                [None, Pawn('b', 'P '), None, None, None, None, Pawn('b', 'P '), None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, Pawn('b', 'P '), None, None, None, None],
                [None, Pawn('b', 'P '), None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Rook('w', 'r '), None, None, None, King('b', 'k '), None, None, Rook('b', 'r ', True)],
            ]
        self.joueur_1 = Joueurs('w')
        self.joueur_2 = Joueurs('b')

    def castle(self, grid, from_x, from_y, to_x, to_y, vector):
        vect_x = vector[0]

        if vect_x < 0:
            if grid[from_y][0].piece_team != grid[from_y][from_x].piece_team:
                print('You cannot castle with an enemy piece')
                return False
            if grid[from_y][0].played:
                print('Your rook was already moved')
                return False
            self.update_grid(from_x, from_y, to_x, from_y)
            self.update_grid(0, from_y, 3, from_y)
            
        elif vect_x > 0:
            if grid[from_y][7].piece_team != grid[from_y][from_x].piece_team:
                print('You cannot castle with an enemy piece')
                return False
            if grid[from_y][7].played:
                print('Your rook was already moved')
                return False
            self.update_grid(from_x, from_y, to_x, from_y)
            self.update_grid(7, from_y, 5, from_y)
        return True

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
    
    def play(self):
        self.display_grid()
        move_from, move_to = self.joueur_1.ask_move()
        from_x, from_y = self.translate_move(move_from)
        to_x, to_y = self.translate_move(move_to)
        piece = self.grid[from_y][from_x]
        vector = piece.get_dir(from_x, from_y, to_x, to_y)
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

    def __repr__(self):
       return self.display_grid()

board = Plateau()
while True:
    board.play()