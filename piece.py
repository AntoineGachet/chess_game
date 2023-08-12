class Piece:
    def __init__(self, piece_team, piece_type):
        self.piece_team = piece_team

        self.type = piece_type

    def get_dir(self, from_x, from_y, to_x, to_y):    
        vect_x = to_x - from_x
        vect_y = to_y - from_y

        vect = vect_x, vect_y
        dist = round((vect_x**2 + vect_y**2)**(1/2))
        return vect, dist
    
    def eat_piece(self, to_x, to_y):
        tile = [to_y][to_x]
        if tile != None:
            if tile.piece_team == self.piece_team:
                return False
            return True


class Rook(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team

        self.type = piece_type

    def valid_move(self, vector):
        vect_x = vector[0]
        vect_y = vector[1]
        
        if vect_x != 0 and vect_y != 0:
            return False
        return True
        
    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector, dist):
        # we need to handle the case where the dist is 1 and there is a piece
        if dist == 1:
            return True
        # to the right of the rook
        if vector[0] > 0:
            for tiles in grid[from_y][from_x+1:to_x-1:]:
                if tiles != None:
                    return False
        
        # to the left of the rook
        elif vector[0] < 0:
            for tiles in grid[from_y][from_x-1:to_x+1:-1]:
                if tiles != None:
                    return False
        
        # under the rook
        elif vector[1] > 0:
            for tiles in grid[from_y+1:to_y-1][from_x]:
                if tiles != None:
                    return False

        # on top of the rook
        elif vector[1] < 0:
            for tiles in grid[from_y-1:to_y+1:-1][from_x]:
                if tiles != None:
                    return False
                
        return True


class Knight(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type


    def valid_move(self, vector):
        if vector[0] == 1 or vector[0] == -1 and vector[1] == 2 or vector[1] == -2:
            return True
        
        if vector[1] == 1 or vector[1] == -1 and vector[0] == 2 or vector[0] == -2:
            return True
        
        return False

    def piece_in_between(self):
        True


class Bishop(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type

        
    def valid_move(self, vector):    
        vect_x, vect_y = vector
        if abs(vect_x) == abs(vect_y):
            return True

    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector, dist):
        if dist == 1:
            return True
        
        vect_x, vect_y = vector
        # to top left
        if vect_x < 0 and vect_y <0:
            for tile in grid[from_y-1:to_y+1:-1][from_x-1:to_x+1:-1]:
                if tile != None:
                    return False

        # to top right
        elif vect_y < 0 and vect_x > 0:
            for tile in grid[from_y-1:to_y+1:-1][from_x+1:to_x-1:]:
                if tile != None:
                    return False
        # to bottom left
        elif vect_y > 0 and vect_x < 0:
            for tile in grid[from_y+1:to_y-1][from_x-1:to_x+1:-1]:
                if tile != None:
                    return False

        # to bottom right 
        elif vect_y > 0 and vect_x > 0:
            for tile in grid[from_y+1:to_y-1][from_x+1:to_x-1]:
                if tile != None:
                    return False
        
        return True


class King(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type

        
    def valid_move(self, dist):
        if dist == 1:
            return True
    
    def piece_in_between(self):
        return True


class Queen(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type

        self.bishop_instance = Bishop(piece_team, 'n')
        self.rook_instance = Rook(piece_team, 'b')

    def valid_move(self, vector):
        # valid move if it moves like a bishop
        return (self.bishop_instance.valid_move(vector) or self.rook_instance.valid_move(vector))
    
    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector, dist):
        # if 0 then it is a rook move
        if 0 in vector:
            return self.rook_instance.piece_in_between(grid, from_x, from_y, to_x, to_y, vector, dist)
        # if not 0 then bishop move
        return self.bishop_instance.piece_in_between(grid, from_x, from_y, to_x, to_y, vector, dist)

    
class Pawn(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type

        
    def get_dir(self):    
        if self.piece_team == 'w':     
            dir = {(2,0), (1, 0)}
        else:
            dir = {(-2, 0), (-1, 0)} 

        return dir
    
    def get_front(self):
        front = "wP" if self.piece_team == "w" else "bP"
        return front
