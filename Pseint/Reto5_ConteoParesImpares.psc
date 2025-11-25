SubProceso ContarParesImpares(veces)
    // Definición de variables
    Definir i, resultado_dado, pares_generados, impares_generados Como Entero;
    
    // Inicialización de los contadores
    pares_generados <- 0;
    impares_generados <- 0;
    
    Escribir "Iniciando ", veces, " lanzamientos...";
    Escribir "------------------------------------";
    
    // Ciclo para simular N lanzamientos
    Para i <- 1 Hasta veces Con Paso 1 Hacer
        // Generar un número aleatorio entre 1 y 6
        resultado_dado <- Aleatorio(1, 6);
        
        // Mostrar el resultado (opcional)
        // Escribir "Tiro #", i, ": ", resultado_dado; 
        
        // Determinar si el resultado es par o impar
        Si (resultado_dado MOD 2 == 0) Entonces
            pares_generados <- pares_generados + 1; // El número es par
        SiNo
            impares_generados <- impares_generados + 1; // El número es impar
        FinSi
    FinPara
    
    // Mostrar el reporte final
    Escribir "------------------------------------";
    Escribir "      REPORTE DE PARES E IMPARES    ";
    Escribir "------------------------------------";
    Escribir "Total de lanzamientos: ", veces;
    Escribir "Total de tiros PARES: ", pares_generados;
    Escribir "Total de tiros IMPARES: ", impares_generados;
    Escribir "------------------------------------";
FinSubProceso

Algoritmo Reto5_ConteoParesImpares
    // Definición de variables para el algoritmo principal
    Definir num_lanzamientos Como Entero;
    
    Escribir "RETO 5: CONTEO DE PARES E IMPARES";
    
    // 1. Solicitar el número de veces que se desea lanzar el dado
    Escribir "Ingrese el número de lanzamientos que va a efectuar:";
    Leer num_lanzamientos;
    
    // 2. Ejecutar el subproceso
    ContarParesImpares(num_lanzamientos);
FinAlgoritmo