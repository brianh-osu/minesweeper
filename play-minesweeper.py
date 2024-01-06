import random 

def play_Minesweeper():
    def initialize_board():
        board_len = int(input('How large would you like the board? Type an integer (i,e. 1 = 1x1 board, 2 = 2x2 board)'))
        total_tiles  = board_len**2 
        board = [['_' for x in range(board_len)] for x in range(board_len)] 
        print('The board has been initialized as:')
        return [board_len, total_tiles, board]
    
    def print_board():
        for rows in board:
            print(rows)

    def place_mines():
        num_mines = random.randint(1, 3) # number of mines 
        print(f"There are a total of {total_tiles} tiles and {num_mines} mine(s).")
        mine_positions = random.sample(range(1, total_tiles+1), num_mines) #array of mine positions
        print(f"SECRET mine positions {mine_positions}")
        for row in range(len(board)):
            for col in range(len(board[row])): 
                position_number = row * board_len + col + 1 
                if position_number in mine_positions:
                    board[row][col] = 'X'
        print('Mines have been set.')
        print_board()
        
    def uncover_mines():
        choice = input("Which tile would you like to uncover?")
        # how do you differentiate the first uncover_mines (before recursion begins) versus the other? Maybe pass in optional parameter?
        # Within that 'first uncover' should I modulate a check_lose method too because for the recursive versions we should not lose. Rather we should go until it is a mine.
        
    # set global variables 
    board = initialize_board()
    board_len, total_tiles, board = board[0], board[1], board[2]
    print_board()
    place_mines()
    uncover_mines()


if __name__ == '__main__':
    play_Minesweeper()
