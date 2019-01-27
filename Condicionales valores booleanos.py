#tipos de datos booleanos, se utiliza para contener 2 posibles valores , ya sea true o false
#Es falso cuando cuendo viene en None, false, zero para datos numericos
#Se puede utlizar con las tablas de la verdad, utilizando and, or, not
a=True
b=False
print(not a)
print(a|b)
print(a&b)
#Por ejemplo, paso un curso si: 
#Examen buen AND hago tareas AND asisto
examen_bueno=True
asisto=True
hagoTarea=True
#Si cambio el valor la salidad ya no va a ser true
#examen_bueno=None
examen_bueno=True
pasa=examen_bueno & asisto & hagoTarea
#Si le coloco un cero la salida va a ser cero ya que el resto de valores es tomado como numero
print(pasa)
#El uso del condicional If
#Despues de una exprexion deben de ir : ya que si no daria errror de syntaxis, se creara un nuevo nivel de identacion o de un bloque 
#Despues del if podemos invocar al else y daremos una opcion para que se ejecute la otra parte del codigo
#Ejemplo de condicional
#con la palabra pass no hace nada pero evitamos que de el error
#Debe de estar bien identado si no el codigo va a dar error de sintaxis
if examen_bueno&asisto&hagoTarea:
	pass
else:
	print('No aprobaste el curso')

if examen_bueno&asisto&hagoTarea:
	print('Aprobaste el curso!!')
	print('Fiesta!!')
else:
	print('No aprobaste el curso')
#El uso del if anidado
examen_bueno=False
if examen_bueno:
	if hagoTarea:
		if asisto:
			print("Fiesta!!")
else:
	print("No hay fiesta")

#El uso del elif
if hagoTarea:
	print('Hago la tarea')
elif examen_bueno:
	pass
#podemos compara numeros utilizando & | not
#podemos obtener el numero binario de un numero entero
print(bin(12))
#Para hacer comparaciones 
#<, <=, >, >=, ==, != ,is, is not
#los is y is not, es para la identidad es decir comparamos que si una variable es un numero o no
print(4==6)
print(4!=6)
a = None
print(a is None)
print(a is not None)





	

