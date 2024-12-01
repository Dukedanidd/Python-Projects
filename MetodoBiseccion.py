import sympy as sp

def f(x, expr):
    # Evalúa la expresión dada en x.
    return expr.evalf(subs={symbol: x})

def bisection_method(expr, a, b, tolerance):
    # Aplica el método de bisección para encontrar la raíz y cuenta las iteraciones.
    if f(a, expr) * f(b, expr) >= 0:
        print("No se puede aplicar el método de bisección.")
        return None, 0
    
    couter = 0  # Contador de iteraciones
    
    while True:
        xm = (a + b) / 2  
        couter += 1
        
        if abs(f(xm, expr)) < tolerance:
            return xm, couter
        
        if f(xm, expr) * f(a, expr) < 0:
            b = xm
        else:
            a = xm
            
        # Condición de escape: si el intervalo se hace muy pequeño
        if abs(b - a) < tolerance:
            break
    
    return (a + b) / 2, couter

# Definimos la variable simbólica
symbol = sp.symbols('x')

# Solicitar la entrada del usuario
print("Ingresa la ecuación en términos de x (por ejemplo, x**2 - 4):")
equation = input("Ecuación: ")
expr = sp.sympify(equation)

a = float(input("Ingresa el límite inferior (a): "))
b = float(input("Ingresa el límite superior (b): "))
tolerance = float(input("Ingresa la tolerance "))

# Ejecutamos el método de bisección
raiz, iteraciones = bisection_method(expr, a, b, tolerance)

if raiz is not None:
    print(f"La raíz encontrada es: {raiz}")
    print(f"f(raíz) = {f(raiz, expr)}")
    print(f"Número de iteraciones realizadas: {iteraciones}")
