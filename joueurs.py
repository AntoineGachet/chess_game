class Joueurs():
    def __init__(self, team):
        self.team = team

    def ask_move(self):
        move_from = tuple(input('which piece do you want to move ?'))
        move_to = tuple(input('where do you want it to go ?'))

        return move_from, move_to
