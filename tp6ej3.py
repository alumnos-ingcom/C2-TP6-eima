

with open("archivo1.txt","w") as f:
    contenido = input("Escribir en archivo 1: ")
    f.write(contenido)
    with open("archivo2.txt", "w") as f1:
        for line in f:
            if contenido in line:
                f1.write(line) 