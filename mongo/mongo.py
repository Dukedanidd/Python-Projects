
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dukedanidd:eTO8eUlD6QOeg3Ku@cluster0.f390h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["recetas"]
    collection = db["recetas"]
    
    #C
    name = input('Ingresa tu nombre: ')
    edad = input('Ingresa tu edad: ')
    city = input('Ingresa tu ciudad: ')
    
    dcumentoUser = {
        "name" : name,
        "edad" : edad,
        "city" : city
    }
    response = collection.insert_one(dcumentoUser)
    print(f'Documento insertado con el id: {response.inserted_id}')
    
    #R
    for doc in collection.find():
        print (doc)
        
    #U
    collection.update_one({'name':'Daniel'},{'$set' : {'city':'Parral'}})
    docActual = collection.find_one({'name':'Daniel'})
    print(docActual)
    
    #D
    collection.delete_one({'name' : 'Daniel'})
    
    
    
except Exception as e:
    print(e)