from sympy import Symbol, limit
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                       implicit_multiplication_application)
import matplotlib.pyplot as plt
import numpy as np

def plot_function(funcion, x_values, y_values):
    plt.plot(x_values, y_values, label='Función')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función')
    plt.legend()
    plt.grid(True)
    plt.show()

def calcular_limites():
    x = Symbol('x')

    while True:
        funcion = input("Ingrese la función en términos de 'x': ")
        x_valor = float(input("Ingrese el valor de 'x': "))

        try:
            # Usar el parser de sympy para evaluar la función
            transformations = (standard_transformations + (implicit_multiplication_application,))
            funcion_expr = parse_expr(funcion, transformations=transformations)

            if funcion_expr.is_algebraic_expr():
                tipo_funcion = "algebraica"
            elif funcion_expr.is_rational_function():
                tipo_funcion = "racional"
            else:
                print("La función debe ser algebraica o racional.")
                continue

            limite_izquierda = limit(funcion_expr, x, x_valor, dir='-')
            limite_derecha = limit(funcion_expr, x, x_valor, dir='+')

            print(f"Límite por izquierda en x = {x_valor}: {limite_izquierda}")
            print(f"Límite por derecha en x = {x_valor}: {limite_derecha}")

            # Graficar la función en un rango cercano al valor ingresado por el usuario
            x_values = np.linspace(x_valor - 2, x_valor + 2, 400)
            y_values = [funcion_expr.subs(x, value) for value in x_values]
            plot_function(funcion_expr, x_values, y_values)

        except Exception as e:
            print(f"Error: {e}")

        respuesta = input("¿Desea volver a calcular? (S/N): ")
        if respuesta.lower() != 's':
            break

calcular_limites()
