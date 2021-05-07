
    #   x------------------->
board = [[0,9,6,0,0,0,0,0,8],  # y|
         [0,0,0,3,0,0,0,4,0],  #  |
         [0,0,0,2,4,0,0,0,0],  #  |
         [0,0,1,0,0,0,0,8,9],  #  |
         [0,0,0,8,0,3,7,0,0],  #  |
         [0,0,7,5,9,0,0,0,0],  #  |
         [0,0,2,4,5,1,0,0,0],  #  |
         [1,0,5,0,0,6,9,0,0],  #  |
         [3,7,0,9,8,0,1,6,0]]  #  \/     zeros represent empty spot


def display_board(bo):
    #make horizontal line
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        #make vertical line
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end='')

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')


def find_possible_spot(y,x,n):
    global board
    #check rows
    for i in range(9):
        if board[y][i] == n:
            return False

    #check columns
    for i in range(9):
        if board[i][x] == n:
            return False

    #check squares 3x3
    y0=(y//3) * 3
    x0=(x//3) * 3
    for i in range(3):
        for j in range(3):
            if board[y0+i][x0+j] == n:
                return False
    return True


def solver():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if find_possible_spot(y,x,n):
                        board[y][x] = n
                        solver()
                        board[y][x] = 0
                return
    display_board(board)

solver()
