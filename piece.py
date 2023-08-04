from plateau import Plateau

class Piece(Plateau):

    def __init__(self, team, type, pos):
        self.team = team
        self.pos = pos
        self.dir = None
    
    def rook(self):
        self.dir = {
            (u, 0) for u in range(-8, 9)
            } | {
                (0, v) for v in range(-8, 9)
        }

    def knight(self):
        self.dir = {
            (u, v) for u in range(-2, 2, 4) for v in range(-1, 1, 2)
            } | {
            (v, u) for u in range(-2, 2, 4) for v in range(-1, 1, 2)
            }

    def bishop(self):
        self.dir = {
            (u, u) for u in range(-8, 9)
            } | {
                (u, self.width+u) for u in range(-8, 1) 
            } | {
                (u, self.width-u) for u in range(9)
            }

    def king(self):
        self.dir = {
            (u, v) for u in range(-1, 2)
            for v in range(-1, 2)
            }

    def queen(self):
        self.dir = self.bishop() | self.rook()

    def pawn(self):
        if self.team == 'white':
            self.dir = {(2,0), (1, 0)}
        else:
            self.dir = {(-2, 0), (-1, 0)} 