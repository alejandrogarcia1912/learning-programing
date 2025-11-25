import random

def reto1_lanzar_dado_par_impar():
    """
    Simula el lanzamiento de un dado y determina si el resultado es par o impar.
    """
    # 1. Generar un número aleatorio entre 1 y 6
    resultado = random.randint(1, 6)
    
    # 2. Mostrar el resultado del lanzamiento
    print(f"El dado ha sido lanzado. Resultado: {resultado}")
    
    # 3. Determinar si el resultado es par o impar
    # El operador % (módulo) se usa para obtener el residuo de la división.
    if resultado % 2 == 0:
        print(f"El número {resultado} es PAR.")
    else:
        print(f"El número {resultado} es IMPAR.")

# Ejecución de la función
if __name__ == "__main__":
    reto1_lanzar_dado_par_impar()