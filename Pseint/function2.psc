Funcion showGreeting (userName)
	Escribir "Hello ", userName, ", welcome"
Fin Funcion

Algoritmo function2
	Definir user_Name Como Caracter
	Escribir "Enter your name: "
	Leer user_Name
	
	showGreeting(user_Name)
FinAlgoritmo
