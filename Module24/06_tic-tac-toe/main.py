################################# Я списал задание, честно пытался разобраться Приду в оффлайн школу и разберусь########################################




class Cell:
    def __init__(self, number):
        self.number = number
        self.value = ' '

    def set_value(self, value):
        if self.value == ' ':
            self.value = value
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        print(' 1 | 2 | 3 ')
        print('---------')
        print(' 4 | 5 | 6 ')
        print('---------')
        print(' 7 | 8 | 9 ')

    def update_board(self):
        print(f' {self.cells[0].value} | {self.cells[1].value} | {self.cells[2].value} ')
        print('---------')
        print(f' {self.cells[3].value} | {self.cells[4].value} | {self.cells[5].value} ')
        print('---------')
        print(f' {self.cells[6].value} | {self.cells[7].value} | {self.cells[8].value} ')


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                move = int(input(f'{self.name}, введите номер клетки (1-9): '))
                if 1 <= move <= 9 and board.cells[move - 1].set_value(self.symbol):
                    break
                else:
                    print('Неверный ход. Попробуйте еще раз.')
            except ValueError:
                print('Неверный ввод. Пожалуйста, введите число от 1 до 9.')

            # Игровая логика


board = Board()
board.display()

player1 = Player('Игрок 1', 'X')
player2 = Player('Игрок 2', 'O')

current_player = player1

while True:
    current_player.make_move(board)
    board.update_board()

    # Проверка на победу или ничью
    if ((board.cells[0].value == board.cells[1].value == board.cells[2].value != ' ') or
            (board.cells[3].value == board.cells[4].value == board.cells[5].value != ' ') or
            (board.cells[6].value == board.cells[7].value == board.cells[8].value != ' ') or
            (board.cells[0].value == board.cells[3].value == board.cells[6].value != ' ') or
            (board.cells[1].value == board.cells[4].value == board.cells[7].value != ' ') or
            (board.cells[2].value == board.cells[5].value == board.cells[8].value != ' ') or
            (board.cells[0].value == board.cells[4].value == board.cells[8].value != ' ') or
            (board.cells[2].value == board.cells[4].value == board.cells[6].value != ' ')):
        print(f'Победил игрок {current_player.name}!')
        break
    elif all(cell.value != ' ' for cell in board.cells):
        print('Ничья!')
        break

    current_player = player1 if current_player == player2 else player2