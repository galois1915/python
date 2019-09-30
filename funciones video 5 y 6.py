
#asegurarse que se esata trabajando el el lenguaje de paiton vinedo 
#	tools y luego build system
#	una ves    guardado se empiesa a colorear las letras 
# no olvidar la extencion .py
print("estamos aprendiendo python1")
#  para ejecutar se usa ctr + b

#declaracion de una funcion
#  sintaxis para definir una funcion
#def nombre_de_la_funcion():
def mensaje():	 
	#cuerpo de una funcion
	#sublime lo indenta automaticamente
	print("estamos aprediendo phyton")
	#lo que va en () lo veremos luego
	print("estamos aprendiendo python")
	#dos enter parasalir de la funcion

#llamando a la funcion para poder ejecutar el mensaje
mensaje()

#se puede llamar varias vese la funcion
print("ejecutando fuera de funcion")

mensaje()
#recordar como esque se lee el programa
#ctr + s para guradar una ves ya fijado la carpeta de destino 
# y luego se puede ejecutar el programa


#CONTINUACION VIDEO 6

#aremos una funcion que sume
print("uso del suma")
def suma():				#sin parametro por aora
	#no olvidar los dos puntos
	#declaracion de variables
	num1=5
	num2=7
	print(num1+num2)	
#salimos de la funcion dos enter
#llamamos la funcion
suma()
#ejecutar para ver los resultados ctr+s y luego ctr+b
#queremos que la misma funcion sume diferentes valores en cada llamada
#usamos lo llamado pametros o argumentos
#dentro de las parentesis van los parametros o argumento
print("uso de suma1")
def suma1(num11,num12):		#creamos una funciones que va a 
	#	recibir dos argumentos, van separados por comas
	#en las parentesis ya declaramos las variable num11 y num12
	print(num11+num12)
 	
#en las llamamos a las funciones tenemos que darles los numeros que van a sumar
suma1(4,5)
#obs :los parametros se guardan en orden num11=4 num12=5
suma1(356,635)
#los parametros pueden ser float , str , o mixto
#una funcion puede devolver un valor para ello usamos return

print("uso de suma2")
#usemos el return
def suma2(nu1,nu2):
	resultado=nu1+nu2
	#uso del return
	return resultado
#obs : phyton pasa los valores por referencia
#usamos la instruccion print para visualizar el resultado
print(suma2(34,5))
 #viendola de otra manera
almacena_resultado=suma2(34,3)
#almacena_resultado = resultado
print(almacena_resultado)
