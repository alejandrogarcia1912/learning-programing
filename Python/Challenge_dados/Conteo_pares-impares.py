import random

def contar_pares_impares(veces):
    """
    Realiza 'veces' lanzamientos de un dado y cuenta el total de resultados pares e impares.
    """
    pares_generados = 0
    impares_generados = 0
    
    print(f"Iniciando {veces} lanzamientos...")
    print("-" * 36)
    
    # Ciclo para simular N lanzamientos
    for i in range(1, veces + 1):
        # Generar un número aleatorio entre 1 y 6
        resultado_dado = random.randint(1, 6)
        
        # Determinar si el resultado es par o impar usando el módulo (%)
        if resultado_dado % 2 == 0:
            pares_generados += 1
        else:
            impares_generados += 1
            
    # Mostrar el reporte final
    print("-" * 36)
    print("      REPORTE DE PARES E IMPARES    ")
    print("-" * 36)
    print(f"Total de lanzamientos: {veces}")
    print(f"Total de tiros PARES: {pares_generados}")
    print(f"Total de tiros IMPARES: {impares_generados}")
    print("-" * 36)

# Proceso Principal
if __name__ == "__main__":
    print("RETO 5: CONTEO DE PARES E IMPARES")
    try:
        # 1. Solicitar el número de veces que se desea lanzar el dado
        num_lanzamientos = int(input("Ingrese el número de lanzamientos que va a efectuar: "))
        
        if num_lanzamientos >= 0:
            # 2. Ejecutar la función
            contar_pares_impares(num_lanzamientos)
        else:
            print("El número de lanzamientos debe ser no negativo.")
            
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")