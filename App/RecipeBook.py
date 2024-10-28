# Sirve para desarrollar aplicaciones web con Python
from flask import Flask, render_template, request, redirect, url_for
# pymongo permite interactuar a Python con MongoDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

# Aquí está FINALMENTE lo que  tanto desee desde hace 5 hrs, la conexion a MONGO Y FUNCIONA LA MAL PORTADA
uri = "mongodb+srv://dukedanidd:eTO8eUlD6QOeg3Ku@cluster0.f390h.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

# Verificamos si conecto la perra
try:
    client.admin.command('ping')
    print("Conexion exitosa mi pa")
except Exception as e:
    print(f"Error, nombre no le sabes al pedo: {e}")

# Accedemos a la base de datos POR FIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIN
db = client["recetas"]
recetas_collection = db["recetas"]

class Receta:
    def __init__(self, nombre, ingredientes, instrucciones, tiempo_preparacion, tiempo_coccion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones
        self.tiempo_preparacion = tiempo_preparacion
        self.tiempo_coccion = tiempo_coccion
        
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'ingredientes': self.ingredientes,
            'instrucciones': self.instrucciones,
            'tiempo_preparacion': self.tiempo_preparacion,
            'tiempo_coccion': self.tiempo_coccion
        }

# Aquí es donde inicia el CRUD
# R de RAJAS
@app.route('/')
def index():
    recetas = list(recetas_collection.find())  
    return render_template('index.html', recetas=recetas)


# C de CULEAR
@app.route('/agregar', methods=['GET', 'POST'])
def agregar_receta():
    ingredientes = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        ingredientes = {ingrediente: int(cantidad) for ingrediente, cantidad in zip(request.form.getlist('ingredientes[]'), request.form.getlist('cantidad[]'))}
        instrucciones = request.form['instrucciones']
        tiempo_preparacion = int(request.form['tiempo_preparacion'])
        tiempo_coccion = int(request.form['tiempo_coccion'])
        
        nueva_receta = Receta(nombre, ingredientes, instrucciones, tiempo_preparacion, tiempo_coccion)
        recetas_collection.insert_one(nueva_receta.to_dict())
        return redirect(url_for('index'))
    
    return render_template('agregar.html', ingredientes=ingredientes)



@app.route('/receta/<nombre>')
def ver_receta(nombre):
    receta = recetas_collection.find_one({'nombre': nombre})
    if receta:
        return render_template('receta.html', receta=receta)
    return 'Receta no encontrada', 404

# U de ESTERNOCLEIDOMASTOIDEO
@app.route('/receta/<nombre>/editar', methods=['GET', 'POST'])  
def editar_receta(nombre):
    receta = recetas_collection.find_one({"nombre": nombre})  
    if request.method == 'POST':
        ingredientes = {ingrediente: int(cantidad) for ingrediente, cantidad in zip(request.form.getlist('ingrediente[]'), request.form.getlist('cantidad[]'))}
        instrucciones = request.form['instrucciones']
        tiempo_preparacion = int(request.form['tiempo_preparacion'])
        tiempo_coccion = int(request.form['tiempo_coccion'])

        recetas_collection.update_one(
            {"nombre": nombre},
            {"$set": {
                "ingredientes": ingredientes,
                "instrucciones": instrucciones,
                "tiempo_preparacion": tiempo_preparacion,
                "tiempo_coccion": tiempo_coccion
            }}
        )
        return redirect(url_for('ver_receta', nombre=nombre))

    if receta:
        return render_template('editar.html', receta=receta)
    return "Receta no encontrada", 404

@app.route('/receta/<nombre>/escalar', methods=['POST'])
def escalar_ingredientes(nombre):
    receta = recetas_collection.find_one({'nombre': nombre})
    if receta:
        porciones = int(request.form['porciones'])
        ingredientes_escalados = {k: v * porciones for k, v in receta['ingredientes'].items()}
        return render_template('receta.html', receta=receta, ingredientes_escalados=ingredientes_escalados)
    return 'Receta no encontrada', 404

# D de DUKE ES UNA VERGA
@app.route('/receta/<nombre>/eliminar', methods=['POST'])
def eliminar_receta(nombre):
    recetas_collection.delete_one({"nombre": nombre}) 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
