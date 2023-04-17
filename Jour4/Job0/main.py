nombre = input("Entrez un nombre : ")

def factorielle ( nombre ):
    if nombre == 0:
        return 1
    return nombre * factorielle ( nombre - 1 )

print ( factorielle ( int ( nombre )))