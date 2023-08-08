from piece import Piece

class Mouvements(Piece):
    def __init__(self, move, turn, plateau_instance):
        self.move = move
        self.from_move = self.move[0]
        self.to_move = self.move[1]
        self.turn = 'b' if turn%2 == 1 else 'w'
        self.plateau_instance = plateau_instance

    def translate_mov(self, pos):
        x, y = pos
        try:
            x_int = int(x)
        except ValueError:
            x_int = None
            
        if x_int is None:
            x = ord(x) - 97  # Adjusted for lowercase letters
            y = int(y)
        else:
            x = x_int
            y = ord(y) - 97  # Adjusted for lowercase letters
        return x, y

    def outside_board(self, x, y):
        if (x or y) >= 9 or (x or y) <= -9:
            return True
        
    def check(self):
            pass 
    
    def wrong_team(self):
        x, y = self.from_move
        print(self.plateau_instance.grid,'je ne comprends pas')
        if self.plateau_instance.grid[x][y].piece_team != self.turn:
            return False

    def can_move(self, from_x, from_y, to_x, to_y):
        # get the new positions
        from_x, from_y = self.translate_mov(self.from_move)
        to_x, to_y = self.translate_mov(self.to_move)

        vector = (to_x-from_x, to_y-from_y)

        if self.outside_board(to_x, to_y):
            return False

        if self.wrong_team():
            return False

        if self.check():
            pass

        if not vector in self.dir:
            return False

        if self.grid[to_x][to_y] != None:
            if self.grid[to_x][to_y].piece_team == self.turn:
                return False

        return True
