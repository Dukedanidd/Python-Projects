# Programa que permite guardar datos de estudiantes, agregar, eliminar y mostrar

def add_student(name, age, course):
    students.append({'name': name, 'age': age, 'course': course})
    print(f"Estudiante {name} agregado correctamente.")

def delete_student(name):
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print(f"Estudiante {name} eliminado correctamente.")
            return
    print(f"Estudiante {name} no encontrado.")
    
def show_students():
    for student in students:
        print(f'Nombre: {student['name']}, Edad: {student['age']}, Curso: {student['course']}')
    if not students:
        print("No hay estudiantes registrados.")
        
students = []

while True:
    print("\nOpciones:")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Mostrar estudiantes")
    print("4. Salir")
    
    option = input("Seleccione una opción: ")
    
    if option == '1':
        name = input("Nombre: ")
        age = input("Edad: ")
        course = input("Curso: ")
        add_student(name, age, course)
    elif option == '2':
        name = input("Nombre del estudiante a eliminar: ")
        delete_student(name)
    elif option == '3':
        show_students()
    elif option == '4':
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")  
