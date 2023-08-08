from plateau import Plateau
from piece import Piece
from mouvement import Mouvements
from joueurs import Joueurs

check_mated = False

black = [
    Piece('b').rook(),
    Piece('b').knight(),
    Piece('b').bishop(),
    Piece('b').king(),
    Piece('b').queen(),
    Piece('b').bishop(),
    Piece('b').knight(),
    Piece('b').rook(),
    Piece('b').pawn(),
    Piece('b').pawn(),
    Piece('b').pawn(),
    Piece('b').pawn(),
    Piece('b').pawn(),
    Piece('b').pawn(),
    Piece('b').pawn(),
    Piece('b').pawn(),
]

white = [
    Piece('w').rook(),
    Piece('w').knight(),
    Piece('w').bishop(),
    Piece('w').king(),
    Piece('w').queen(),
    Piece('w').bishop(),
    Piece('w').knight(),
    Piece('w').rook(),
    Piece('w').pawn(),
    Piece('w').pawn(),
    Piece('w').pawn(),
    Piece('w').pawn(),
    Piece('w').pawn(),
    Piece('w').pawn(),
    Piece('w').pawn(),
    Piece('w').pawn(),
]

board = Plateau()
board.set_grid(white, black)
player_1 = Joueurs('w')
player_2 = Joueurs('b')

def main():
    turn = 0
    while not check_mated:
        if turn%2 == 0:
            board.display_grid()
            move_1 = player_1.ask_move()
            mouvements = Mouvements(move_1, turn, board)
            x_1, y_1 = mouvements.translate_mov((move_1[0]))
            x_2, y_2 =mouvements.translate_mov(move_1[1])
            mouvements.can_move(x_1, y_1, x_2, y_2)
            board.update_grid(move_1[0], move_1[1])
            board.display_grid()

            turn +=1

        else:
            move_2 = player_2.ask_move()
            mouvements = Mouvements(move_2, turn)
            x_1, y_1 = mouvements.translate_mov(move_2[0])
            x_2, y_2 =mouvements.translate_mov(move_2[1])
            mouvements.can_move(x_1, y_1, x_2, y_2)
            board.update_grid(move_2[0], move_2[1])
            board.display_grid()

            turn +=1

if __name__ == '__main__':
    main()
