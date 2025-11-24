import random

# --- 1. Definición de Funciones ---

def solicitar_jugadores():
    """Solicita y valida la cantidad de jugadores (Mínimo 2, máximo 4)."""
    while True:
        try:
            num_jugadores = int(input("Ingrese la cantidad de jugadores (2 a 4): "))
            # Validación de la regla: Mínimo 2, máximo 4 
            if 2 <= num_jugadores <= 4:
                return num_jugadores
            else:
                print("⚠️ La cantidad de jugadores debe ser entre 2 y 4. Intente de nuevo.")
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, ingrese un número entero.")

def seleccionar_nivel():
    """Muestra el menú y retorna la posición de la meta."""
    niveles = {
        1: 20, # Nivel básico (Tablero de 20 posiciones) [cite: 26]
        2: 30, # Nivel intermedio (Tablero de 30 posiciones) [cite: 27]
        3: 50, # Nivel avanzado (Tablero de 50 posiciones) [cite: 28]
        4: 100 # Nivel experto (Tablero de 100 posiciones) [cite: 28]
    }
    
    print("\n--- Nivel de Tablero a Jugar ---")
    print("1. Nivel básico (Tablero de 20 posiciones) [cite: 26]")
    print("2. Nivel intermedio (Tablero de 30 posiciones) [cite: 27]")
    print("3. Nivel avanzado (Tablero de 50 posiciones) [cite: 28]")
    print("4. Nivel experto (Tablero de 100 posiciones) [cite: 28]")

    while True:
        try:
            opcion = int(input("Seleccione un nivel (1-4): "))
            if opcion in niveles:
                # La meta es la última posición del tablero 
                return niveles[opcion]
            else:
                print("⚠️ Opción inválida. Por favor, seleccione 1, 2, 3 o 4.")
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, ingrese un número entero.")

def lanzar_dados():
    """Simula el lanzamiento de dos dados (1-6)."""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# --- 2. Lógica Principal del Juego ---

def iniciar_juego():
    """Simula el comportamiento del juego 'Carrera Numérica'[cite: 34]."""
    print("🎲 **Bienvenido a Carrera Numérica** 🚗")

    # A. Inicializar Jugadores
    num_jugadores = solicitar_jugadores()
    # Inicializar la posición de cada jugador a 0 y pares consecutivos a 0
    posiciones = [0] * num_jugadores
    pares_consecutivos = [0] * num_jugadores
    
    # B. Seleccionar Nivel
    meta = seleccionar_nivel()
    print(f"\n--- Juego Iniciado ---")
    print(f"Número de Jugadores: {num_jugadores}")
    print(f"Posición de la Meta: {meta} \n")

    jugador_actual = 0
    juego_terminado = False

    # Proceso C: El juego finaliza ÚNICAMENTE cuando un jugador llega a la meta
    # o cumple la regla D.
    while not juego_terminado:
        print(f"➡️ Turno del Jugador {jugador_actual + 1} (Posición actual: {posiciones[jugador_actual]})")

        # C. Lanzar los dos dados 
        d1, d2 = lanzar_dados()
        movimiento = d1 + d2
        print(f"   Lanzamiento: {d1} y {d2}. Se mueve {movimiento} posiciones.")
        
        # 3. Verificar Pares Consecutivos (Regla D)
        if d1 == d2:
            pares_consecutivos[jugador_actual] += 1
            print(f"   ¡Par! ({d1} y {d2}). Pares consecutivos: {pares_consecutivos[jugador_actual]}")
            
            # Si el jugador obtiene 3 pares CONSECUTIVOS, es el ganador 
            if pares_consecutivos[jugador_actual] == 3:
                print(f"\n🎉 **¡FELICIDADES! El Jugador {jugador_actual + 1} GANA directamente por obtener 3 pares consecutivos!** 🎉 ")
                juego_terminado = True
                continue # Terminar el bucle de juego
        else:
            # Si no es un par, se reinicia el contador
            pares_consecutivos[jugador_actual] = 0

        # 2. Actualizar Posición
        posiciones[jugador_actual] += movimiento
        print(f"   Nueva posición: {posiciones[jugador_actual]}")

        # 4. Verificar Condición de Victoria (Regla de Meta)
        # Gana quién llegue con el valor igual o mayor al de la meta 
        if posiciones[jugador_actual] >= meta:
            print(f"\n🏆 **¡FELICIDADES! El Jugador {jugador_actual + 1} GANA al alcanzar la Meta ({meta})!** 🏆 ")
            juego_terminado = True
            continue # Terminar el bucle de juego

        # Fin del Turno: Pasar al siguiente jugador
        jugador_actual = (jugador_actual + 1) % num_jugadores
        print("-" * 30)

# --- Ejecución ---
if __name__ == "__main__":
    iniciar_juego()