########################################################
# Matías G. Quevedo - @Gerchu-arq

# TP 6, Etiquetas HTML.
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def hace_etiqueta(contenido, etiqueta):
   
    salida = ''
    salida = "<"+ etiqueta +">" + contenido + "</"+ etiqueta +">" 
    return salida
        
def hace_comenta(contenido_):
    
    salida = ''
    salida = "<!--"+ contenido_ +"-->" 
    return salida

def principal(entrada1, entrada2):
    
    print("<html>\n<body>")
    encabezado = entrada1
    parrafo = entrada2
    print(encabezado)
    print(parrafo)
    print("<\html>\n<\\body>")
    
def prueba():
    
        entrada1 = hace_etiqueta('Hola HTML', 'h1')
        entrada2 = hace_comenta('Esto es un parrafo')
        principal(entrada1, entrada2)

############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()  
    
