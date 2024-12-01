def es_palindromo(texto):
    # Convertir a minúsculas y eliminar espacios
    texto = texto.lower().replace(" ", "")
    # Comparar el texto con su versión invertida
    return texto == texto[::-1]

while True:
    palabra = input("Ingresa una palabra o frase (o 'salir' para terminar): ")
    
    if palabra.lower() == 'salir':
        break
        
    if es_palindromo(palabra):
        print(f'"{palabra}" es un palíndromo')
    else:
        print(f'"{palabra}" no es un palíndromo')
