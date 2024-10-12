from flask import Flask, render_template, request, redirect, url_for, flash


class Receta:
    def __init__(self, nombre, ingredientes, instrucciones, tiempo_preparacion, tiempo_coccion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones
        self.tiempo_preparacion = tiempo_preparacion
        self.tiempo_coccion = tiempo_coccion

    def tiempo_total(self):
        return self.tiempo_preparacion + self.tiempo_coccion

    def escalar_ingredientes(self, porciones):
        return {ingrediente: cantidad * porciones for ingrediente, cantidad in self.ingredientes.items()}

class LibroRecetas:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def buscar_receta(self, nombre):
        return next((receta for receta in self.recetas if receta.nombre.lower() == nombre.lower()), None)

    def mostrar_recetas(self):
        return self.recetas

libro = LibroRecetas()

@app.route('/')
def index():
    return render_template('index.html', recetas=libro.mostrar_recetas())

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_receta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ingredientes = eval(request.form['ingredientes']) 
        instrucciones = request.form['instrucciones']
        tiempo_preparacion = int(request.form['tiempo_preparacion'])
        tiempo_coccion = int(request.form['tiempo_coccion'])
        
        nueva_receta = Receta(nombre, ingredientes, instrucciones, tiempo_preparacion, tiempo_coccion)
        libro.agregar_receta(nueva_receta)
        
        flash('Receta agregada exitosamente!')
        return redirect(url_for('index'))
    
    return render_template('agregar_receta.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_receta():
    receta_encontrada = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        receta_encontrada = libro.buscar_receta(nombre)
    
    return render_template('buscar_receta.html', receta=receta_encontrada)

app.run(debug=True)
