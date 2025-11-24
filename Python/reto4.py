# Reto condicional 3.
# Implementa una calculadora que solicita dos números y realiza una operación
# elegida mediante un menú.

def realizar_operacion(num1, num2, opcion):
    """Realiza la operación matemática basada en la opción seleccionada."""
    
    # Se utiliza una estructura if/elif/else para manejar las opciones del menú
    if opcion == '1': # Sumar
        print(f"Resultado de la Suma: {num1 + num2}")
        
    elif opcion == '2': # Restar
        print(f"Resultado de la Resta: {num1 - num2}")
        
    elif opcion == '3': # Multiplicar
        print(f"Resultado de la Multiplicación: {num1 * num2}")
        
    elif opcion == '4': # Dividir
        # Validación: Evitar división por cero
        if num2 != 0:
            print(f"Resultado de la División: {num1 / num2}")
        else:
            print("Error: No se puede dividir por cero.")
            
    elif opcion == '5': # Todas las operaciones
        print("\n--- Resultados de Todas las Operaciones ---")
        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"Multiplicación: {num1 * num2}")
        if num2 != 0:
            print(f"División: {num1 / num2}")
        else:
            print("División: Error (división por cero)")
            
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")


def reto_calculadora_menu():
    """Función principal para el reto de la calculadora."""
    print("--- Reto Condicional 3: Calculadora con Menú ---")
    
    try:
        # 1. Solicitar números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        # 2. Mostrar Menú
        print("\n--- MENÚ DE OPERACIONES ---")
        print("[1]. Sumar")
        print("[2]. Restar")
        print("[3]. Multiplicar")
        print("[4]. Dividir")
        print("[5]. Todas")
        print("---------------------------")
        
        # 3. Solicitar y procesar la opción
        opcion = input("Ingrese la opción deseada [1-5]: ")
        realizar_operacion(num1, num2, opcion)
        
    except ValueError:
        print("Error: Asegúrese de ingresar números válidos.")

if __name__ == "__main__":
    reto_calculadora_menu()