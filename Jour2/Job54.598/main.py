import random

class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for x in range(j)] for y in range(i)]
        self.last_row = -1
        self.last_col = -1

    def play(self, column, color, simulate=False):
        if column < 0 or column >= self.j:
            print("Invalid column!")
            return False
        row = self.i - 1
        while row >= 0:
            if self.board[row][column] == 'O':
                if simulate:
                    return row
                self.board[row][column] = color
                self.last_row = row
                return True
            row -= 1
        print("Column is full!")
        return False

    def print(self):
        for i in range(self.i):
            print("| ", end="")
            for j in range(self.j):
                print(self.board[i][j] + " | ", end="")
            print("")
        print("-" * (self.j * 4 + 1))

    def check_win(self, row, col, color):
        # Check horizontal
        count = 0
        for j in range(max(0, col-3), min(self.j, col+4)):
            if self.board[row][j] == color:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check vertical
        count = 0
        for i in range(max(0, row-3), min(self.i, row+4)):
            if self.board[i][col] == color:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check diagonal (top-left to bottom-right)
        count = 0
        i = max(0, row-col)
        j = max(0, col-row)
        while i < min(self.i, row-col+4) and j < min(self.j, col-row+4):
            if self.board[i][j] == color:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
            i += 1
            j += 1

        # Check diagonal (bottom-left to top-right)
        count = 0
        i = min(self.i-1, row+col-3)
        j = max(0, col-row)
        while i >= max(0, row+col-self.j) and j < min(self.j, col-row+4):
            if self.board[i][j] == color:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
            i -= 1
            j += 1

        return False



class AI_One:
    def __init__(self):
        self.color = None
    
    def think(self, board, color):
        self.color = color
        for col in range(board.j):
            row = board.play(col, self.color)
            if row is not False and board.check_win(row, col, self.color):
                return col
        for col in range(board.j):
            row = board.play(col, Board.get_opponent_color(self.color))
            if row is not False and board.check_win(row, col, Board.get_opponent_color(self.color)):
                return col
        return random.randint(0, board.j - 1)


board = Board(6, 7)
ai = AI_One()

# boucle de jeu
while True:
    # tour du joueur humain
    board.print()
    col = int(input("Joueur humain, dans quelle colonne voulez-vous jouer ? "))
    while not board.play(col, 'J'):
        col = int(input("Cette colonne est invalide ou pleine, veuillez en choisir une autre : "))

    # vérification de la victoire du joueur humain
    if board.check_win(board.last_row, col, 'J'):
        board.print()
        print("Le joueur humain a gagné !")
        break

    # tour de l'IA
    col = ai.think(board, 'R')
    print("L'IA joue dans la colonne", col+1)
    board.play(col, 'R')

    # vérification de la victoire de l'IA
    if board.check_win(board.last_row, col, 'R'):
        board.print()
        print("L'IA a gagné !")
        break