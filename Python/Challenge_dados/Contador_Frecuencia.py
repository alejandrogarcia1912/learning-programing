import random

def contar_frecuencia(veces):
    """
    Realiza 'veces' lanzamientos de un dado y cuenta la frecuencia de cada resultado [1-6].
    """
    # Inicializar el diccionario de contadores para cada número del 1 al 6
    contadores_dado = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    print(f"Iniciando {veces} lanzamientos...")
    print("-" * 32)
    
    # Ciclo para simular N lanzamientos
    for i in range(1, veces + 1):
        # Generar un número aleatorio entre 1 y 6
        resultado_dado = random.randint(1, 6)
        
        # Mostrar el resultado de este tiro (opcional)
        # print(f"Tiro #{i}: {resultado_dado}")
        
        # Incrementar el contador correspondiente al resultado obtenido
        contadores_dado[resultado_dado] += 1
        
    # Mostrar el reporte final de frecuencias
    print("-" * 32)
    print("      REPORTE DE FRECUENCIAS    ")
    print("-" * 32)
    print(f"Total de lanzamientos: {veces}")
    
    # Iterar sobre el diccionario para mostrar la frecuencia de cada número [1-6]
    # Se utiliza sorted() para asegurar que los resultados se muestren en orden 1, 2, 3...
    for numero in sorted(contadores_dado.keys()):
        print(f"El número {numero} se generó: {contadores_dado[numero]} veces.")
    print("-" * 32)

# Proceso Principal
if __name__ == "__main__":
    print("RETO 3: CONTEO DE FRECUENCIA POR NÚMERO")
    try:
        # 1. Solicitar el número de veces que se desea lanzar el dado
        num_lanzamientos = int(input("Ingrese el número de veces que desea lanzar el dado: "))
        
        if num_lanzamientos >= 0:
            # 2. Ejecutar la función
            contar_frecuencia(num_lanzamientos)
        else:
            print("El número de lanzamientos debe ser no negativo.")
            
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")