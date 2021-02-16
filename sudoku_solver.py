class Sudoku:

    def __init__(self, s, d=9):
        self.grid = s
        self.vakjes = d

    def is_valid_placement_row_and_column(self, pos, number):  # Check valid placement of a number in x and y direction.
        # row
        for i in range(self.vakjes):
            if self.grid[pos[0]][i] == number:
                return False

        # column
        for i in range(self.vakjes):
            if self.grid[i][pos[1]] == number:
                return False

        return True

    def is_valid_placement_square(self, pos, number):  # Check valid placement of a number in a 3x3 square.
        square_x = pos[1] // 3
        square_y = pos[0] // 3
        for i in range(square_y * 3, square_y * 3 + 3):
            for j in range(square_x * 3, square_x * 3 + 3):
                if self.grid[i][j] == number:
                    return False
        return True

    def find_zero(self):
        for i in range(self.vakjes):
            for j in range(self.vakjes):
                if self.grid[i][j] == 0:
                    return (i, j)

    def solve_sudoku(self):
        zero = self.find_zero()
        if not zero:
            print("is solved")
            return True
        else:
            pos = zero

        for n in range(1, 10):
            if self.is_valid_placement_row_and_column(pos, n) and self.is_valid_placement_square(pos, n):
                self.grid[pos[0]][pos[1]] = n

                if self.solve_sudoku():
                    return True

                self.grid[pos[0]][pos[1]] = 0
                # if the solution cannot be found with the current setup,
                # reset previous number and try again.
        return False

    def __str__(self):  # print sudoku.
        s = ''
        s += '-------------------------\n'
        for i in range(self.vakjes):
            s += '| '
            for j in range(self.vakjes):
                s += str(self.grid[i][j]) + ' '
                if j in [2, 5]:
                    s += '| '
            s += '|\n'
            if i in [2, 5]:
                s += '-------------------------\n'
        s += '-------------------------\n'
        return s


# test
sudoku = Sudoku([[7, 8, 0, 4, 0, 0, 1, 2, 0],
                 [6, 0, 0, 0, 7, 5, 0, 0, 9],
                 [0, 0, 0, 6, 0, 1, 0, 7, 8],
                 [0, 0, 7, 0, 4, 0, 2, 6, 0],
                 [0, 0, 1, 0, 5, 0, 9, 3, 0],
                 [9, 0, 4, 0, 6, 0, 0, 0, 5],
                 [0, 7, 0, 3, 0, 0, 0, 1, 2],
                 [1, 2, 0, 0, 0, 7, 4, 0, 0],
                 [0, 4, 9, 2, 0, 6, 0, 0, 7]])

print(sudoku)
sudoku.solve_sudoku()
print(sudoku)


