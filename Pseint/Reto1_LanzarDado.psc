SubProceso DeterminarParImpar
    // Definición de variables
    Definir resultado Como Entero;
	
    resultado <- Aleatorio(1, 6);
    Escribir "El dado ha sido lanzado. Resultado: ", resultado;
	
    Si (resultado MOD 2 == 0) Entonces
        Escribir "El número ", resultado, " es PAR.";
    SiNo
        Escribir "El número ", resultado, " es IMPAR.";
    FinSi
	
FinSubProceso // NOTA: No se usa '()' aquí en la definición

Algoritmo Reto1_LanzarDado
    // Llamada al SubProceso sin paréntesis si no tiene argumentos
    DeterminarParImpar; 
FinAlgoritmo