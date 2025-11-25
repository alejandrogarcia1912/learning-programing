import random

def lanzar_hasta_doble_seis():
    """
    Lanza dos dados repetidamente hasta que ambos muestren 6.
    """
    contador_tiros = 0
    
    print("RETO 4: LANZAR DOS DADOS HASTA OBTENER UN PAR DE SEIS (6, 6)")
    print("-" * 56)
    
    # Usamos un ciclo infinito, saliendo con 'break' cuando se cumpla la condición
    while True:
        contador_tiros += 1
        
        # 1. Lanzar los dos dados
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        
        # 2. Mostrar el resultado del tiro actual
        print(f"Tiro #{contador_tiros}: Resultados ({dado1}, {dado2})")
        
        # 3. Verificar la condición de salida
        if dado1 == 6 and dado2 == 6:
            break
            
    print("-" * 56)
    print("¡CONDICIÓN CUMPLIDA!")
    print("Se ha generado un PAR de SEIS (6, 6).")
    print(f"Total de intentos necesarios: {contador_tiros}")

# Proceso Principal
if __name__ == "__main__":
    lanzar_hasta_doble_seis()