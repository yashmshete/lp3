def is_safe(board, row, col, n): 
    for i in range(row): 
        if board[i][col] == 1 or (col - (row - i) >= 0 and board[i][col - (row - i)] == 1) or (col + (row - i) < n and board[i][col + (row - i)] == 1): 
            return False 
    return True 

def solve_nqueens(board, row, n): 
    if row == n: 
        return True 
    for col in range(n): 
        if is_safe(board, row, col, n): 
            board[row][col] = 1 
            if solve_nqueens(board, row + 1, n): 
                return True 
            board[row][col] = 0 
    return False 

def n_queens_first_placed(n, first_row, first_col): 
    board = [[0 for _ in range(n)] for _ in range(n)] 
    board[first_row][first_col] = 1 
    if not solve_nqueens(board, first_row + 1, n): 
        print("No solution found.") 
    else: 
        for row in board: 
            print(row) 

n = int(input("Enter the value of n: ")) 
first_row = int(input("Enter the first queen's row position: ")) 
first_col = int(input("Enter the first queen's column position: ")) 
n_queens_first_placed(n, first_row, first_col) 
