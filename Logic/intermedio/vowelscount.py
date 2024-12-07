# Escribir un programa que cuente las vocales de una palabra

def count_vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in word if char in vowels)
while True:
    print(count_vowels(input("Ingresa la palabra: "))) 

