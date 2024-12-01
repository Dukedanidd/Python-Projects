import random
import string

def generar_password(longitud=12, mayusculas=True, minusculas=True, num=True, symbols=True):
    characters = ''
    
    if mayusculas:
        characters += string.ascii_letters.upper()
    if minusculas:
        characters += string.ascii_letters.lower()
    if num:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError('No se puede generar una contraseña')
    
    password = ''.join(random.choices(characters, k=longitud))
    
    # Pedir al usuario una descripción para la contraseña
    descripcion = input("Ingresa una descripción para esta contraseña (ej: Facebook, Gmail, etc.): ")
    
    # Guardar la contraseña con su descripción
    with open('passwords.txt', 'a') as archivo:
        archivo.write(f"App: {descripcion} | Contraseña: {password}\n")
    
    return password

# Ejemplo de uso
nueva_password = generar_password()
print(f"Tu contraseña es: {nueva_password}")

