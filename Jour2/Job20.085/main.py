class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for x in range(j)] for y in range(i)]

    def play(self, column, color):
        if column < 0 or column >= self.j:
            print("Colonne invalide!")
            return False
        row = self.i - 1
        while row >= 0:
            if self.board[row][column] == 'O':
                self.board[row][column] = color
                return True
            row -= 1
        print("Cette colonne est pleine!")
        return False

    def print(self):
        for i in range(self.i):
            print("| ", end="")
            for j in range(self.j):
                print(self.board[i][j] + " | ", end="")
            print("")
        print("-" * (self.j * 4 + 1))


board = Board(4, 4)
current_player = 'J'
winner = None

while not winner:
    board.print()
    column = int(input(f"Joueur {current_player}, choisi une colonne de (0-{board.j-1}): "))
    if board.play(column, current_player):
        if current_player == 'J':
            current_player = 'R'
        else:
            current_player = 'J'

   
    for i in range(board.i):
        for j in range(board.j):
            if board.board[i][j] == 'O':
                continue
            if j <= board.j - 4 and len(set(board.board[i][j:j+4])) == 1:
                winner = board.board[i][j]
            if i <= board.i - 4:
                if len(set([board.board[i+k][j] for k in range(4)])) == 1:
                    winner = board.board[i][j]
            if j <= board.j - 4 and i <= board.i - 4:
                if len(set([board.board[i+k][j+k] for k in range(4)])) == 1:
                    winner = board.board[i][j]
            if j >= 3 and i <= board.i - 4:
                if len(set([board.board[i+k][j-k] for k in range(4)])) == 1:
                    winner = board.board[i][j]
            if winner:
                board.print()
                print(f"Le joueur {winner} à gagné!")
                break

    
    if not winner:
        full_columns = sum([1 for j in range(board.j) if board.board[0][j] != 'O'])
        if full_columns == board.j:
            board.print()
            print("Matxh Null!")
            break
