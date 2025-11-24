# Reto Condicional 5: Cálculo de Aumento Salarial.
# Script en Python (para VS Code).

def reto_aumento_salarial():
    """Calcula el salario final de un empleado aplicando un aumento condicional
    basado en el salario base y el género, según las reglas especificadas."""
    
    print("--- Reto Condicional 5: Cálculo de Aumento Salarial ---")
    
    try:
        # 1. Solicitud de datos del empleado
        print("\n--- INGRESO DE DATOS DEL EMPLEADO ---")
        # Se solicitan los datos requeridos, aunque no todos se usen en el cálculo
        tipo_id = input("Tipo de identificación (CC, PS, CE, CI): ")
        nombre = input("Nombres: ")
        apellidos = input("Apellidos: ")
        
        # Validación y lectura del género (M o H)
        while True:
            genero = input("Género (M: Mujer / H: Hombre): ").strip().upper()
            if genero in ('M', 'H'):
                break
            print("Entrada no válida. Por favor, ingrese 'M' o 'H'.")
            
        anio_nacimiento = input("Año de nacimiento: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        salario_base = float(input("Salario Base (ej: 1500000): "))
        
        aumento_porcentaje = 0.0
        
        # 2. Lógica Condicional (Estructura if/elif/else anidada)
        
        # CASO 1: Salario menor o igual que 1,200,000
        if salario_base <= 1200000:
            if genero == 'M':
                aumento_porcentaje = 0.10  # 10%
            else: # genero == 'H'
                aumento_porcentaje = 0.08  # 8%
                
        # CASO 2: Salario mayor a 1,200,000 y menor a 2,000,000
        elif salario_base < 2000000:
            aumento_porcentaje = 0.05  # 5% (Ambos géneros)
            
        # CASO 3: Salario mayor o igual a 2,000,000
        else: # salario_base >= 2000000
            if genero == 'M':
                aumento_porcentaje = 0.03  # 3%
            else: # genero == 'H'
                aumento_porcentaje = 0.025 # 2.5%
        
        # 3. Cálculo del Salario Final
        monto_aumento = salario_base * aumento_porcentaje
        salario_final = salario_base + monto_aumento
        
        # 4. Presentación de Resultados
        print("\n--- RESULTADO DEL AUMENTO SALARIAL ---")
        print(f"Empleado: {nombre} {apellidos}")
        print(f"Salario Base: ${salario_base:,.2f}")
        print(f"Porcentaje de Aumento Aplicado: {aumento_porcentaje * 100}%")
        print(f"Monto del Aumento: ${monto_aumento:,.2f}")
        print(f"SALARIO FINAL: ${salario_final:,.2f}")
        
    except ValueError:
        print("Error: Asegúrese de ingresar un valor numérico válido para el salario.")

if __name__ == "__main__":
    reto_aumento_salarial()