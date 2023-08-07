class Piece:

    def __init__(self, piece_team, pos, front=None):
        self.piece_team = piece_team
        self.pos = pos
        self.front = None
    
    def rook(self):
        dir = {
            (u, 0) for u in range(-8, 9)
            } | {
                (0, v) for v in range(-8, 9)
        }
        return dir

        self.front = "♜" if self.piece_team == "w" else "♖"

    def knight(self):
        dir = {
            (u, v) for u in range(-2, 2, 4) for v in range(-1, 1, 2)
            } | {
            (v, u) for u in range(-2, 2, 4) for v in range(-1, 1, 2)
            }
        
        self.front = "♞" if self.piece_team == "w" else "♘"
        return dir

    def bishop(self):
        dir = {
            (u, u) for u in range(-8, 9)
            } | {
                (u, 8+u) for u in range(-8, 1) 
            } | {
                (u, 8-u) for u in range(9)
            }
        return dir
    
        self.front = "♝" if self.piece_team == "w" else "♗"
        

    def king(self):
        dir = {
            (u, v) for u in range(-1, 2)
            for v in range(-1, 2)
            }
        
        self.front = "♚" if self.piece_team == "w" else "♔"
        return dir
    
    def queen(self):
        dir = self.bishop() | self.rook()

        self.front = "♛" if self.piece_team == "w" else "♕"
        return dir
    
    def pawn(self):
        if self.piece_team == 'white':
            dir = {(2,0), (1, 0)}
        else:
            dir = {(-2, 0), (-1, 0)} 
        
        self.front = "♟" if self.piece_team == "w" else "♙"
        return dir  