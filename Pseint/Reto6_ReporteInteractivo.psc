SubProceso LanzamientoInteractivo
    // Definición de variables
    Definir respuesta Como Caracter;
    Definir resultado_dado, total_tiros, suma_total, pares_generados, impares_generados Como Entero;
    
    // Inicialización de contadores y acumuladores
    total_tiros <- 0;
    suma_total <- 0;
    pares_generados <- 0;
    impares_generados <- 0;
    respuesta <- "S"; // Inicializamos para entrar al ciclo
    
    Escribir "RETO 6: LANZAMIENTO INTERACTIVO CON REPORTE";
    Escribir "--------------------------------------------";
    
    // El ciclo se repite mientras el jugador quiera seguir lanzando ('S' o 's')
    Repetir
        // 1. Simular el lanzamiento
        total_tiros <- total_tiros + 1;
        resultado_dado <- Aleatorio(1, 6);
        
        Escribir "Tiro #", total_tiros, ": ¡Ha salido el número ", resultado_dado, "!";
        
        // 2. Acumular y contar
        suma_total <- suma_total + resultado_dado;
        
        // Determinar si es par o impar y contar
        Si (resultado_dado MOD 2 == 0) Entonces
            pares_generados <- pares_generados + 1; 
        SiNo
            impares_generados <- impares_generados + 1;
        FinSi
        
        // 3. Preguntar si desea volver a lanzar
        Escribir ""; // Salto de línea
        Escribir "¿Desea volver a lanzar? (S/N)";
        Leer respuesta;
        Escribir "--------------------------------------------";
        
        // Usamos Mayusculas(respuesta) para aceptar 's' o 'S'
    Hasta Que Mayusculas(respuesta) <> "S"
    
    // Una vez que el ciclo termina, se visualiza el reporte
    Escribir "FIN DE LA PARTIDA. Generando reporte...";
    Escribir "";
    Escribir "============================================";
    Escribir "          REPORTE FINAL DE JUEGO            ";
    Escribir "============================================";
    Escribir "Total de tiros efectuados:    ", total_tiros;
    Escribir "Suma total de los tiros efectuados: ", suma_total;
    Escribir "Total de pares generados:     ", pares_generados;
    Escribir "Total de impares generados:   ", impares_generados;
    Escribir "============================================";
FinSubProceso

Algoritmo Reto6_ReporteInteractivo
    // Llamada al SubProceso
    LanzamientoInteractivo;
FinAlgoritmo