from flask import Flask, render_template, request, redirect, url_for

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
        ingredientes_escalados = {}
        for ingrediente, cantidad in self.ingredientes.items():
            ingredientes_escalados[ingrediente] = cantidad * porciones
        return ingredientes_escalados

class LibroRecetas:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def buscar_receta(self, nombre):
        for receta in self.recetas:
            if receta.nombre.lower() == nombre.lower():
                return receta
        return None

    def mostrar_recetas(self):
        return self.recetas

libro = LibroRecetas()

app = Flask(__name__)

@app.route('/')
def index():
    recetas = libro.mostrar_recetas()
    return render_template('index.html', recetas=recetas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_receta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ingredientes = {ingrediente: int(cantidad) for ingrediente, cantidad in zip(request.form.getlist('ingrediente[]'), request.form.getlist('cantidad[]'))}
        instrucciones = request.form['instrucciones']
        tiempo_preparacion = int(request.form['tiempo_preparacion'])
        tiempo_coccion = int(request.form['tiempo_coccion'])

        nueva_receta = Receta(nombre, ingredientes, instrucciones, tiempo_preparacion, tiempo_coccion)
        libro.agregar_receta(nueva_receta)
        return redirect(url_for('index'))

    return render_template('agregar.html')

@app.route('/receta/<nombre>')
def ver_receta(nombre):
    receta = libro.buscar_receta(nombre)
    if receta:
        return render_template('receta.html', receta=receta)
    return "Receta no encontrada", 404

@app.route('/receta/<nombre>/escalar', methods=['POST'])
def escalar_ingredientes(nombre):
    receta = libro.buscar_receta(nombre)
    if receta:
        porciones = int(request.form['porciones'])
        ingredientes_escalados = receta.escalar_ingredientes(porciones)
        return render_template('receta.html', receta=receta, ingredientes_escalados=ingredientes_escalados)
    return "Receta no encontrada", 404

# Ejecutamos la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
