from letras import letras

def frase_fila(alto,palabras):
    frase = []
    for i in range(alto):
        frase.append([])
    
    for palabra in palabras:
        for indice, caracter in enumerate(palabra):
            car = letras[caracter]
            for i in range(len(car)):
                frase[i+3].extend(car[i])
                frase[i+3].append(0)
                if indice == len(palabra) - 1:
                    frase[i+3].append(0)
    
    for r in range(3):
        frase[r] = [0] * len(frase[7])
    
    array_unidimensional = [pixel for fila in frase for pixel in fila]


    return array_unidimensional


def frase_col_espejada(palabras):
    frase = []
    
    for palabra in palabras:
        for indice, caracter in enumerate(palabra):
            car = letras[caracter]
            for i in range(4):
                for j in range(8):
                    pass
                    if j < 3:
                        frase.append(0)
                    else:
                        frase.append(car[j-3][i])
            frase.extend([0, 0, 0, 0, 0, 0, 0, 0])
            if indice == len(palabra) - 1:
                frase.extend([0, 0, 0, 0, 0, 0, 0, 0])

    return frase

palabra = ['HOLA','COMO','ESTAS']

def frase(palabras):
    frase = []
    
    for palabra in palabras:
        for indice, caracter in enumerate(palabra):
            car = letras[caracter]
            for i in range(4):
                # Itera sobre las columnas en orden inverso para corregir el efecto espejo
                for j in reversed(range(8)):
                    if j < 3:
                        frase.append(0)
                    else:
                        frase.append(car[j-3][i])
            frase.extend([0, 0, 0, 0, 0, 0, 0, 0])
            if indice == len(palabra) - 1:
                frase.extend([0, 0, 0, 0, 0, 0, 0, 0])

    return frase

prueba = frase(palabra)

print(prueba)

print(len(prueba))