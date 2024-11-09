import time
import pywhatkit as kit

numeros = ['+525554222300']

mensaje = """Hey Hola, Espero que estés muy bien.
Me llamo Daniel Balderrama e hice una aplicación diseñada para que psicólogos y terapeutas puedan llevar mejor control y seguimiento de sus pacientes. 
Te gustara conocer mas detalles? """

for numero in numeros:
    kit.sendwhatmsg_instantly(numero, mensaje) 
    time.sleep(5)

