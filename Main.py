boards = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

def printboard(board):

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------------------------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" |   ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + "  ", end="")


def box_empty(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)

    return None

def valid_row(board, num, pos):

    #ROW
    for x in range(9):
        if board[pos[0]][x] == num and pos[1] != x:
            return False

    return True

def valid_column(board, num, pos):

    #COLUMN
    for y in range(9):
        if board[y][pos[1]] == num and pos[0] != y:
            return False

    return True

def valid_grid(board, num, pos):

    #SUB GRID
    box_x = pos[1]//3
    box_y = pos[0]//3


    for a in range(box_y*3, box_y*3 + 3):
        for b in range(box_x*3, box_x*3 + 3):
            if board[a][b] == num and (a, b) != pos:
                return False

    return True

count = 0
def solve(board):

    global count
    empty = box_empty(board)

    if not empty:
        return True
    else:

        row, column = empty

    for x in range(1, 10):
        if valid_row(board, x, (row, column)) and valid_column(board, x, (row, column)) and valid_grid(board, x, (row, column)):
            board[row][column] = x
            count = count + 1
            if solve(board):

                return True


            board[row][column] = 0

    return False


printboard(boards)
print("\n\n")
solve(boards)
print("\n\n")
printboard(boards)
print("\n", count)