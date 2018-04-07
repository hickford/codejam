from sys import stderr, exit

def read_two_int():
    return [int(x) for x in input().split()]

def solved(board):
    return all(all(row) for row in board)

def first_empty_column(board):
    for c in range(5):
        for row in range(4):
            if not board[row][c]:
                return c

def column_to_target(board):
    return min(first_empty_column(board) + 1, 3)

def row_to_target(board):
    for c in range(5):
        if not board[0][c]:
            return 1
        if not board[3][c]:
            return 2
    return 1

T = int(input())
for case in range(1, T+1):
    A = float(input())
    print("2 2")
    x_offset, y_offset = read_two_int()
    board = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    while not solved(board):
        y = column_to_target(board)
        x = row_to_target(board)
        print("{} {}".format(x + x_offset, y + y_offset))
        x, y = read_two_int()
        if x == y == -1:
            exit()
        if x == y == 0:
            break
        board[x - x_offset][y - y_offset] += 1
