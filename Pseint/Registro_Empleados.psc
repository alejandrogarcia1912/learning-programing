Algoritmo Registro_Empleados
	
    Definir nombre, email, celular, genero Como Cadena
    Definir salario, total_salarios, suma_edades Como Real
    Definir anio_nac, total_empleados, total_m, total_f, total_o, anio_actual, edad Como Entero
    Definir continuar Como Cadena
	
    total_empleados <- 0
    total_m <- 0
    total_f <- 0
    total_o <- 0
    total_salarios <- 0
    suma_edades <- 0
	
    anio_actual <- 2025   // Cambia si lo necesitas
	
    Repetir
		
        Escribir ""
        Escribir "----- Registro de empleado -----"
		
        Escribir "Nombres completos: "
        Leer nombre
		
        Escribir "Email: "
        Leer email
		
        Escribir "Número móvil: "
        Leer celular
		
        // ------------------------------
        // Validación del género
        // ------------------------------
        Repetir
            Escribir "Género [M-F-O]: "
            Leer genero
            genero <- Mayusculas(genero)
        Hasta Que (genero = "M") O (genero = "F") O (genero = "O")
		
        Escribir "Salario: "
        Leer salario
		
        Escribir "Año de nacimiento [AAAA]: "
        Leer anio_nac
		
        // Calcular edad
        edad <- anio_actual - anio_nac
		
        // Acumular datos
        total_empleados <- total_empleados + 1
        total_salarios <- total_salarios + salario
        suma_edades <- suma_edades + edad
		
        Si genero = "M" Entonces
            total_m <- total_m + 1
        Sino
            Si genero = "F" Entonces
                total_f <- total_f + 1
            Sino
                total_o <- total_o + 1
            FinSi
        FinSi
		
        // ------------------------------
        // Validación para continuar S/N
        // ------------------------------
        Repetir
            Escribir "¿Desea registrar otro empleado? (S/N): "
            Leer continuar
            continuar <- Mayusculas(continuar)
        Hasta Que (continuar = "S") O (continuar = "N")
		
    Hasta Que continuar = "N"
	
    // -------- REPORTE FINAL --------
    Escribir ""
    Escribir "======= REPORTE FINAL ======="
    Escribir "Total empleados registrados: ", total_empleados
    Escribir "Total género M: ", total_m
    Escribir "Total género F: ", total_f
    Escribir "Total género O: ", total_o
    Escribir "Total salarios a pagar: ", total_salarios
    Escribir "Promedio de edades: ", suma_edades / total_empleados
	
FinAlgoritmo
