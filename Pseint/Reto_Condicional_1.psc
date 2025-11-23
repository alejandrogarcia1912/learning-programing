Algoritmo Reto_Condicional_1
	
    Definir dado1, dado2 Como Entero
	
    // Generar valores aleatorios entre 1 y 6
    dado1 <- Aleatorio(1, 6)
    dado2 <- Aleatorio(1, 6)
	
    Escribir "Dado 1: ", dado1
    Escribir "Dado 2: ", dado2
	
    // Validar si cada dado es par o impar
    Si (dado1 MOD 2 = 0) Entonces
        Escribir "Dado 1 es PAR"
    Sino
        Escribir "Dado 1 es IMPAR"
    FinSi
	
    Si (dado2 MOD 2 = 0) Entonces
        Escribir "Dado 2 es PAR"
    Sino
        Escribir "Dado 2 es IMPAR"
    FinSi
	
    // Validar si los dos dados son iguales
    Si (dado1 = dado2) Entonces
        Escribir "YOU WIN"
    Sino
        Escribir "GAME OVER"
    FinSi
	
FinAlgoritmo

