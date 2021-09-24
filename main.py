import random
import numpy as np
import pickle


def get_mines(N, M, mines):
    coord = []
    len_coord = 0
    while len_coord != mines:
        x = random.randint(0, N - 1)
        y = random.randint(0, M - 1)
        coord.append((x, y))
        len_coord = len(set(coord))
    return set(coord)


def get_numbers(N, M, coord):
    board = np.zeros(shape=(N,M), dtype=int)

    for row, col in coord:
        if row == 0:
            board[row + 1, col] += 1
            if col == 0:
                board[row, col + 1] += 1
                board[row + 1, col + 1] += 1
            elif col == M - 1:
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
            elif col == M - 1:
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
            elif col == M - 1:
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

    def __init__(self, N, M, board_open, game):
        self.game = game
        self.board_open = board_open
        self.N = N
        self.M = M
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
            elif col == self.M - 1:
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
            elif col == self.M - 1:
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
            elif col == self.M - 1:
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


def print_board(N, M, board_open):
    toplabel = ''
    for i in range(M):
        toplabel += str(i+1) + '   '
    print('     ' + toplabel)
    print('   ' + (4 * M * '-') + '-')
    for row in range(N):
        str_ = '{}|'.format(row + 1)
        for col in range(M):
            str_ += '   ' + str(board_open[row, col])
        print(str_)
    print('')


def creat_board(N, M):
    toplabel = ''
    for i in range(M):
        toplabel += str(i+1) + '   '
    print('     ' + toplabel)
    print('   ' + (4 * M * '-') + '-')
    for row in range(N):
        str_ = '{}|'.format(row + 1)
        for col in range(M):
            str_ += '   ' + '*'
        print(str_)
    print('')

def check_size(text):
    while True:
        print(text)
        try:
            str_ = int(input())
            if str_ < 0 or str_ > 9:
                raise ValueError
            break
        except ValueError:
            print("Wrong Input! Try again. Field size does not exceed 9")
    return str_

def check_mines(N, M):
    size = N * M
    while True:
        print('enter the number of mines:')
        try:
            str_ = int(input())
            if str_ < 0:
                raise ValueError
            if str_ > size:
                raise Exception
            break
        except ValueError:
            print("Wrong Input! Try again")
        except Exception:
            print('Too many mines. Mines should be less than {}'.format(size))
    return str_

def check_answer(text):
    print(text)

    while True:
        try:
            str_ = input().strip()
            if str_ != 'old' and str_ != 'new':
                raise ValueError
        except ValueError:
            print("Wrong Input! Try again")
            continue
        if str_ == 'new':
            N = check_size('enter the number of rows in the field:')
            M = check_size('enter the number of cols in the field:')
            mines = check_mines(N, M)
            # Создание доски для сапёра
            creat_board(N, M)
            count_flag = 0
            coord_flags = []
            # рандомно расставляем мины на поле и запоминаем их координаты
            coord_mines = get_mines(N, M, mines)
            # заполняем поле метками по положению мин
            game = get_numbers(N, M, coord_mines)
            # добавляем мины на поле
            for row, col in coord_mines:
                game[row, col] = -1
            # создаём массив, отражающий ходы игрока
            board_open = np.full((N, M), '*')
        elif str_ == 'old':
            try:
                with open('board_open.pkl', 'rb') as f:
                    board_open = pickle.load(f)
                with open('game.pkl', 'rb') as f:
                    game = pickle.load(f)
                with open('coord_mines.pkl', 'rb') as f:
                    coord_mines = pickle.load(f)
                with open('coord_flags.pkl', 'rb') as f:
                    coord_flags = pickle.load(f)
                with open('count_flag.pkl', 'rb') as f:
                    count_flag = pickle.load(f)
                N = board_open.shape[0]
                M = board_open.shape[1]
                mines = len(coord_mines)
                print_board(N, M, board_open)
            except Exception:
                print('There is no saved game, start a new game')
                continue
        break
    return N, M, board_open, game, mines, coord_mines, count_flag, coord_flags



def main():

    print('Welcome to Python Minesweeper!')

    N, M, board_open, game, mines, coord_mines, count_flag, coord_flags = check_answer('Select action: \n[new] - new game\n[old] - load the game\nyou action:')
    print('You must enter a move in the form: \'1 2 Action\', where Action is Flag or Open')
    while True:
        print('If you want to close the game, enter [end] and the game will be saved')
        print('Type action:')
        input_str = input()

        if input_str == 'end':
            with open('board_open.pkl', 'wb') as f:
                pickle.dump(board_open, f)
            with open('game.pkl', 'wb') as f:
                pickle.dump(game, f)
            with open('coord_mines.pkl', 'wb') as f:
                pickle.dump(coord_mines, f)
            with open('coord_flags.pkl', 'wb') as f:
                pickle.dump(coord_flags, f)
            with open('count_flag.pkl', 'wb') as f:
                pickle.dump(count_flag, f)
            break
        else:
            input_str = input_str.split()
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
                print_board(N, M, board_open)
                break
            # если игрок выбрал нулевую ячейку
            elif game[X, Y] == 0:
                search_point = grid(N, M, board_open, game)
                board_open = search_point.null_cell(X, Y)
            else:
                board_open[X, Y] = game[X, Y]

        sorted_coord_mines = sorted(coord_mines, key=lambda x: (x[0], x[1]))
        sorted_coord_flags = sorted(coord_flags, key=lambda x: (x[0], x[1]))
        # если все координаты флагов равны координатам мин или открыты все ячейки, кроме мин
        if sorted_coord_mines == sorted_coord_flags:
            print("You've won!")
            break
        print_board(N, M, board_open)



if __name__ == "__main__":
    main()