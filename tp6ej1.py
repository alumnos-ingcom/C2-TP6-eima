###########################################################
# Matias German Quevedo - @Gerchu-arq
#TP 6, Anagrama2 1.
# UNRN Andina - Introducción a la Ingenieria en Computación
###########################################################

def es_anagrama(cadena1, cadena2):
    cadena1_list = list(cadena1)
    cadena1_list.sort()
    cadena2_list = list(cadena2)
    cadena2_list.sort()

    return (cadena1_list == cadena2_list)


def principal():
    """Toda la interacción con el usuario va acá"""
    
    cadena1 = input("Ingresar cadena 1:")
    cadena2 = input("Ingresar cadena 2:")

    if es_anagrama(cadena1, cadena2): return True
    else: return False

if __name__ == "__main__":
    print(principal())

