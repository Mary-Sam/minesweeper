import random
import numpy as np


def get_mines(N, mines):
    coord = []
    len_coord = 0
    while len_coord != mines:
        x = random.randint(0, N - 1)
        y = random.randint(0, N - 1)
        coord.append((x, y))
        len_coord = len(set(coord))
    return set(coord)


def get_numbers(N, coord):
    board = np.zeros(shape=(N,N), dtype=int)

    for row, col in coord:
        if row == 0:
            board[row + 1, col] += 1
            if col == 0:
                board[row, col + 1] += 1
                board[row + 1, col + 1] += 1
            elif col == N - 1:
                board[row, col - 1] += 1
                board[row + 1, col - 1] += 1
            else:
                board[row , col - 1] += 1
                board[row + 1, col - 1] += 1
                board[row, col + 1] += 1
                board[row + 1, col + 1] += 1
        elif row == N - 1:
            board[row - 1, col] += 1
            if col == 0:
                board[row - 1, col + 1] += 1
                board[row, col + 1] += 1
            elif col == N - 1:
                board[row, col - 1] += 1
                board[row - 1, col - 1] += 1
            else:
                board[row, col - 1] += 1
                board[row - 1, col - 1] += 1
                board[row - 1, col + 1] += 1
                board[row, col + 1] += 1
        else:
            board[row - 1, col] += 1
            board[row + 1, col] += 1
            if col == 0:
                board[row - 1, col + 1] += 1
                board[row, col + 1] += 1
                board[row + 1, col + 1] += 1
            elif col == N - 1:
                board[row - 1, col - 1] += 1
                board[row, col - 1] += 1
                board[row + 1, col - 1] += 1
            else:
                board[row - 1, col + 1] += 1
                board[row, col + 1] += 1
                board[row + 1, col + 1] += 1
                board[row - 1, col - 1] += 1
                board[row, col - 1] += 1
                board[row + 1, col - 1] += 1
    return board


class grid():

    def __init__(self, N, board_open, game):
        self.game = game
        self.board_open = board_open
        self.N = N
        self.coord_null_point = []

    def checker(self, row, col):
        self.board_open[row, col] = self.game[row, col]
        if self.game[row, col] == 0 and (row, col) not in self.coord_null_point:
            self.null_cell(row, col)

    def null_cell(self, row, col):
        self.coord_null_point.append((row, col))
        self.board_open[row, col] = self.game[row, col]
        if row == 0:
            self.checker(row+1, col)
            if col == 0:
                self.checker(row, col + 1)
                self.checker(row + 1, col + 1)
            elif col == self.N - 1:
                self.checker(row, col - 1)
                self.checker(row + 1, col - 1)
            else:
                self.checker(row, col - 1)
                self.checker(row + 1, col - 1)
                self.checker(row, col + 1)
                self.checker(row + 1, col + 1)
        elif row == self.N - 1:
            self.checker(row - 1, col)
            if col == 0:
                self.checker(row - 1, col + 1)
                self.checker(row, col + 1)
            elif col == self.N - 1:
                self.checker(row, col - 1)
                self.checker(row - 1, col - 1)
            else:
                self.checker(row, col - 1)
                self.checker(row - 1, col - 1)
                self.checker(row - 1, col + 1)
                self.checker(row, col + 1)
        else:
            self.checker(row - 1, col)
            self.checker(row + 1, col)
            if col == 0:
                self.checker(row - 1, col + 1)
                self.checker(row, col + 1)
                self.checker(row + 1, col + 1)
            elif col == self.N - 1:
                self.checker(row - 1, col - 1)
                self.checker(row, col - 1)
                self.checker(row + 1, col - 1)
            else:
                self.checker(row - 1, col + 1)
                self.checker(row, col + 1)
                self.checker(row + 1, col + 1)
                self.checker(row - 1, col - 1)
                self.checker(row, col - 1)
                self.checker(row + 1, col - 1)
        return self.board_open


