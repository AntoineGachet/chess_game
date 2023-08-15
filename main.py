from plateau import Plateau
from joueurs import Joueurs

joueur_1 = Joueurs('w')
joueur_2 = Joueurs('b')

def play(board, joueur):
    board.display_grid()
    moved = False
    board.reset_en_passant(joueur)

    while not moved:
        move_from, move_to = joueur.ask_move()
        from_x, from_y = board.translate_move(move_from)
        to_x, to_y = board.translate_move(move_to)
    
        piece = board.grid[from_y][from_x]
        vector = piece.get_dir(from_x, from_y, to_x, to_y)
        if board.move(joueur.team, from_x, from_y, to_x, to_y, vector):
            moved = True
        
            

board = Plateau()
def main():
    n = 0
    while True:
        joueur = joueur_1 if n%2 == 0 else joueur_2
        n+=1
        play(board, joueur)

if __name__ == '__main__':
    main()