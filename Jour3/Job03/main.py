import string
import matplotlib.pyplot as plt

# Initialiser un dictionnaire pour stocker le nombre d'occurrences de chaque lettre
counts = {}
for char in string.printable:
    if char.isalpha():
        counts[char] = 0

# Ouvrir le fichier texte et compter les occurrences de chaque lettre
with open("Jour3/data.txt", "r") as fichié:
    for line in fichié:
        for letter in line.lower():
            if letter.isalpha() and letter in counts:
                counts[letter] += 1

# Calculer le total des occurrences de toutes les lettres
total_count = sum(counts.values())

# Calculer le pourcentage d'apparition de chaque lettre et les stocker dans deux listes
letters = []
percentages = []
for letter, count in counts.items():
    letters.append(letter)
    percentages.append(count / total_count * 100)

# Générer l'histogramme
plt.bar(letters, percentages)
plt.xlabel("Lettres")
plt.ylabel("% d'apparition")
plt.title("Pourcentage d'apparition de chaque lettre")
plt.show()
