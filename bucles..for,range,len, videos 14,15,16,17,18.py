#la uti.idad del bucle es para repetir codigo
#hay dos tipos de bucles LOS DETERMINADOS Y LOS INDETERMINADOS

#BUCLES DETERMINADOS (FOR)
#se ejecutan un numerod determinado de veces
#e sabe a priori cuantas veces se va a  ejecutar el codigo del interior del bucle
#sintaxi (for "variable" in "elemnto a recorrer" :)
#ejemplo usando una tupla
for i in [1,2,3]:
	#puede ser una tupla , una cadena de txto , etc
    #cuerpo del bucle 
    #el elmento a recorrero esta formada por tres elementos, asi que imprimira tres veses el bucle  
	print("hola")
#vemaos como seria si tenemos texto como elemento a recorrer
for variable in ["primavera","verano","otono","invierno"] :
	#corroboremos como varia la "variable"
	print(variable)


#PARTE DOS (for: recorriendo string, tipo range, notaciones especiales con print)
for i in ["pildoras","informaticas", 3]:
	#la funcion end ase que el print imprima todo en una sola linea
	#el espacio entre comillas da el espacio entr palabras que va imprimir el print
	print("hola",end="")

#usando strin
for i in "angel tomas chaico":
	print("chau")

#otro ejemplo:veamos si un correo esta bien escrito
email=False
for i in "angel_98tcc@hotmail.com":
	if(i=="@"):
		email=True
#se puede suprimir el ==True , si lo sacamos el programa supondra que la variable es true
if email==True:	#obs::   if email==True: es igual en phyton a if email:
	print("el email es correcto")
else:
	print("el email es incorrecto")
#fin de ejemplo


#podemos tambien introducir un correo con la funcion input 
email=False
miemail=input("introdusca su email:  ")	#
for i in miemail:
	if(i=="@"):
		email=True
#se puede suprimir el ==True , si lo sacamos el programa supondra que la variable es true
if email==True:
	print("el email es correcto")
else:
	print("el email es incorrecto")

#siendo mas quisquillosos
contador=0
miemail=input("introdusca su email:  ")
 
for i in "angel_98tcc@hotmail.com":
	if(i=="@" or i=="."):
		contador=contador+1
#se puede suprimir el ==True , si lo sacamos el programa supondra que la variable es true
if contador==2:
	print("el email es correcto")
else:
	print("el email es incorrecto")

#USO DEL RANGE
for i in range(5):
	print("bateria")
	#imprime "bateria" cinco veses comensando con 0
for i in range(5):
	print(i)

#TERCERA PHYTON(uso de range)
#hay una maner de concatenar una variable con un texto
#para eso usamos "f" antes del texto que vamos a imprimir .., ejemplo
for i in range(6):
	print(f"valor de la variable: {i}")

#necesariamento no comiensa desde cero
for i in range(5,10):
	print(f"bateria {i} ")
	#osea va desde 5 asta el 9

#admite tambien un tercer argumento
for i in range(5,50,3):
	#aora va desde 5 asta el 50 pero va de tres en tres
	print(f"causa {i}")

#USO DE LA FUNCION "LEN"
#devuelve lalongitud de un strin(numero de caracteres)
valido=False
email=input("introduce tu email:  ")
for i in range(len(email)):

	if email[i]=="@":
		valido=True
if valido:
	print("el email es correcto")
else:
	print("email incorrecto")
	


#CUARTA PARTE
#uso del bucle while
#sintaxis:   while  condicion:
#					cuerpo del bucle
#mientras se sigua cumpliendo la condicion se va estar ejecutando el cuerpo del bucle
#el bucle es "indeterminado", puede que se jecute indefinidamente
i = 1
while i<=10:
	print("ejecucion " + str(i))
	i=i+1  #este es un contador
print("termino la ejecucion")

#probemos otro ejemplo:
edad = int(input("introduce tu edad por favor:  "))
while edad<0 or edad>100 :
	print("has introducido una  edad negativa , vuelve a intentarlo imbecíl")
	edad = int(input("introduce tu edad por favor:  "))

print("gracias por colaborar tarado, puedes pasar")
print("edad del aspirante  " + str(edad))


#hallemos la raiz cuadrada
import math
#import es un concepto que se aclarara mas adelante por 
#	aora es importante para usar sqrt
print("programa de calculo de raiz cuadrada")
numero = int(input("introdice un numero porfavor : "))
intentos=0
while numero<0:
	print("no se puede hallar la raiz de un nmero negativo")
	if intentos == 2:
		print("as consumido demasiados intentos ,  a finalisado el programa")
		break;	#sale del blucle white
	numero = int(input("introdice un numero porfavor : "))
	if numero<0:
		intentos = intentos +1
if intentos<2:
	solucion=math.sqrt(numero)
	print("la raiz cuadrada de "+ str(numero)+" es: "+str(solución))

#USEMOS  LAS INSTRUCCIONES CONTINUE, PASS, ELSE
#ignora un bucle
#pass ase queun bucle devuelve null en un bucle
#else es igual al de un condicional
for letra in "python":
	if letra=="h":
		continue   	#ingora los demas comandos , y vuelve al siquiente bucle
	print("viendo la letra : "+ letra)

#cpnttemos letras
nombre="pildora informaticas"
contador=0
#al espacio en blanco se considera como caracter
print(len(nombre))
#imprime 21
#aora usemos continue
for i in nombre:
	if 1==" ":
		continue
	contador+=1
print(contador)

#uso de la instruccion pass
#este seria infinito
#para salir del bucle infinito seri ctr + c
while True:
	pass 	#mantener el programa ocupado asta que el usuario salga del 
			#	delprogrma usando ctr+c
# hay mas casos pero notantos XD

#uso del else
#se puede ignorar
email=input("introduce tu email")
for i in email:
	if i=="@":
		arroba=True
		break;	#sale del for
else:		#forma parte del for
	#el else se ejecuta solo cuando el for se queda vacio osea que ya no tenga nada por recorre
	#si se ejecuta el break antes de que termine el for , el else no se ejecuta
	#observar que forma parte de for , no del if
	arroba=False
print(arroba)
