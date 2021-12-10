from tkinter import *

ventana = tk()
ventana.title("calculadora")

i = 0
#entrada 
e_texto = entry (ventana, font= ("calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)

#funciones
def click_boton(valor):
	global i
	e_texto.insert(i, valor)
	i += 1

def borrar():
	e_texto.delete(0, end)
	i = 0

def hacer_operacion():
	ecuacion = e_texto.get()
	resultado = eval(ecuacion)
	e_texto.delete(0, end)
	e_texto.insert(0, resultado)
	i = 0

#botones
boton1 = button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton2 = button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton3 = button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = button(ventana, text = "0", width = 13, height = 2, command = lambda: click_boton(0))

boton_borrar = button(ventana, text = "ac", width = 5, height = 2, command = lambda: borrar())
boton_parentesis1 = button(ventana, text = "(", width = 5, height = 2, command = lambda: click_boton("("))
boton_parentesis2 = button(ventana, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
boton_punto = button(ventana, text = ".", width = 5, height = 2, command = lambda: click_boton("."))

boton_division = button(ventana, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
boton_multiplicacion = button(ventana, text = "x", width = 5, height = 2, command = lambda: click_boton("*"))
boton_suma = button(ventana, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
boton_resta = button(ventana, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
boton_igual = button(ventana, text = "=", width = 5, height = 2, command = lambda: hacer_operacion())

#agregar botones en pantalla
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_multiplicacion.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0,columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)



ventana.mainloop()