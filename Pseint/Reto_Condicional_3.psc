ALGORITMO Reto_Condicional_3
	// Solicitar un número entero al usuario
	ESCRIBIR "Por favor, ingrese un número entero (positivo o negativo):"
	LEER numero
	
	// Manejo del caso especial CERO
	SI (numero == 0) ENTONCES
		ESCRIBIR "El número 0 es un número PAR, considerado ni positivo ni negativo en este contexto."
		// El programa finaliza aquí para el caso 0
	SINO
		
		// --- PRIMERA CONDICIÓN: POSITIVO o NEGATIVO ---
		SI (numero > 0) ENTONCES
			// El número es POSITIVO. Ahora verificamos Par/Impar.
			SI (numero MOD 2 == 0) ENTONCES
				ESCRIBIR "El número " , numero , " es PAR POSITIVO."
			SINO
				ESCRIBIR "El número " , numero , " es IMPAR POSITIVO."
				FINSI
				
			SINO
				// El número es NEGATIVO. Ahora verificamos Par/Impar.
				// Nota: El operador módulo (%) en muchos lenguajes maneja el signo del dividendo,
				// por lo que si el número es negativo, el resto es 0 (Par) o -1 (Impar).
				SI (numero MOD 2 == 0) ENTONCES
					ESCRIBIR "El número " , numero , " es PAR NEGATIVO."
				SINO
					ESCRIBIR "El número " , numero , " es IMPAR NEGATIVO."
					FINSI
					
					FINSI // Fin de la condición Positivo/Negativo
					
					FINSI // Fin de la condición Cero
FINALGORITMO