# Reto condicional 3.
# Valida si un número es PAR POSITIVO, PAR NEGATIVO, IMPAR POSITIVO o IMPAR NEGATIVO.

def reto_condicional_3():
    """Implementa la lógica para clasificar un número entero en 4 categorías."""
    print("--- Reto Condicional 2: Clasificación Cuádruple ---")
    
    try:
        entrada = input("Por favor, ingrese un número entero (positivo o negativo): ")
        numero = int(entrada)
        
        # Manejo del Cero
        if numero == 0:
            print("El número 0 es PAR, y es un caso especial (ni positivo ni negativo).")
            return # Terminar la función si es 0

        # Paso 1: Determinar el signo (Positivo o Negativo)
        if numero > 0:
            signo = "POSITIVO"
        else: # numero < 0
            signo = "NEGATIVO"

        # Paso 2: Determinar la paridad (Par o Impar)
        # El operador % funciona correctamente con números negativos en Python
        if numero % 2 == 0:
            paridad = "PAR"
        else:
            paridad = "IMPAR"

        # Paso 3: Combinar y mostrar el resultado
        print(f"El número {numero} es {paridad} {signo}.")
            
    except ValueError:
        print("Error: La entrada no es un número entero válido. Por favor, intente de nuevo.")

if __name__ == "__main__":
    reto_condicional_3()