from plateau import Plateau
from joueurs import Joueurs
import copy

joueur_1 = Joueurs('w')
joueur_2 = Joueurs('b')

def play(board, joueur):
    # board.display_grid(board.grid)
    moved = False
    board.reset_en_passant(joueur)

    while not moved:
        move_from, move_to = joueur.ask_move()
        from_x, from_y = board.translate_move(move_from)
        to_x, to_y = board.translate_move(move_to)
    
        piece = board.grid[from_y][from_x]
        vector = piece.get_dir(from_x, from_y, to_x, to_y)
        if board.move(board.grid, joueur.team, from_x, from_y, to_x, to_y, vector):
            moved = True

    test_grid = copy.deepcopy(board.grid)
    board.update_grid(test_grid, from_x, from_y, to_x, to_y)
    if board.checked(test_grid, joueur.team):
        play(board, joueur)
    board.update_grid(board.grid, from_x, from_y, to_x, to_y)
    return 
        
            

board = Plateau()
def main(player_1, player_2):
    turn = 1
    checkmated = False
    drawn = False
    while not checkmated and not drawn:
        player, enemy_player = (player_1, player_2) if turn%2 == 0 else (player_2, player_1)
        turn += 1
        board.display_grid(board.grid)
        play(board, player)
        checkmated = board.checkmate(board.grid, enemy_player.team)
    if checkmated is True:
        board.display_grid(board.grid)
        print(f"Well played {player.team}, you delivered checkmate ")
    else:
        print("This game is a draw")

if __name__ == '__main__':
    main(joueur_1, joueur_2)