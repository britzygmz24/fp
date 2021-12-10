Algoritmo calculadora
	// definir variables
	definir n1, n2, opc, res como entero;
	// pedir datos de entrada 
	escribir "ingrese numero 1"
	leer n1 ;
	escribir "ingrese numero 2";
	leer n2 ;
	
	//opciones 
	escribir "ingrese una opcion"
	escribir "1. sumar" ;
	escribir "2. restar" ;
	escribir "3. multiplicar" ;
	escribir "4. dividir" ;
	leer  opc ;
	
	// Proceso 
	Segun opc Hacer
		opcion_1:
			res = n1 + n2;
			escribir "la suma es", res;
		opcion_2:
			res = n1- n2;
			escribir "la resta es", res;
		opcion_3:
			res = n1 * n2;
			escribir "la multiplicacion es", res;
		De Otro Modo:
			escribir "opcion incorrecta";
	Fin Segun
	
	
FinAlgoritmo
