from piece import Piece

class Mouvements(Piece):
    def __init__(self):
        self.available_move = []

    def can_move(self):
        for dir in self.dir:
            x, y = tuple(map(lambda i, j: i+j, self.pos, dir))
            if self.grid[x][y] == '':
                self.available_move.append((x, y))
            
            elif self.grid[x][y] in self.white_pieces:
                if self.team == 'white':
                    continue

                self.available_move.append((x, y))
                continue