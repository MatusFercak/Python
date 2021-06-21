
# Last update: 21.6.2021

class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __str__(self):
        line = '-+-+-\n'
        b = f'{self.board[0]}|{self.board[1]}|{self.board[2]}\n' + line
        b += f'{self.board[3]}|{self.board[4]}|{self.board[5]}\n' + line
        b += f'{self.board[6]}|{self.board[7]}|{self.board[8]}\n'
        return b

    def clear_board(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def is_empty(self, index):
        if self.board[index-1] == ' ':
            return True
        return False

    def set_char(self, index, char):
        if self.board[index - 1] == ' ':
            self.board[index-1] = char
        return

    def is_end(self):
        for i in self.board:
            if i == ' ':
                return True
        return False

    def who_win(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != ' ':
            return self.board[0]
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != ' ':
            return self.board[3]
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != ' ':
            return self.board[6]
        elif self.board[0] == self.board[3] == self.board[6] and self.board[0] != ' ':
            return self.board[0]
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ':
            return self.board[4]
        elif self.board[2] == self.board[5] == self.board[8] and self.board[8] != ' ':
            return self.board[2]
        elif self.board[0] == self.board[4] == self.board[8] and self.board[8] != ' ':
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] and self.board[6] != ' ':
            return self.board[2]
        return 0


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        p = f'Name: {self.name}\n'
        p += f'Score: {self.score}\n'
        return p

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def add_score(self):
        self.score += 1


def game(num_of_games):
    board = Board()

    player_1 = Player(input('Set name for player 1: '))
    player_2 = Player(input('Set name for player 2: '))
    print(10*'-')

    for i in range(1, num_of_games+1):
        print(f'{i}. game\n')
        print('1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n')
        print('Type a number where you want to start.\n'+9*'-')

        turn = True  # switching players -> line 114
        while board.is_end():
            if board.who_win() != 0:

                if board.who_win() == 'X':
                    player_1.add_score()
                    print(f'{player_1.get_name()} win!')
                else:
                    player_2.add_score()
                    print(f'{player_2.get_name()} win!')
                print(
                    f'{player_1.get_name()} {player_1.get_score()} / {player_2.get_score()} {player_2.get_name()}\n', 9*'-')
                break

            name = player_1.get_name() if turn else player_2.get_name()

            index = int(input(f'{name} your turn: '))

            if index not in [i for i in range(1, 10)]:
                print('This position is not valid!')
                continue

            if not board.is_empty(index):
                print('This position is taken!')
                continue

            board.set_char(index, 'X' if turn else 'O')
            print(board)
            turn = not turn

            if not board.is_end():
                print('DRAW\n', 9*'-')
        board.clear_board()


def main():
    game(3)


if __name__ == '__main__':
    main()
