import pygame

# Initialisation de PyGame
pygame.init()

# Définition des dimensions de la fenêtre
size = (600, 600)

# Création de la fenêtre
screen = pygame.display.set_mode(size)

# Définition du titre de la fenêtre
pygame.display.set_caption("TicTacToe1337")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Variables du jeu
player = 1  # Le joueur 1 commence
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # La grille est vide au début

# Fonction pour dessiner la grille
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i*200, 0), (i*200, 600), 5)
        pygame.draw.line(screen, BLACK, (0, i*200), (600, i*200), 5)

# Fonction pour dessiner un symbole sur la grille
def draw_symbol(row, col, symbol):
    if symbol == 1:
        pygame.draw.circle(screen, BLACK, (col*200+100, row*200+100), 80, 10)
    elif symbol == 2:
        pygame.draw.line(screen, BLACK, (col*200+50, row*200+150), (col*200+150, row*200+50), 10)
        pygame.draw.line(screen, BLACK, (col*200+50, row*200+50), (col*200+150, row*200+150), 10)
    grid[row][col] = symbol
    pygame.display.flip()

# Fonction pour vérifier si un joueur a gagné
def check_win(symbol):
    for i in range(3):
        if grid[i][0] == symbol and grid[i][1] == symbol and grid[i][2] == symbol:
            return True
        elif grid[0][i] == symbol and grid[1][i] == symbol and grid[2][i] == symbol:
            return True
    if grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol:
        return True
    elif grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == symbol:
        return True
    return False

# Fonction principale du jeu
def main():
    global player

if __name__ == '__main__':
    screen.fill(WHITE)
    # Affichage de la grille
    draw_grid()
    # Rafraîchissement de l'écran
    pygame.display.flip()
    # Boucle principale
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Récupération des coordonnées de la case cliquée
                x, y = event.pos
                row = y // 200
                col = x // 200

                # Vérification que la case est vide
                if grid[row][col] == 0:
                    # Dessin du symbole du joueur
                    draw_symbol(row, col, player)

                    # Vérification si le joueur a gagné
                    if check_win(player):
                        print("Joueur", player, "a gagné")
                        running = False
                    # Vérification si la grille est pleine
                    elif all(all(row) for row in grid):
                        print("Match nul")
                        running = False
                    # Affichage d'un message de victoire
                    font = pygame.font.Font(None, 50)
                    text = font.render(f"Player {player} wins!", True, WHITE)
                    text_rect = text.get_rect(center=(300, 50))
                    screen.blit(text, text_rect)

                # Changement de joueur
                player = 3 - player

    
    pygame.quit()

