SubProceso ContarFrecuencia(veces)
    // Definición de variables
    Definir i, resultado_dado Como Entero;
    
    // 1. CORRECCIÓN DEL ERROR DE DIMENSIONAMIENTO:
    // Se define el arreglo de 7 posiciones (índices 1 a 6 se usarán).
    Definir contadores_dado Como Entero; // Se define primero como variable (opcional)
    Dimensión contadores_dado[7]; // Se establece la dimensión en una línea separada y usando "Dimensión"
    
    // 2. CORRECCIÓN DEL ERROR DE IDENTIFICADOR:
    // Al estar la dimensión definida antes, el identificador ya es un arreglo.
    
    // Inicializar todos los contadores a cero (solo del 1 al 6)
    Para i <- 1 Hasta 6 Hacer
        contadores_dado[i] <- 0;
    FinPara
    
    Escribir "Iniciando ", veces, " lanzamientos...";
    Escribir "--------------------------------";
    
    // Ciclo para simular N lanzamientos
    Para i <- 1 Hasta veces Con Paso 1 Hacer
        resultado_dado <- Aleatorio(1, 6);
        Escribir "Tiro #", i, ": ", resultado_dado;
        
        // Incrementar el contador correspondiente
        contadores_dado[resultado_dado] <- contadores_dado[resultado_dado] + 1;
    FinPara
    
    // Mostrar el reporte final de frecuencias
    Escribir "--------------------------------";
    Escribir "      REPORTE DE FRECUENCIAS    ";
    Escribir "--------------------------------";
    Escribir "Total de lanzamientos: ", veces;
    
    // Mostrar la frecuencia de cada número [1-6]
    Para i <- 1 Hasta 6 Hacer
        Escribir "El número ", i, " se generó: ", contadores_dado[i], " veces.";
    FinPara
    Escribir "--------------------------------";
FinSubProceso

Algoritmo Reto3_ConteoFrecuencia
    // Definición de variables para el algoritmo principal
    Definir num_lanzamientos Como Entero;
    
    Escribir "RETO 3: CONTEO DE FRECUENCIA POR NÚMERO";
    
    // 1. Solicitar el número de veces que se desea lanzar el dado
    Escribir "Ingrese el número de veces que desea lanzar el dado:";
    Leer num_lanzamientos;
    
    // 2. Ejecutar el subproceso
    ContarFrecuencia(num_lanzamientos);
FinAlgoritmo