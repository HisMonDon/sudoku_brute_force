from time import sleep
from colorama import Fore, Style, init

init()

def display_sudoku(board, fixed_positions):
    output = []
    for row_index, row in enumerate(board):
        line = []
        for col_index, num in enumerate(row):
            if (row_index, col_index) in fixed_positions:
                line.append(Fore.YELLOW + str(num) + Style.RESET_ALL if num != 0 else ".")
            else:
                line.append(Fore.CYAN + str(num) + Style.RESET_ALL if num != 0 else ".")
        output.append(" ".join(line))
    return "\n".join(output)

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[r][col] for r in range(9)]:
        return False
    box_row, box_col = row - row % 3, col - col % 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False
    return True

def find_empty_position(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def solve_sudoku(board, fixed_positions):
    empty_pos = find_empty_position(board)
    if not empty_pos:
        return True

    row, col = empty_pos

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            print("\033[H\033[J", end="")
            print(display_sudoku(board, fixed_positions))
            sleep(0.01)

            if solve_sudoku(board, fixed_positions):
                return True

        board[row][col] = 0
        print("\033[H\033[J", end="")
        print(display_sudoku(board, fixed_positions))
        sleep(0.005)

    return False

puzzle = [
    [5, 0, 0, 0, 7, 0, 0, 0, 3],
    [0, 0, 3, 2, 0, 0, 8, 0, 0],
    [0, 8, 0, 0, 0, 9, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 5, 0],
    [0, 7, 0, 6, 0, 8, 0, 9, 0],
    [0, 9, 0, 0, 0, 0, 7, 0, 0],
    [3, 0, 0, 5, 0, 0, 0, 4, 0],
    [0, 0, 6, 0, 0, 4, 5, 0, 0],
    [4, 0, 0, 0, 3, 0, 0, 0, 9]
]


fixed_positions = {(r, c) for r in range(9) for c in range(9) if puzzle[r][c] != 0}
print("Solving Sudoku...\n")
print(display_sudoku(puzzle, fixed_positions))
sleep(1)
print("Importing Modules... \n")
sleep(1)
print("Setting up functions... \n")
sleep(0.4)
print("Initiating startup... \n")
solve_sudoku(puzzle, fixed_positions)
print("\nSolved Sudoku:")
print(display_sudoku(puzzle, fixed_positions))
