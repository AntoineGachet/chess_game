from piece import Piece

class Mouvements(Piece):
    def __init__(self, move):
        self.available_move = []
        self.move = move
        self.from_move = self.move[0]
        self.to_move = self.move[1]

    def translate_mov(self, pos):
        x, y = pos
        try:
            x =int(x)
        except ValueError:
            x = ord(x) -90
            y = int(y)
            return x, y
        y = ord(y) - 90
        return x, y

    def outside_board(self, x, y):
        if (x or y) >= 9 or (x or y) <= -9:
            return True
        
    def check(self):
            pass 
    
    def wrong_team(self):
        x, y = self.from_move

        if self.grid[x][y].piece_team != self.team:
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

        if self.grid[to_x][to_y] != "":
            if self.grid[to_x][to_y].team == self.team:
                return False

        return True
