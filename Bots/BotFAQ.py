import discord
from discord.ext import commands
import os
from dotenv import load_dotenv  # Agregar esta importación al inicio

load_dotenv('.env.local')  # Especificar el nombre del archivo

intents = discord.Intents.default() # Permite que el bot lea los mensajes
intents.message_content = True  # Agregar este permiso
bot = commands.Bot(command_prefix = '!' , intents=intents) # Prefijo para los comandos

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Base de datos para las preguntas frecuentes(FAQ)   
faq_db = {
    "qué es python?": "Python es un lenguaje de programación de alto nivel, conocido por su simplicidad y legibilidad.",
    "cómo instalo python?": "Puedes instalar Python desde su página oficial: https://www.python.org/downloads/",
    "qué es una lista en python?": "Una lista es una colección de elementos que se pueden modificar, como ['manzana', 'banana', 'cereza'].",
    "cómo creo una función en python?": "Para crear una función en Python, usa la palabra clave `def`, seguida del nombre de la función:\n```python\ndef saludar():\n    print('¡Hola mundo!')\n```",
    "cómo abro un archivo en python?": "Puedes usar la función `open` para abrir un archivo:\n```python\nwith open('archivo.txt', 'r') as archivo:\n    contenido = archivo.read()\n```",
    "qué es un diccionario en python?": "Un diccionario es una colección de pares clave-valor, como {'clave1': 'valor1', 'clave2': 'valor2'}.",
    "cómo creo una clase en python?": "Para crear una clase, usa la palabra clave `class`:\n```python\nclass Persona:\n    def __init__(self, nombre, edad):\n        self.nombre = nombre\n        self.edad = edad\n```",
    "qué es un bucle for en python?": "Un bucle `for` permite iterar sobre una secuencia de elementos:\n```python\nfor i in range(5):\n    print(i)\n```",
    "cómo uso try-except en python?": "Usa `try-except` para manejar errores:\n```python\ntry:\n    resultado = 10 / 0\nexcept ZeroDivisionError:\n    print('No se puede dividir entre cero')\n```",
    "cómo instalo paquetes con pip?": "Usa el comando `pip install nombre_paquete` en tu terminal para instalar paquetes.",
    "cómo manejo archivos json en python?": "Usa el módulo `json` para trabajar con archivos JSON:\n```python\nimport json\n\n# Crear JSON\ncon_datos = {'nombre': 'Juan', 'edad': 25}\nwith open('datos.json', 'w') as archivo:\n    json.dump(con_datos, archivo)\n\n# Leer JSON\nwith open('datos.json', 'r') as archivo:\n    datos = json.load(archivo)\n```",
    "cómo genero números aleatorios?": "Usa el módulo `random`:\n```python\nimport random\nnumero = random.randint(1, 10)\nprint(numero)\n```",
    "qué es una tupla en python?": "Una tupla es una colección inmutable de elementos, como (1, 2, 3).",
    "cómo hago que mi script se ejecute como un programa principal?": "Usa este patrón:\n```python\nif __name__ == '__main__':\n    print('Ejecutado como programa principal')\n```",
    "qué son las listas por comprensión?": "Son una forma concisa de crear listas:\n```python\ncuadrados = [x**2 for x in range(10)]\n```",
    "cómo uso argumentos en funciones?": "Puedes pasar argumentos posicionales o nombrados:\n```python\ndef saludar(nombre, edad):\n    print(f'Hola {nombre}, tienes {edad} años')\nsaludar('Juan', 25)\n```",
    "cómo mido el tiempo de ejecución de un código?": "Usa el módulo `time`:\n```python\nimport time\ninicio = time.time()\n# Código a medir\ntiempo_total = time.time() - inicio\nprint(f'Tiempo de ejecución: {tiempo_total:.2f} segundos')\n```",
    "cómo creo un decorador en python?": "Un decorador es una función que modifica otra función:\n```python\ndef decorador(func):\n    def funcion_modificada():\n        print('Ejecutando antes de la función')\n        func()\n        print('Ejecutando después de la función')\n    return funcion_modificada\n\n@decorador\ndef mi_funcion():\n    print('Función original')\n\nmi_funcion()\n```",
    "cómo trabajo con hilos (threads) en python?": "Usa el módulo `threading`:\n```python\nimport threading\n\ndef imprimir():\n    print('Hola desde un hilo')\n\nhilo = threading.Thread(target=imprimir)\nhilo.start()\nhilo.join()\n```",
    "que es python?": "Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Es conocido por su sintaxis simple y legible, lo que lo hace ideal para principiantes.",
    "que es una variable?": "Una variable es un espacio en la memoria del ordenador donde puedes almacenar datos. Es como una caja donde guardas información que puede cambiar durante la ejecución del programa. Por ejemplo: nombre = 'Juan'",
    "que son los tipos de datos?": "Los tipos de datos básicos en Python son:\n- Strings (texto): 'Hola'\n- Integers (números enteros): 42\n- Float (números decimales): 3.14\n- Boolean (verdadero/falso): True/False\n- Lists (listas): [1, 2, 3]\n- Dictionaries (diccionarios): {'clave': 'valor'}",
    "que es un bucle?": "Un bucle es una estructura que permite repetir un bloque de código varias veces. Los más comunes son:\n- for: para iterar sobre una secuencia\n- while: para repetir mientras una condición sea verdadera",
    "que es una funcion?": "Una función es un bloque de código reutilizable que realiza una tarea específica. Se define usando 'def' y puede recibir parámetros y retornar valores. Por ejemplo:\ndef saludar(nombre):\n    return f'Hola {nombre}'",
    "que es una lista?": "Una lista es una colección ordenada de elementos que puede contener diferentes tipos de datos. Se define usando corchetes []. Ejemplo: numeros = [1, 2, 3, 4, 5]",
    "que es un diccionario?": "Un diccionario es una estructura de datos que almacena pares de clave-valor. Se define usando llaves {}. Ejemplo: persona = {'nombre': 'Ana', 'edad': 25}",
    "que son los condicionales?": "Los condicionales (if, elif, else) son estructuras que permiten ejecutar diferentes bloques de código según se cumplan ciertas condiciones. Ejemplo:\nif edad >= 18:\n    print('Eres mayor de edad')\nelse:\n    print('Eres menor de edad')",
    "como se hace un comentario?": "En Python hay dos formas de hacer comentarios:\n- Comentario de una línea: usando #\n- Comentario multilinea: usando ''' o \"\"\"",
    "que son los operadores?": "Los operadores son símbolos que realizan operaciones entre valores:\n- Aritméticos: +, -, *, /, %\n- Comparación: ==, !=, >, <, >=, <=\n- Lógicos: and, or, not",
    "como se lee input del usuario?": "Para leer entrada del usuario se usa la función input(). Ejemplo:\nnombre = input('Escribe tu nombre: ')",
    "que es una clase?": "Una clase es una plantilla para crear objetos. Define atributos (datos) y métodos (funciones) que tendrán los objetos. Ejemplo:\nclass Persona:\n    def __init__(self, nombre):\n        self.nombre = nombre",
    "que son los metodos de string?": "Los métodos de string son funciones que pueden aplicarse a textos. Algunos comunes son:\n- upper(): convierte a mayúsculas\n- lower(): convierte a minúsculas\n- strip(): elimina espacios en blanco\n- split(): divide el string en una lista",
    "como se importan modulos?": "Los módulos se importan usando 'import'. Hay varias formas:\n- import modulo\n- from modulo import funcion\n- from modulo import *\nEjemplo: import random",
}

def quitar_acentos(texto):
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
    }
    for a, b in reemplazos.items():
        texto = texto.replace(a, b)
    return texto

@bot.command()
async def preguntar(ctx, *, pregunta):
    # Normalizar la pregunta: convertir a minúsculas y quitar acentos
    pregunta_normalizada = quitar_acentos(pregunta.lower())
    
    # Buscar en el diccionario normalizando cada clave
    respuesta = None
    for key, value in faq_db.items():
        if quitar_acentos(key.lower()) == pregunta_normalizada:
            respuesta = value
            break
    
    if respuesta:
        await ctx.send(respuesta)
    else:
        await ctx.send(f'No tengo esa respuesta, intenta revisar en la documentacion o en el chat de la comunidad')

# Agregar funcionalidad para buscar en la documentacion
@bot.command()
async def buscar(ctx, *, consulta):
    base_url = 'https://docs.python.org/3/search.html?q='
    enlace = base_url + consulta.replace(' ' , '+')
    await ctx.send(f'Puedes encontrar mas informacion aqui: {enlace}')

# Ejecutar el bot
bot.run(os.getenv('TOKEN_DISCORD'))  # Cambiado de 'TOKEN DISCORD'
