from sympy import Symbol, limit, oo, simplify
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                       implicit_multiplication_application)

def calcular_limites():
    x = Symbol('x')

    while True:
        funcion = input("Ingrese la función en términos de 'x': ")
        x_valor = float(input("Ingrese el valor de 'x': "))

        try:
            # Usar el parser de sympy para evaluar la función
            transformations = (standard_transformations + (implicit_multiplication_application,))
            funcion = parse_expr(funcion, transformations=transformations)

            if funcion.is_algebraic_expr():
                tipo_funcion = "algebraica"
            elif funcion.is_rational_function():
                tipo_funcion = "racional"
            else:
                print("La función debe ser algebraica o racional.")
                continue

            limite_izquierda = limit(funcion, x, x_valor, dir='-')
            limite_derecha = limit(funcion, x, x_valor, dir='+')

            print(f"Tipo de función: {tipo_funcion}")
            print(f"Límite por izquierda en x = {x_valor}: {limite_izquierda}")
            print(f"Límite por derecha en x = {x_valor}: {limite_derecha}")

        except Exception as e:
            print(f"Error: {e}")

        respuesta = input("¿Desea volver a calcular? (S/N): ")
        if respuesta.lower() != 's':
            break

calcular_limites()
