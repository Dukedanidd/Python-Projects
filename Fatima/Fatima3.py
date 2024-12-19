# CONDICIOINALES

# IF Si esto se cumple pasa esto
# ELIF 
# ELSE

# num1 = 2

#if num1 == 1:
 #   print('Fatima')
#else: 
 #   pregunta = input('como llamas? ')
  #  print(pregunta)
    

# QUIERO UN PROGRAMA QUE ME PREGUNTE UN NUMERO PRIMERO DEL 1 AL 3, Y USANDO CONDICIONALES ME IMPRIMAS , SI ES == 1 DANIEL, SI ES == 2 FATIMA, SI ES == 3 ANA 
# Y SI NO EXISTE EL NUMERO QUE SE IMPRIMA UN MENSAJE DE ERROR

pregunta = int(input('Digita un numero del 1-3 '))
print(pregunta)
if pregunta == 1:
    print('daniel')
elif pregunta == 2:
    print('fatima')
elif pregunta == 3:
    print('ana')
else:
    print('lo siento, ha surgido un error')
