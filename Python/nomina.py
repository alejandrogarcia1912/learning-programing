totalEmpleados = 0
totalM = 0
totalF = 0
totalO = 0
totalSalarios = 0
sumaEdades = 0
anioActual = 2025
continuar = "S"
while continuar == "S":
    print("Registro de Empleados")
    print("Nombre")
    nombre = input()
    print("email")
    email = input()
    print("numero de celular")
    celular = input()
    print("Genero [M, F, O]")
    genero = input()
    while genero != "M" and genero != "F" and genero != "O":
        print("Valor inválido. Digite M, F o O")
        genero = input()
        genero = ToUpper(genero)
    print("Salario")
    salario = float(input())
    print("Año de nacimiento")
    anioNacimiento = int(input())
    edad = anioActual - anioNacimiento
    totalEmpleados = totalEmpleados + 1
    totalSalarios = totalSalarios + salario
    sumaEdades = sumaEdades + edad
    if genero == "M":
        totalM = totalM + 1
    else:
        if genero == "F":
            totalF = totalF + 1
        else:
            totalO = totalO + 1
    print("¿Desea agregar otro? (S/N)")
    continuar = input()
print("REPORTE FINAL")
print("Total empleados: " + str(totalEmpleados))
print("Total hombres (M): " + str(totalM))
print("Total mujeres (F): " + str(totalF))
print("Total otros (O): " + str(totalO))
print("Total salarios: " + str(totalSalarios))
print("Promedio edades: " + str(float(sumaEdades) / totalEmpleados))
