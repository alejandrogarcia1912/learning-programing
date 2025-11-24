Algoritmo Reto_Condicional_4_Calculadora
	// 1. Definición de variables
	Definir num1, num2, resultado Como Real
	Definir opcion Como Entero
	
	// 2. Solicitud de números
	Escribir "Ingrese el primer número:"
	Leer num1
	Escribir "Ingrese el segundo número:"
	Leer num2
	
	// 3. Mostrar Menú
	Escribir ""
	Escribir "--- MENÚ DE OPERACIONES ---"
	Escribir "[1]. Sumar"
	Escribir "[2]. Restar"
	Escribir "[3]. Multiplicar"
	Escribir "[4]. Dividir"
	Escribir "[5]. Todas"
	Escribir "---------------------------"
	Escribir "Ingrese la opción deseada [1-5]:"
	Leer opcion
	
	// 4. Estructura Condicional Múltiple (Segun)
	Segun opcion Hacer
		
			// CASO 1: Sumar
		1:
			resultado <- num1 + num2 // Asignación con '<-'
			Escribir "Resultado de la Suma: ", resultado
			
			// CASO 2: Restar
		2:
			resultado <- num1 - num2 // Asignación con '<-'
			Escribir "Resultado de la Resta: ", resultado
			
			// CASO 3: Multiplicar
		3:
			resultado <- num1 * num2 // Asignación con '<-'
			Escribir "Resultado de la Multiplicación: ", resultado
			
			// CASO 4: Dividir (Requiere validación de división por cero)
		4:
			Si (num2 <> 0) Entonces
				resultado <- num1 / num2 // Asignación con '<-'
				Escribir "Resultado de la División: ", resultado
			Sino
				Escribir "Error: No se puede dividir por cero."
			FinSi
			
			// CASO 5: Todas las operaciones
		5:
			Escribir "--- Resultados de Todas las Operaciones ---"
			Escribir "Suma: ", num1 + num2
			Escribir "Resta: ", num1 - num2
			Escribir "Multiplicación: ", num1 * num2
			Si (num2 <> 0) Entonces
				Escribir "División: ", num1 / num2
			Sino
				Escribir "División: Error (división por cero)"
			FinSi
			
			// Opción por defecto (opción inválida)
		De Otro Modo:
			Escribir "Opción no válida. Por favor, ingrese un número entre 1 y 5."
			
  FinSegun
FinAlgoritmo