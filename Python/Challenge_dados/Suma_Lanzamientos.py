import random

def sumar_lanzamientos(veces):
    """
    Realiza 'veces' lanzamientos de un dado y calcula la suma total.
    """
    suma_total = 0
    
    print(f"Iniciando {veces} lanzamientos...")
    print("-" * 30)
    
    # Ciclo para simular N lanzamientos
    for i in range(1, veces + 1):
        # Generar un número aleatorio entre 1 y 6
        resultado_dado = random.randint(1, 6)
        
        # Mostrar el resultado de este tiro
        print(f"Tiro #{i}: {resultado_dado}")
        
        # Acumular el resultado
        suma_total += resultado_dado
        
    # Mostrar el resultado final
    print("-" * 30)
    print(f"Total de lanzamientos: {veces}")
    print(f"La suma total de los valores generados es: {suma_total}")

# Proceso Principal
if __name__ == "__main__":
    print("RETO 2: SUMA TOTAL DE LANZAMIENTOS")
    try:
        # 1. Solicitar el número de veces que se desea lanzar el dado
        num_lanzamientos = int(input("Ingrese el número de veces que desea lanzar el dado: "))
        
        if num_lanzamientos > 0:
            # 2. Ejecutar la función
            sumar_lanzamientos(num_lanzamientos)
        else:
            print("El número de lanzamientos debe ser positivo.")
            
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")