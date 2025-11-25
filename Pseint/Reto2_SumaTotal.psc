SubProceso SumarLanzamientos(veces)
    // Definición de variables
    Definir i, resultado_dado, suma_total Como Entero;
    
    // Inicialización del acumulador antes del ciclo
    suma_total <- 0;
    
    Escribir "Iniciando ", veces, " lanzamientos...";
    Escribir "-----------------------------";
    
    // Ciclo para simular N lanzamientos
    Para i <- 1 Hasta veces Con Paso 1 Hacer
        // Generar un número aleatorio entre 1 y 6
        resultado_dado <- Aleatorio(1, 6);
        
        // Mostrar el resultado de este tiro
        Escribir "Tiro #", i, ": ", resultado_dado;
        
        // Acumular el resultado en la variable suma_total
        suma_total <- suma_total + resultado_dado;
    FinPara
    
    // Mostrar el reporte final
    Escribir "-----------------------------";
    Escribir "Total de lanzamientos: ", veces;
    Escribir "La suma total de los valores generados es: ", suma_total;
FinSubProceso // El SubProceso no devuelve valor

Algoritmo Reto2_SumaTotal
    // Definición de variables para el algoritmo principal
    Definir num_lanzamientos Como Entero;
    
    // 1. Solicitar el número de veces que se desea lanzar el dado
    Escribir "RETO 2: SUMA TOTAL DE LANZAMIENTOS";
    Escribir "Ingrese el número de veces que desea lanzar el dado:";
    Leer num_lanzamientos;
    
    // 2. Ejecutar el subproceso, enviando el número de lanzamientos como argumento
    // NOTA: La llamada se hace pasando la variable entre paréntesis.
    SumarLanzamientos(num_lanzamientos);
FinAlgoritmo