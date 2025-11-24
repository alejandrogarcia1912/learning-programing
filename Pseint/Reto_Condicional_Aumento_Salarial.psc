Algoritmo Reto_Condicional_Aumento_Salarial
	// 1. Definición de variables
	Definir nombre, genero, tipo_id, apellidos, direccion, telefono Como Caracter
	Definir salario_base, aumento, salario_final, monto_aumento Como Real
	Definir anio_nacimiento Como Entero
	
	// 2. Solicitud de datos
	Escribir "--- INGRESO DE DATOS DEL EMPLEADO ---"
	Escribir "Tipo de identificación (CC, PS, CE, CI):"
	Leer tipo_id
	Escribir "Nombres:"
	Leer nombre
	Escribir "Apellidos:"
	Leer apellidos
	
	// Solicitud y validación de Género
	Repetir
		Escribir "Género (M: Mujer / H: Hombre):"
		Leer genero
		genero <- Mayusculas(genero) // Asignación con <-
	Mientras Que (genero <> "M" Y genero <> "H")
	
	Escribir "Año de nacimiento:"
	Leer anio_nacimiento
	Escribir "Dirección:"
	Leer direccion
	Escribir "Teléfono:"
	Leer telefono
	
	// Solicitud de Salario Base
	Escribir "Salario Base (ej: 1500000):"
	Leer salario_base
	
	// 3. Inicialización
	aumento <- 0.0 // Asignación con <-
	
	// 4. Lógica Condicional para el Cálculo del Aumento
	
	// CASO 1: Salario menor o igual a 1,200,000
	Si (salario_base <= 1200000) Entonces
		Si (genero == "M") Entonces
			aumento <- 0.10 // 10%
		Sino
			aumento <- 0.08 // 8%
		FinSi
		
		// CASO 2: Salario entre 1,200,000 y 2,000,000
	Sino Si (salario_base > 1200000 Y salario_base < 2000000) Entonces
			aumento <- 0.05 // 5% para ambos
			
			// CASO 3: Salario mayor o igual a 2,000,000
		Sino
			Si (genero == "M") Entonces
				aumento <- 0.03 // 3%
			Sino
				aumento <- 0.025 // 2.5%
			FinSi
		FinSi
		
		// 5. Cálculo del Salario Final
		monto_aumento <- salario_base * aumento // Cálculo del monto
		salario_final <- salario_base + monto_aumento // Cálculo del total
		
		// 6. Presentación de Resultados
		Escribir ""
		Escribir "--- RESULTADO DEL AUMENTO SALARIAL ---"
		Escribir "Empleado: ", nombre, " ", apellidos // Concatenación con comas
		Escribir "Salario Base: $", salario_base // Concatenación con comas
		Escribir "Porcentaje de Aumento Aplicado: ", aumento * 100, "%"
		Escribir "Monto del Aumento: $", monto_aumento
		Escribir "SALARIO FINAL: $", salario_final
	FINSI
FinAlgoritmo