def print_board(N, board_open):
    toplabel = ''
    for i in range(N):
        toplabel += str(i+1) + '   '
    print('     ' + toplabel)
    print('   ' + (4 * N * '-') + '-')
    for row in range(N):
        str_ = '{}|'.format(row + 1)
        for col in range(N):
            str_ += '   ' + str(board_open[row, col])
        print(str_)
    print('')


def creat_board(N):
    toplabel = ''
    for i in range(N):
        toplabel += str(i+1) + '   '
    print('     ' + toplabel)
    print('   ' + (4 * N * '-') + '-')
    for row in range(N):
        str_ = '{}|'.format(row + 1)
        for col in range(N):
            str_ += '   ' + '*'
        print(str_)
    print('')


def main():
    print('Welcome to Python Minesweeper! You must enter a move in the form: \'1 2 Action\', where Action is Flag or Open')

    N = 5
    # vertical = 3
    mines = 5
    # Создание доски для сапёра
    creat_board(N)
    count_flag = 0
    coord_flags = []

    # рандомно расставляем мины на поле и запоминаем их координаты
    coord_mines = get_mines(N, mines)
    # заполняем поле метками по положению мин
    game = get_numbers(N, coord_mines)
    # добавляем мины на поле
    for row, col in coord_mines:
        game[row, col] = -1
    # создаём массив, отражающий ходы игрока
    board_open = np.full((N,N), '*')

    while True:

        print('Type action:')
        input_str = input().split()

        # если длина ввода больше положенной [X, Y, Action] - 3
        if len(input_str) != 3:
            print("Wrong Input! Try again")
            continue
        try:
            X = int(input_str[0]) - 1
            Y = int(input_str[1]) - 1
        # если координаты точки некорректы
        except ValueError:
            print("Wrong Input! Try again")
            continue
        action = input_str[2]
        # если действие некорректно
        if action != 'Flag' and action != 'Open':
            print("Wrong Input! Try again")
            continue
        # вывод команды в консоль
        # print(' '.join(input_str))

        # установить флаг на соответвующую клетку, пометив её как предположительно содержащую бомбу
        if action == 'Flag':
            # ячейка уже была помечена как флаг
            # снять флаг
            if board_open[X, Y] == 'F':
                count_flag -= 1
                board_open[X, Y] = '*'
                coord_flags.remove((X, Y))
                # print("Flag already set")
                # continue
            # значение ячейки уже известно
            elif board_open[X, Y] != '*':
                print("Value already known")
                continue
            # количество флагов превышает количество мин
            elif count_flag == mines:
                print("Flags finished")
                continue
            # добавить флаг на игровое поле
            else:
                count_flag += 1
                board_open[X, Y] = 'F'
                coord_flags.append((X, Y))
                # continue

        elif action == 'Open':
            # если игрок выбрал ячейку с миной
            if game[X, Y] == -1:
                print("Landed on a mine. Game over.")
                for X_m, Y_m in coord_mines:
                    board_open[X_m, Y_m] = 'M'
                print_board(N, board_open)
                break
            # если игрок выбрал нулевую ячейку
            elif game[X, Y] == 0:
                search_point = grid(N, board_open, game)
                board_open = search_point.null_cell(X, Y)
            else:
                board_open[X, Y] = game[X, Y]

        sorted_coord_mines = sorted(coord_mines, key=lambda x: (x[0], x[1]))
        sorted_coord_flags = sorted(coord_flags, key=lambda x: (x[0], x[1]))
        # а если три мины под флагом, а две неоткрытые ячейки - мины??????????
        # (sum_board_open + count_flag) == mines
        # если все координаты флагов равны координатам мин или открыты все ячейки, кроме мин
        if sorted_coord_mines == sorted_coord_flags:
            print("You've won!")
            break
        print_board(N, board_open)


if __name__ == "__main__":
    main()
