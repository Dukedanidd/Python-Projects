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
    # Python básico
    "qué es python?": "Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Es conocido por su sintaxis simple y legible, lo que lo hace ideal para principiantes.",
    "que es python?": "[MISMA RESPUESTA QUE ARRIBA]",
    "python que es?": "[MISMA RESPUESTA QUE ARRIBA]",
    "puedes explicarme que es python?": "[MISMA RESPUESTA QUE ARRIBA]",
    "me explicas python?": "[MISMA RESPUESTA QUE ARRIBA]",
    "definicion de python": "[MISMA RESPUESTA QUE ARRIBA]",
    "dime sobre python": "[MISMA RESPUESTA QUE ARRIBA]",

    # Instalación
    "cómo instalo python?": "Puedes instalar Python desde su página oficial: https://www.python.org/downloads/",
    "como instalar python?": "[MISMA RESPUESTA QUE ARRIBA]",
    "instalar python": "[MISMA RESPUESTA QUE ARRIBA]",
    "como puedo instalar python?": "[MISMA RESPUESTA QUE ARRIBA]",
    "donde instalo python?": "[MISMA RESPUESTA QUE ARRIBA]",
    "pasos para instalar python": "[MISMA RESPUESTA QUE ARRIBA]",
    "guia instalacion python": "[MISMA RESPUESTA QUE ARRIBA]",

    # Variables
    "que es una variable?": "Una variable es un espacio en la memoria del ordenador donde puedes almacenar datos. Es como una caja donde guardas información que puede cambiar durante la ejecución del programa. Por ejemplo: nombre = 'Juan'",
    "que son las variables?": "[MISMA RESPUESTA QUE ARRIBA]",
    "variables en python": "[MISMA RESPUESTA QUE ARRIBA]",
    "como usar variables?": "[MISMA RESPUESTA QUE ARRIBA]",
    "explicame las variables": "[MISMA RESPUESTA QUE ARRIBA]",
    "para que sirven las variables?": "[MISMA RESPUESTA QUE ARRIBA]",
    "definicion de variable": "[MISMA RESPUESTA QUE ARRIBA]",

    # Listas
    "qué es una lista en python?": "Una lista es una colección de elementos que se pueden modificar, como ['manzana', 'banana', 'cereza'].",
    "que son las listas?": "[MISMA RESPUESTA QUE ARRIBA]",
    "listas en python": "[MISMA RESPUESTA QUE ARRIBA]",
    "como uso las listas?": "[MISMA RESPUESTA QUE ARRIBA]",
    "explicame las listas": "[MISMA RESPUESTA QUE ARRIBA]",
    "para que sirven las listas?": "[MISMA RESPUESTA QUE ARRIBA]",
    "definicion de lista": "[MISMA RESPUESTA QUE ARRIBA]",
    "como crear una lista": "[MISMA RESPUESTA QUE ARRIBA]",

    # Funciones
    "cómo creo una función en python?": "Para crear una función en Python, usa la palabra clave `def`, seguida del nombre de la función:\n```python\ndef saludar():\n    print('¡Hola mundo!')\n```",
    "como hacer una funcion?": "[MISMA RESPUESTA QUE ARRIBA]",
    "funciones en python": "[MISMA RESPUESTA QUE ARRIBA]",
    "crear funciones": "[MISMA RESPUESTA QUE ARRIBA]",
    "como defino una funcion?": "[MISMA RESPUESTA QUE ARRIBA]",
    "sintaxis de funciones": "[MISMA RESPUESTA QUE ARRIBA]",
    "ejemplo de funcion": "[MISMA RESPUESTA QUE ARRIBA]",

    # ... continuar con el mismo patrón para todas las preguntas existentes ...
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
