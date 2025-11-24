import random

# Reto condicional 1 (Simulación de Dados).
# Simula el lanzamiento de dos dados, verifica si son iguales (YOU WIN/GAME OVER),
# y verifica si cada dado es PAR o IMPAR.

def verificar_par_impar(dado, nombre):
    """Función auxiliar para validar y mostrar si un dado es PAR o IMPAR."""
    if dado % 2 == 0:
        print(f"El {nombre} ({dado}) es PAR.")
    else:
        print(f"El {nombre} ({dado}) es IMPAR.")

def reto_simulacion_dados():
    """Implementa la lógica del lanzamiento de dos dados con condicionales."""
    print("--- Reto Condicional 4: Simulación de Lanzamiento de Dos Dados ---")
    
    # Generar números aleatorios entre 1 y 6 para simular los dados
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    
    print(f"Lanzamiento del Dado 1: {dado_1}")
    print(f"Lanzamiento del Dado 2: {dado_2}")
    
    # Validación de igualdad (Condicional principal)
    # Si los dados son iguales, muestra YOU WIN, de lo contrario, GAME OVER. 
    if dado_1 == dado_2:
        print("\n¡YOU WIN! (Ambos dados son iguales)")
    else:
        print("\nGAME OVER (Los dados son diferentes)")
        
    # Validación de Par o Impar para cada dado 
    print("\n--- Análisis Individual ---")
    verificar_par_impar(dado_1, "Dado 1")
    verificar_par_impar(dado_2, "Dado 2")

if __name__ == "__main__":
    reto_simulacion_dados()