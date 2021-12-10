Algoritmo areas
	definir opc como entero 
	definir tri, cuad, cir como real
	escribir "por favor ingrese una opcion"
	escribir "0: calcular area del cuadrado"
	escribir "1: calcular area del triangulo"
	escribir "2: calcular area del circulo"
	leer opc
	Segun opc Hacer
		0:
			escribir "area del cuadrado"
			escribir"ingrese el lado"
			leer diez
			cuad <- 1 * 1
			escribir "el area es: ", cuad 
		1:
			escribir "area del triangulo"
			escribir "ingrese la base"
			leer b
			escribir "ingrese la altura"
			leer h
			tri <- (b * h) / 2
			
		2:
			escribir "area del circulo"
			escribir "ingrese el radio"
			leer r
			cir <- PI *r^2
			escribir "el area es: ", cir
			
		De Otro Modo:
			
			escribir "opcion invalida"
	Fin Segun
	
FinAlgoritmo
