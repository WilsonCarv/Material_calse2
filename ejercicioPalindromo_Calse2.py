#Segundo Ejercicio
#Palindromo de una palabra puedo sacar otra con las mismas letras
palabra1=['c','a','r']
import math
from random import randint
palabra2=[]
numerosUsados=[]

for i in palabra1:
    numero=(randint(0, len(palabra1)-1))
    
    if numero in numerosUsados:
    	numero=(randint(0, len(palabra1)))

    	
    else:
    	numerosUsados.append(numero)
    	palabra2 +=  [palabra1[numero]] 
      
         
print(palabra2,numerosUsados)	


    