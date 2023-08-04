from piece import Piece 

class Plateau():
    def __init__(self):
        self.height = 8
        self.width = 8
        self.grid = None
    
    def set_grid(self):
        grid = [['' for _ in range(self.width)] for _ in range(self.height)]
        self.grid = grid
        
    
    def display_grid(self):
        for column in self.grid:
            print(column)
    
    def __repr__(self):
       return f'{self.grid}' 

grid = Plateau()

grid.set_grid()
grid.display_grid()