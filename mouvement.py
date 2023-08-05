from piece import Piece

class Mouvements(Piece):
    def __init__(self, move):
        self.available_move = []
        self.move = move

    def translate_mov(self):
        x, y = self.move
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

    def can_move(self):
        # get the new positions
        x, y = self.translate_move()
        vector = tuple(map(lambda i, j: i - j, (x,y), self.move))

        if self.outside_board(x, y):
            return False

        if not vector in self.dir:
            return False

        if self.grid[x][y] != "":
            if self.grid[x][y].team == self.team:
                return False

        return True
