SubProceso LanzarHastaDobleSeis
    // Definición de variables
    Definir dado1, dado2, contador_tiros Como Entero;
    
    // Inicialización del contador de intentos
    contador_tiros <- 0;
    
    Escribir "RETO 4: LANZAR DOS DADOS HASTA OBTENER UN PAR DE SEIS (6, 6)";
    Escribir "--------------------------------------------------------";
    
    // El ciclo se repite al menos una vez y hasta que se cumpla la condición de salida
    Repetir
        // 1. Incrementar el contador de tiros
        contador_tiros <- contador_tiros + 1;
        
        // 2. Lanzar los dos dados
        dado1 <- Aleatorio(1, 6);
        dado2 <- Aleatorio(1, 6);
        
        // 3. Mostrar el resultado del tiro actual
        Escribir "Tiro #", contador_tiros, ": Resultados (", dado1, ", ", dado2, ")";
        
        // La condición de parada es: (dado1 = 6 Y dado2 = 6)
    Hasta Que (dado1 = 6 Y dado2 = 6)
    
    Escribir "--------------------------------------------------------";
    Escribir "¡CONDICIÓN CUMPLIDA!";
    Escribir "Se ha generado un PAR de SEIS (6, 6).";
    Escribir "Total de intentos necesarios: ", contador_tiros;
FinSubProceso

Algoritmo Reto4_ParDeSeis
    // Llamada al SubProceso
    LanzarHastaDobleSeis; 
FinAlgoritmo