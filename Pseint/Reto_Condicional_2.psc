ALGORITMO Reto_Condicional_2
	// Solicitar un n?mero entero al usuario
	ESCRIBIR "Por favor, ingrese un n?mero entero (positivo o negativo):"
	LEER numero
	
	// Validar si el n?mero es par o impar
	// Un n?mero es PAR si el residuo de la divisi?n entre 2 es 0 (numero MOD 2 = 0)
	SI (numero MOD 2 == 0) ENTONCES
		ESCRIBIR "El n?mero " , numero , " es PAR."
	SINO
		ESCRIBIR "El n?mero " , numero , " es IMPAR."
	FINSI
FINALGORITMO