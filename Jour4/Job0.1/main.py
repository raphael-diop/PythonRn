x = input("Votre nombre: ")
n = input("Votre puissance: ")

def puissance(x, n):
    if n == 0:
        return 1
    return x * puissance(x, n - 1)
print(puissance(int(x), int(n)))