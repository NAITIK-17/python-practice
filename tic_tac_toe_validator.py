# Your input code (PERFECT!)
row1 = []
row2 = []
row3 = []
for i in range(3):
    row1.append(input(f"Top row cell {i+1}: ").upper())
for i in range(3):    
    row2.append(input(f"Middle row cell {i+1}: ").upper())
for i in range(3):
    row3.append(input(f"Bottom row cell {i+1}: ").upper())

board = [row1, row2, row3]

def is_win(board):
    # Check ROWS (3 lines)
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return f"{row[0]} wins"
    
    # Check COLUMNS (3 lines)
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return f"{board[0][col]} wins"
    
    # Check DIAGONALS (2 lines)
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return f"{board[0][0]} wins"
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return f"{board[0][2]} wins"
    
    return "No winner"

# Show board + result
for row in board:
    print(" ".join(row))
print(is_win(board))
