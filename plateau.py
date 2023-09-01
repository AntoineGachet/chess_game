import copy
from piece import Rook, Knight, Bishop, King, Queen, Pawn
from joueurs import Joueurs

class Plateau:
    def __init__(self):
        self.grid = [        
                [Rook('b', '♖ '), Knight('b', '♘ '), Bishop('b', '♗ '), Queen('b', '♕ '), King('b', '♔ '), Bishop('b', '♗ '), Knight('b', '♘ '), Rook('b', '♖ ')],
                [Pawn('b', '♙ '), Pawn('b', '♙ '), None, Pawn('b', '♙ '), None, Pawn('b', '♙ '), Pawn('b', '♙ '), Pawn('b', '♙ ')],
                [None, None, None, None, None, None, None, None],
                [None, Pawn('w', '♟ '), Pawn('b', '♙ ', True, True), None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Pawn('w', '♟ '), None, Pawn('w', '♟ '), Pawn('w', '♟ '), Pawn('w', '♟ '), None, None, Pawn('w', '♟ ')],
                [Rook('w', '♜ '), Knight('w', '♞ '), Bishop('w', '♝ '), Queen('w', '♛ '), King('w', '♚ '), Bishop('w', '♝ '), Knight('w', '♞ '), Rook('w', '♜ ')],
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
            self.update_grid(grid, from_x, from_y, to_x, from_y)
            self.update_grid(grid, 0, from_y, 3, from_y)

        elif vect_x > 0:
            if grid[from_y][7].team != grid[from_y][from_x].team:
                print('You cannot castle with an enemy piece')
                return False
            if grid[from_y][7].played:
                print('Your rook was already moved')
                return False
            self.update_grid(grid, from_x, from_y, to_x, from_y)
            self.update_grid(grid, 7, from_y, 5, from_y)

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
    
    def get_king_pos(self, grid, team):
        for y in range(0, 8):
            for x in range(0, 8):
                if grid[y][x] is None:
                    continue
                if type(grid[y][x]) != type(King('', '')):
                    continue
                if grid[y][x].team == team:
                    return x, y

    def checked(self, grid, team, king_x=None, king_y=None):
        enemy_team = 'b' if team == 'w' else 'w'
        if king_x is None and king_y is None:
            king_x, king_y = self.get_king_pos(grid, team)
        for y in range(0, 8):
            for x in range(0, 8):
                if grid[y][x] is None:
                    continue
                elif grid[y][x].team == enemy_team:
                    vector = grid[y][x].get_dir(x, y, king_x, king_y)
                    if self.move(grid, enemy_team, x, y, king_x, king_y, vector):
                        return True
        return False

    def checkmate(self, grid, team):
        king_x, king_y = self.get_king_pos(grid, team)
        for y in range(0, 8):
            for x in range(0, 8):
                if grid[y][x] is None:
                    continue
                if grid[y][x].team != team:
                    continue

                if self.find_valid_move(grid, team, grid[y][x], x, y, king_x, king_y):
                    return False
        return True

    def find_valid_move(self, grid, team, piece, x, y, king_x, king_y):
        moves = piece.generate_moves(x, y)
        for to_x, to_y in moves:
            test_grid = copy.deepcopy(grid)
            vect = piece.get_dir(x, y, to_x, to_y)
            if not self.move(test_grid, team, x, y, to_x, to_y, vect):
                continue
            vect = piece.get_dir(x, y, to_x, to_y)
            self.update_grid(test_grid, x, y, to_x, to_y)
            if type(grid[y][x]) == type(King('','')):
                if not self.checked(test_grid, team, to_x, to_y):
                    return True
            elif not self.checked(test_grid, team, king_x, king_y):
                print(x, y)
                print(to_x, to_y)
                return True
        return False

    def update_grid(self, grid, from_x, from_y, to_x, to_y):
        # Update the board with the new piece position
        # self.display_grid(grid)
        if (to_x, to_y) == (2, 3) or (from_x, from_y) == (2, 3):
            print(from_x, from_y)
            print(to_x, to_y)
        grid[to_y][to_x] = self.grid[from_y][from_x]
        grid[from_y][from_x] = None
        # self.display_grid(grid)
        

    def display_grid(self, grid):
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        print("    " + "    ".join(files))
        print("  +" + "+".join(["----"] * 8) + "+")

        for rank, row in enumerate(grid):
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
    
    def outside_board(self, to_x, to_y):
        if 0 <= to_x <= 7 and 0 <= to_y <= 7:
            return False
        return True
        
    def move(self, grid, team, from_x, from_y, to_x, to_y, vector):
        piece = self.grid[from_y][from_x]

        if piece is None:
            print('error: you must move a piece')
            return False

        if (from_x, from_y) == (to_x, to_y):
            print('error: you must move your piece')
            return False

        if piece.team != team:
            print('error: You are trying to move an enemy piece')
            return False
        
        if self.outside_board(to_x, to_y):
            print('error: you cannot move your piece outside the board')
            return False

        if not piece.valid_move(vector):
            print("error: this piece cannot move like that")
            return False
    
        if not piece.piece_in_between(grid, from_x, from_y, to_x, to_y, vector):
            #  the only one returning an empty string is the king trying to castle
            if piece.piece_in_between(self.grid, from_x, from_y, to_x, to_y, vector) == '':
                self.castle(self.grid, from_x, from_y, to_x, to_x, vector)
                return True

            else:
                print("error: your piece cannot jump other pieces")
                return False

        if not piece.valid_tile(self.grid, to_x, to_y):
            print("error: this piece is already occupied by one of your piece")
            return False

        return True

    def __repr__(self):
       return self.display_grid(self.grid)
