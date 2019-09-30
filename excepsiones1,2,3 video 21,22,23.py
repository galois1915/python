#las excepciones son errore que ocurren durante la ejecucion del programa
#la sintaxis del codigo es correcta pero durante la ejecucion ha ocurrido
# algo "inesperado"
#este tipo de errore de ejecucion se pueden controlar para que la ejecucion del 
#del programa continue .Eesto lo que se conose como"manejo o conrol de exexciones"

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	return num1/num2
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")

#si aproposito cometemos un erros como dividir un numero con cero
#	sale erros y el programa ignora todo lo demas que sique(todo el programa cae)
#	la solucion es hacer una captura o control de excepcion:
#		intenta realizar esta instruccion y en caso de que no se puede seguir con los demas instrucciones

#dividiendo un numero netre cero:
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2
####quie es donde puede aver error, asi que usamos try
def divide(num1,num2):		
	try:		
		return num1/num2 	#sino puede dividir y si coincide el error con el error que mencionamos 
							#		se ejecutara el except
	except ZeroDivisionError:		#si no se genera el error que se especifica el programa caera
		print("no se puede dividir entre 0")
		return "operacion erronea"

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
peracion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")
#primero denbemos ver el mensaje error,"pila de llamadas", y debemos ir donde se ocaciona el error
#	debemos fijarnos el normbre del tipo de error, eneste caso fue "Zerodivisioncero"
#	la funcion que es suseptible para cometer un error la tenemos que meter en un bloque try
if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica"
	print(multiplica(op1,op2))#
#el error erra de la division por zero
elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")

#SEGUNDA PARTE:
#usando las mismas instrucciones del video anterior
#veamos como tomas en cuenta el error cuando se introduce letras en ves de numeros 
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	return num1/num2
################	
try :
	op1=(int(input("Introduce el primer número: ")))
	op2=(int(input("Introduce el segundo número: ")))		
except ValueError:
	print("los valores introducidos no son correctos")
#el programa no cae pero no funcionara correctamente ya que se ejecuta el comando que sigue
#analisar las instrucciones para ver el error
#el error es cunando llega a if
#para ello cambiamos el try
while True:		#es un bucle infinito
	try:
		op1=(int(input("Introduce el primer número: ")))
	 	op2=(int(input("Introduce el segundo número: "))) #si todo va biense ejecuta break(sale de while)
	 	break
	 except ValueError:
	 	print("los valores introducidos son errores")
#aora todo esat bacan Xd

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")
if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplica":
	print(multiplica(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))
else:
	print ("Operación no contemplada")
print("Operación ejecutada. Continuación de ejecúción del programa ")

#agamos otro ejemplo para ver el uso de exception
#el bloeuq en generar puede tenre varios errores
#para ello metemos todo en un bloque

def divide():
	try:
		op1=(float(input("introduce el primer numero: ")))
		op2=(float(input("introduce el segundo numero")))
		print("la division es: "+ str(op1/op2))
	#dependiendo del error entra al tipo de except que tiene dicho error
	except ValueError:
		print("el valor introducido es erroneo")
	#aqui  viene la novedad
	except ZeroDivisionError:
		prin("no se puede dvir entre sero")
		#se puede poner mas exceoriones

	print("calcuoo finalizado")
divide()


###en ves de ponder varios excep podemos aser un expcet unico 
#	per es poco recomendable, pues no se sabe que tipo de eroor se cometio
	except :	#agarre todo tipo de error
		print("a ocurrido un error")

#cuando quieres que un codigo se ejecute siempre existe la laternativa de introducir
#	ese codigo en un finally
	#...
	finally:
		print("calculo finalisado")	#se ejecuta si o si

#tambien se puede usar try sin except pero usando finally, en este caso
#	intenta aser try y no se captura ningun error si hay, pero el programa no cae
#	y se ejecuta finally, no se puede presindir en esta caso del finally			
# osea: sale el error pero el programa sigue , se ejecuta finally

#PARTE TRES DEL VIDEO
#aora lazaremos exceptiones: seamos quieres proboquemos una exception
#	para ello se usa Raise(es la base que mas adelante usaremos para crear nuestars exceptiones propias)
#creamos un programas que evalue nuestra edad:
def evaluaEdad(edad):
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "cuidate..."
#si ponemos un nuemro negativo no ocasiona un error		  
print(evaluaEdad(-15))
#para ello podemos lanzar una exception



def evaluaEdad(edad):
	if edad<20:
		raise TypeError("no se permiten edades negativas")	 #se puede acompañar un mensaje
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "cuidate..."

print(evaluaEdad(-15))


#las intrsucciones posterios no se ejecutarian

#creamos un programa para que alle raises cuadradas


import math
def calcularaiz(num1):
	if num1<0:
		raise ValueError("el numero no puede ser cero")
	else:
		return math.sqrt(num1)

op1=(int(input("introduce el numero: ")))
	print(calcularaiz(op1))		
print("programa terminado")

#captuando el error

import math
def calcularaiz(num1):
	if num1<0:
		raise ValueError("el numero no puede ser cero")
	else:
		return math.sqrt(num1)

op1=(int(input("introduce el numero: ")))
#capturando el error
try:
	print(calcularaiz(op1))		#este asia salta la eception
except ValueError as Errordenumeronegativo:	#dando un alias a nuestro error
	print(Errordenumeronegativo)
#no se imprime el siguiente  comando si hay error
#una ves capturando el error se puede imprimer el siquiente comando 
#	y el programa sigue
print("programa terminado")











