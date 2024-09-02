import random

# Function to print the game board
def print_board(board):
    global board_dim, user_board
    st = '  '
    for i in range(board_dim):
        st = st + '     ' + str(i+1)  # Column numbers
    print(st)

    for r in range(board_dim):
        if r == 0:
            # Print the top border of the board
            st = "    "
            for f in range(board_dim):
                st = st + '______'
            print(st)

        # Print the empty cells of the board
        st = '    '
        for col in range(board_dim):
            st = st + "|     "
        print(st + '|')

        # Print row number and cell values
        if r < 9:
            st = "  " + str(r+1) + " |"
        else:
            st = " " + str(r+1) + " |"
            
        for col in range(board_dim):
            st = st + '  ' + str(board[r][col]) + "  |"
        print(st)

        # Print the bottom border of the cells
        st = '    '
        for col in range(board_dim):
            st = st + "|_____"
        print(st + '|')

# Function to place bombs randomly on the board
def plant_the_bombs(bombs):
    bombs_planted = 0
    while bombs_planted < bombs:
        rand_loc = random.randint(0, board_dim ** 2 - 1)
        row = rand_loc // board_dim
        col = rand_loc % board_dim

        if board[row][col] == '*':  # Check if the cell already has a bomb
            continue
        else:
            board[row][col] = '*'  # Plant a bomb
            bombs_planted += 1

# Function to set values in the board representing the number of adjacent bombs
def set_values():
    for r in range(board_dim):
        for c in range(board_dim):
            if board[r][c] == "*":  # Skip bombs
                continue
            else:
                board[r][c] = str(get_neighbours_value(r, c))

# Function to count the number of bombs surrounding a cell
def get_neighbours_value(row, col):
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    neighbour_bombs = 0
    for r1, c1 in offsets:
        nr, nc = row + r1, col + c1

        if 0 <= nr < board_dim and 0 <= nc < board_dim and board[nr][nc] == "*":
            neighbour_bombs += 1  # Increment count if a bomb is found
    return neighbour_bombs

# Function to dig at a given location on the board
def dig(row, col):
    if [row, col] in dugged:
        print('position already dugged')
        return False
    else:
        dugged.append([row, col])  # Mark this location as dug

    if board[row][col] == "*":  # Hit a bomb
        print('OOps! Badluck')
        return False
    elif board[row][col] == '0':  # If no adjacent bombs, dig neighbors
        for r in range(max(0, row-1), min(board_dim-1, row+1) + 1):
            for c in range(max(0, col-1), min(board_dim-1, col+1) + 1):
                if [r, c] not in dugged:
                    dig(r, c)
    user_board[row][col] = board[row][col]
    return True

# Function to flag or unflag a cell
def flag(row, col):
    if [row, col] in flagged:
        flagged.remove([row, col])
        user_board[row][col] = " "
    else:
        flagged.append([row, col])
        user_board[row][col] = "F"

# Function to take user input for digging or flagging
def user_value():
    user_input = input('Enter the coordinates here to dig the board Ex,1,1f or 1,1:')
    return user_input

# Function to check if the user has won
def winner():
    if len(dugged) == board_dim**2 - bombs:
        print('Congratulations! You have cleared the minefield!')
        print_board(board)

# Function to ask if the user wants to replay the game
def replay():
    replay_game = input('Do you want to play Minesweeper again? Enter -y- to play again and -n- to exit: ')
    if replay_game == 'y':
        print('Here we go again!')
        game()
        return True
    else:
        return False

# Function to initialize or reset the game board
def setup():
    global board, user_board, dugged, flagged
    board = [[" " for _ in range(board_dim)] for _ in range(board_dim)]
    user_board = [[" " for _ in range(board_dim)] for _ in range(board_dim)]
    dugged = []
    flagged = []

# Main game function
def game():
    setup()  # Initialize the game setup
    game_on = True

    while game_on:
        print_board(user_board)
        plant_the_bombs(bombs)
        set_values()

        user_input = user_value()
        try:
            if 'f' not in user_input:  # Handle dig command
                row, col = map(int, user_input.split(','))
            else:  # Handle flag command
                row, col = map(int, user_input.split('f')[0].split(','))

            if 1 <= row <= board_dim and 1 <= col <= board_dim:
                if 'f' not in user_input:
                    safe = dig(row-1, col-1)
                    if not safe:
                        print('You hit a bomb, Game Over!')
                        print_board(board)
                        game_on = False
                else:
                    flag(row-1, col-1)
            else:
                print('Invalid Coordinates passed, Try again"_"')
        except(ValueError, IndexError):
            print('Invalid Coordinates, Try again later!')

        winner()
        
    if not replay():
        print('Game Over!')
        quit()

if __name__ == '__main__':
    board_dim = 10  # Size of the board
    bombs = 10  # Number of bombs
    game()  # Start the game
