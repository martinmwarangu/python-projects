class TicTacToe:
    def __init__(self) :
        self.board = [' ' for _ in range(9)]  # initializing a 3*3 board
        self.current_winner = None
    def print_board(self):
        for row in [self.board[i*3: (1+1)*3]for i in range(3)]:
            print('|'+'|' .join(row) +'|')
    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3 , (j+1)*3)] for i in range(3)]
        for row in number_board:
             print('|'+'|' .join(row) +'|')
    def available_moves(self):
        return{}         


