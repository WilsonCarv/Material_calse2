#Las listas es una coleccion de elemntos, sea objetos, o valores primitivos
#Seprados por coma lo elementos
#Lo que ingresamos ahi se queda con el tipo que es
a=[]
print(type(a))
a=[1,2,3,99,1000]
b=[10,11,'a']
c=['a','b',None]
d=['a','b',None,[]]
print(a,b,c,d,)
print(len(a))
#Consulta si el elemnto x esta en la lista X =x in S
print(1 in a)
print (None in a)
print([]in [1,2,3,[]])
#para saber si ni esta= x not in s
#Para concatenar= s + t
original= [1,2,3]
nuevos = [4,5,6]
print(original + nuevos)
#s * n or n * s= clona la lista tanta veces que lo deseamos
print(original*4)
#s[i] para sabere el ultimo se pone el -1
print(original[-1])
print(original[0])
print(original[-2])
#s[i:j] obtenemos un subconjunto de elementos, un rango de elementos
nuevos= nuevos+[7,8,9,10]
print(nuevos[2:])
print(nuevos[:5])
print(nuevos[2:-2])
print(nuevos[1:10])
print(nuevos[-1:-2])
#s[i:j:k] obtenemos un subconjunto de elementos, dandole la longitud del saltos
print(nuevos[::])
#Con este le damos vuelta a la lista
print(nuevos[::-1])
#Este me lo dara de 2 en 2 
print(nuevos[::2])
#Los pares en reversa
print(nuevos[::-2])
#sacamos las posiciones impares
print(nuevos[1::2])
print(nuevos[::2]+ nuevos[1::2])
#len(s) = la longitud
print(len(nuevos))
#min(s)= el numero minimo(solo se aplica con numeros) 
print(min(nuevos))
#max(s)= el numero maximo(solo se aplica con numeros)
print(max(nuevos))
#s.index(x[,i[,j]]) indice de un numero
print(nuevos.index(9))
#s.count(xs) numero de veces que se encuenta un numero
lista=[1,1,1,1,1,1,2,3,4,2]
print(lista.count(1))
#como agregar elementos
nuevos.append(11)
print(nuevos)
#s[i]=x para reemplazar
nuevos[0]=1
print(nuevos)
#s[i:j]= t reemplazar por cierta cantidad de elementos
nuevos[0:1]=[2,1]
print(nuevos)
#del s[i:j] borrar elemto en alguna parte
del nuevos[0:2]
print(nuevos)
#s[i:j:k]= t
#del s[i:j:k]
#s.clear() borra lista
nuevos.clear()
print(nuevos)
#s.copy() copy lista
#s.extend(t) agregamos mas elementos, es como si lo hicieramos con el + 
nuevos=[1,2,3,4,5,6,7]
nuevos.extend([8,9])
print(nuevos)
#s*=n la lista s multiplicado por n
#s.insert= Inserta en una posicion especifica
#s.pop([i])= remueve el valor de una posicion especifica
nuevos.pop(2)
print(nuevos)
#s.reverse()= muestra los numeros en reversa
nuevos.reverse()
print(nuevos)
#Ejercicio de anagrama
#Son palabras que se pueden leer al derecho y al revez, por ejemplo= Ana y Salas
nombre1=['A','N','A']
nombre2=['A','N','A']


if(nombre1.reverse()==nombre2):
	print("Es anagrama")

else:
    print("No es anagrama")	



#Segundo Ejercicio
#Palindromo de una palabra puedo sacar otra con las mismas letras
palabra1=['p','r','o','g','r','a','m','a','c','i','o','n']
import math
from random import randint
palabra2=[]
palabra3= []
for i in palabra1:
	numero=(randint(0, len(palabra1)-1))

	palabra2 +=  [palabra1[numero]]


print(palabra2)	


#


