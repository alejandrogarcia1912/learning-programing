import random

def lanzamiento_interactivo():
    """
    Permite al jugador lanzar un dado repetidamente y genera un reporte al finalizar.
    """
    total_tiros = 0
    suma_total = 0
    pares_generados = 0
    impares_generados = 0
    
    print("RETO 6: LANZAMIENTO INTERACTIVO CON REPORTE")
    print("-" * 44)
    
    while True:
        # 1. Simular el lanzamiento
        total_tiros += 1
        resultado_dado = random.randint(1, 6)
        
        print(f"Tiro #{total_tiros}: ¡Ha salido el número {resultado_dado}!")
        
        # 2. Acumular y contar
        suma_total += resultado_dado
        
        # Contar pares e impares
        if resultado_dado % 2 == 0:
            pares_generados += 1
        else:
            impares_generados += 1
        
        # 3. Preguntar si desea volver a lanzar
        respuesta = input("\n¿Desea volver a lanzar? (S/N): ").upper()
        print("-" * 44)
        
        # Condición de salida: si la respuesta no es 'S'
        if respuesta != 'S':
            break

    # Generar el reporte final
    print("FIN DE LA PARTIDA. Generando reporte...")
    print("\n" + "=" * 44)
    print("          REPORTE FINAL DE JUEGO            ")
    print("=" * 44)
    print(f"Total de tiros efectuados:    {total_tiros}")
    print(f"Suma total de los tiros efectuados: {suma_total}")
    print(f"Total de pares generados:     {pares_generados}")
    print(f"Total de impares generados:   {impares_generados}")
    print("=" * 44)

# Proceso Principal
if __name__ == "__main__":
    lanzamiento_interactivo()