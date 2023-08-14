class Piece:
    def __init__(self, piece_team, piece_type):
        self.piece_team = piece_team

        self.type = piece_type

    def get_dir(self, from_x, from_y, to_x, to_y):    
        vect_x = to_x - from_x
        vect_y = to_y - from_y
        vect = vect_x, vect_y
        
        return vect

    def get_dist(self, vector):
        vect_x, vect_y = vector
        dist = round((vect_x**2 + vect_y**2)**(1/2))
        return dist
   
    def valid_tile(self, grid, to_x, to_y):
        tile = grid[to_y][to_x]
        if tile is None:
            return True
        if tile.piece_team == self.piece_team:
            return False
        return True


class Rook(Piece):
    def __init__(self, piece_team, piece_type, played=False):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type
        self.played = played

    def valid_move(self, vector):
        vect_x = vector[0]
        vect_y = vector[1]
        
        if vect_x != 0 and vect_y != 0:
            return False
        return True
        
    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector):
        # we need to handle the case where the dist is 1 and there is a piece
        dist = self.get_dist(vector)
        if dist == 1:
            self.played = True
            return True

        # go right
        if vector[0] > 0:
            print('right')
            for tiles in grid[from_y][from_x+1:to_x-1:]:
                if tiles is not None:
                    return False
        
        # go left
        elif vector[0] < 0:
            print('left')
            for tiles in grid[from_y][from_x-1:to_x+1:-1]:
                if tiles is not None:
                    return False
        
        # go below
        elif vector[1] > 0:
            print('under')
            for y in range(from_y+1, to_y):
                if grid[y][from_x] is not None:
                    return False

        # go up
        elif vector[1] < 0:
            for y in range(from_y-1, to_y, -1):
                if grid[y][from_x] is not None:
                    return False
        
        self.played = True
        return True


class Knight(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type


    def valid_move(self, vector):
        # knight moves in a l-shape : 2 to one direction and 1 in another
        if (vector[0] == 1 or vector[0] == -1) and (vector[1] == 2 or vector[1] == -2):
            return True
        
        if (vector[1] == 1 or vector[1] == -1) and (vector[0] == 2 or vector[0] == -2):
            return True
        
        return False

    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector):
        return True


class Bishop(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type

        
    def valid_move(self, vector):    
        vect_x, vect_y = vector
        if abs(vect_x) == abs(vect_y):
            return True

    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector):
        dist = self.get_dist(vector)
        if dist == 1:
            return True
        
        vect_x, vect_y = vector
        # to top left
        if vect_x < 0 and vect_y <0:
            for tile in grid[from_y-1:to_y+1:-1][from_x-1:to_x+1:-1]:
                if tile is not None:
                    return False

        # to top right
        elif vect_y < 0 and vect_x > 0:
            for tile in grid[from_y-1:to_y-1:-1][from_x+1:to_x-1:]:
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
    def __init__(self, piece_team, piece_type, played=False):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type
        self.played = played

        
    def valid_move(self, vector):
        vect_x = vector[0]
        dist = self.get_dist(vector)
        # king can only move one tile at a time
        if dist == 1:
            self.played = True
            return True
        
        # if the king wants to castle
        if abs(vect_x) == 2:
            if not self.played:
                self.played = True
                return True
            else:
                return False
    
    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector):
        dist = self.get_dist(vector)
        if dist == 1:
            return True
        
        # castle to the right
        if vector[0] > 0:
            for tiles in grid[from_y][5:6]:
                if tiles is not None:
                    return False
        
        # castle to the left
        if vector[0] < 0:
            for tiles in grid[from_y][3:1:-1]:
                if tiles is not None:
                    print(tiles)
                    return False
        return ''

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
    
    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector):
        # if 0 then it is a rook move
        if 0 in vector:
            return self.rook_instance.piece_in_between(grid, from_x, from_y, to_x, to_y, vector)
        # if not 0 then bishop move
        return self.bishop_instance.piece_in_between(grid, from_x, from_y, to_x, to_y, vector)

    
class Pawn(Piece):
    def __init__(self, piece_team, piece_type):
        super().__init__(piece_team, piece_type)
        self.piece_team = piece_team
        self.type = piece_type
        self.played = False

        
    def valid_move(self, vector):
        vect_x, vect_y = vector[0], vector[1]
        # white pawns
        if vect_y == -1:
            return self.piece_team == 'w'
        if vect_y == -2:
            if not self.played:
                self.played = True
                return self.piece_team == 'w'
            return False

        # black pawns
        if vect_y == 1:
            return self.piece_team == 'b'
        if vect_y == 2:
            if not self.played:
                self.played = True
                return self.piece_team == 'b'
            return False
        
        # eating pieces
        if abs(vect_x) == abs(vect_y) == 1:
            return True

    def piece_in_between(self, grid, from_x, from_y, to_x, to_y, vector):
        # case where the pawn does not eat
        if not(abs(vector[0]) == abs(vector[1])):
            return True
        
        # case where the pawn tries to play diagnolly
        if grid[to_y][to_x] is not None:
            return True
        
        return False