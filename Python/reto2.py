# Reto condicional 2.
# Crea un algoritmo que solicite un número entero por consola (positivo o negativo),
# y valide si ese número es PAR o IMPAR.

def reto_condicional_2():
    """Implementa la lógica para determinar si un número es par o impar."""
    print("--- Reto Condicional 1: Par o Impar ---")
    
    try:
        # Solicitar y convertir la entrada del usuario a un número entero
        entrada = input("Por favor, ingrese un número entero (positivo o negativo): ")
        numero = int(entrada)
        
        # El operador módulo (%) devuelve el resto de una división.
        # Si numero % 2 es igual a 0, el número es par.
        if numero % 2 == 0:
            print(f"El número {numero} es PAR.")
        else:
            print(f"El número {numero} es IMPAR.")
            
    except ValueError:
        # Manejo de error si el usuario no ingresa un número entero válido
        print("Error: La entrada no es un número entero válido. Por favor, intente de nuevo.")

if __name__ == "__main__":
    reto_condicional_2()