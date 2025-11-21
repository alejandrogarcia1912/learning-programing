Funcion msg <- ShowGreeting2 ( userName )
	Escribir "Hello ", userName, ", welcome"
Fin Funcion

Algoritmo function3
	Definir userName, message Como Caracter
	Escribir "Enter your name: "
	Leer user_Name
	
	message = ShowGreeting2(user_Name)
	Escribir message
FinAlgoritmo
