import math
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ''
def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return 1 if board[row][0] == PLAYER_X else -1
    for col in  range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return 1 if board[0][col] == PLAYER_X else -1
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 1 if board[0][0] == PLAYER_X else -1
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 1 if board[0][2] == PLAYER_X else -1
    return 0

def minimax(board, is_maximizing):
    score = evaluate(board)
    if score !=0:
        return score
    if all(cell != EMPTY for row in board for cell in row):
        return 0
    best_score = -math.inf if is_maximizing else math.inf
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X if is_maximizing else PLAYER_O
                current_score = minimax(board, not is_maximizing)
                board[row][col] = EMPTY
                best_score = max(best_score, current_score) if is_maximizing else min(best_score, current_score)
    return best_score

def find_best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                score = minimax(board, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (row,col)
    return move

if __name__ == "__main__":
    board = [
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
    ]
best_move = find_best_move(board)
print(f"Best move for X is at position: {best_move}")
