# Importar los módulos necesarios
from sympy import Symbol, limit  # Importar clases Symbol y limit de Sympy para cálculo simbólico
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)
# Importar herramientas para análisis de expresiones matemáticas
import matplotlib.pyplot as plt  # Importar módulo para graficar
import numpy as np  # Importar módulo para manipulación de arreglos numéricos
import math  # Importar módulo de funciones matemáticas

# Función para graficar la función
def plot_function(funcion, x_values, y_values):
    """
    Grafica la función y la muestra.
    
    funcion (SymPy Expr): La expresión de la función.
    x_values (numpy array): Valores de x para el eje x.
    y_values (numpy array): Valores de f(x) para el eje y.
    """
    plt.plot(x_values, y_values, label='Función')  # Graficar la función
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Agregar línea horizontal en y=0
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Agregar línea vertical en x=0
    plt.xlabel('x')  # Etiqueta del eje x
    plt.ylabel('f(x)')  # Etiqueta del eje y
    plt.title('Gráfico de la función')  # Título de la gráfica
    plt.legend()  # Mostrar leyenda
    plt.grid(True)  # Mostrar cuadrícula
    plt.show()  # Mostrar la gráfica

# Función principal para calcular límites
def calcular_limites():
    x = Symbol('x')  # Crear el símbolo x para usar en las expresiones

    while True:
        # Solicitar la función y el valor de x al usuario
        print("X² = X**2\n________________________________________________")
        funcion = input("Ingrese la función en términos de 'x': ")  # Solicitar la función al usuario
        x_valor = float(input("Ingrese el valor de 'x': "))  # Solicitar el valor de x al usuario

        try:
            # Usar el parser de sympy para evaluar la función
            transformations = (standard_transformations + (implicit_multiplication_application,))
            funcion_expr = parse_expr(funcion, transformations=transformations)

            # Determinar el tipo de función (algebraica o racional)
            if funcion_expr.is_algebraic_expr():  # Verificar si es una función algebraica
                tipo_funcion = "algebraica"
            elif funcion_expr.is_rational_function():  # Verificar si es una función racional
                tipo_funcion = "racional"
            else:
                print("La función debe ser algebraica o racional.")  # Mostrar mensaje de error si no es algebraica ni racional
                continue  # Volver al inicio del bucle

            # Calcular límites por izquierda y derecha
            limite_izquierda = limit(funcion_expr, x, x_valor, dir='-')  # Calcular límite por izquierda
            limite_derecha = limit(funcion_expr, x, x_valor, dir='+')  # Calcular límite por derecha

            print("Es una funcion:", tipo_funcion)
            print(f"Límite por izquierda en x = {x_valor}: {limite_izquierda}")  # Mostrar límite por izquierda
            print(f"Límite por derecha en x = {x_valor}: {limite_derecha}")  # Mostrar límite por derecha

            # Calcular la diferencia entre los límites izquierdo y derecho
            LimiteTotal = limite_izquierda - limite_derecha 

            if math.isnan(LimiteTotal):  # Verificar si el límite es infinito
                print("El límite es infinito.")
            elif -0.1 < LimiteTotal < 0.1:  # Verificar si los límites son cercanos
                print("Ambos laterales son iguales, el límite es:", limite_izquierda)
            else:
                print("El límite no existe en ese punto porque los laterales no son iguales")

            # Graficar la función en un rango cercano al valor ingresado por el usuario
            x_values = np.linspace(x_valor - 2, x_valor + 2, 400)  # Crear valores de x para la gráfica
            y_values = [funcion_expr.subs(x, value) for value in x_values]  # Calcular f(x) para cada valor de x
            plot_function(funcion_expr, x_values, y_values)  # Llamar a la función para graficar

        except Exception as e:
            print(f"Error: {e}")  # Mostrar mensaje de error en caso de excepción

        respuesta = input("¿Desea volver a calcular? (S/N): ")  # Preguntar si el usuario desea repetir el cálculo
        if respuesta.lower() != 's':  # Si la respuesta no es 's'
            break  # Salir del bucle

# Llamar a la función para comenzar el cálculo de límites
calcular_limites()
