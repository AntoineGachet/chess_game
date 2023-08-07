from plateau import Plateau
from piece import Piece
from mouvement import Mouvements
from joueurs import Joueurs

check_mated = False

black = [
    Piece('b', ('a', 8)).rook(),
    Piece('b', ('b', 8)).knight(),
    Piece('b', ('c', 8)).bishop(),
    Piece('b', ('d', 8)).king(),
    Piece('b', ('e', 8)).queen(),
    Piece('b', ('e', 8)).bishop(),
    Piece('b', ('e', 8)).knight(),
    Piece('b', ('e', 8)).rook(),
    Piece('b', ('a', 7)).pawn(),
    Piece('b', ('b', 7)).pawn(),
    Piece('b', ('c', 7)).pawn(),
    Piece('b', ('d', 7)).pawn(),
    Piece('b', ('e', 7)).pawn(),
    Piece('b', ('f', 7)).pawn(),
    Piece('b', ('g', 7)).pawn(),
]

white = [
    Piece('w', ('a', 8)).rook(),
    Piece('w', ('b', 8)).knight(),
    Piece('w', ('c', 8)).bishop(),
    Piece('w', ('d', 8)).king(),
    Piece('w', ('e', 8)).queen(),
    Piece('w', ('e', 8)).bishop(),
    Piece('w', ('e', 8)).knight(),
    Piece('w', ('e', 8)).rook(),
    Piece('w', ('a', 7)).pawn(),
    Piece('w', ('b', 7)).pawn(),
    Piece('w', ('c', 7)).pawn(),
    Piece('w', ('d', 7)).pawn(),
    Piece('w', ('e', 7)).pawn(),
    Piece('w', ('f', 7)).pawn(),
    Piece('w', ('g', 7)).pawn(),
]

board = Plateau()
board.set_grid()
player_1 = Joueurs('w')
player_2 = Joueurs('b')

def main():
    while not check_mated:
        move_1 = player_1.ask_move()
        mouvements = Mouvements(move_1)
        x_1, y_1 = mouvements.translate_mov((move_1[0]))
        x_2, y_2 =mouvements.translate_mov(move_1[1])
        mouvements.can_move(x_1, y_1, x_2, y_2)
        board.update_grid(move_1[0], move_1[1])
        board.display_grid()

        move_2 = player_2.ask_move()
        mouvements = Mouvements(move_2)
        x_1, y_1 = mouvements.translate_mov(move_2[0])
        x_2, y_2 =mouvements.translate_mov(move_2[1])
        mouvements.can_move(x_1, y_1, x_2, y_2)
        board.update_grid(move_2[0], move_2[1])
        board.display_grid()

if __name__ == '__main__':
    main()
