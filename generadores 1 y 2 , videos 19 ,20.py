#son estructuras que extraen valores de una funcion y se almacenan 
#	en objetos iterables(que se pueden recorrer con for , while , etc)
#estos valores de almacenen de uno en uno
#cada ves que un generador almacena un valor , esta permanece en un 
#estado pausado hasta que se solicite el siquiente .
#esta caracteristica es conocida como "suspension de estado"
#son mas eficietes que las funciones tradicionales
#muy utiles con listas de valores infinitos
#bajos determinados escenarios, sera muy util qe un generador devuelva los valores de uno en uno
#sintaxis:
#un generador lleva un yield aunque tambien puede llevar un return
#def  generadorNumeros():
#      yield  numeros

#usando una clasica funcion
def generadorpares(limite): 
	#lo de que va en () es pqra limitar cuantos numeros pares va generar la funcion
	num=1
	milista=[]	 #creo una lista vacia
	while num<limite:	
		milista.append(num*2)
		num=num+1
	return milista
print(generadorpares(10))

#usando generadores
def generadorpares(limite):
	num=1
	#no tenemos lista
	while num<limite:
		yield num*2		#yield construye un obejto iterable con los valores en su 
		#	interior y que las va almacenando de uno en uno
		num=num+1

devuevepares=generadorpares(10)		#guardo el obejeto iterable en el la nueva variable
for i in devuevepares :
	print(i)		

#asemos que se devuelva el primer elemnto
#aqui se puede ver el uso del generador
print(next(devuevepares))
print("aqui podria ir mas codigos")
print(next(devuevepares))
print("aqui podria ir mas codigos")
print(next(devuevepares))

#PARTE DOS
#usaremos el "yield from"
#
def  devuelve_ciudades(*ciudades):
	#el * indica al program que va recibir un numero indetermiado de elemnot
	#ademas lo va resibir en forma de tuplas
	for elemento in ciudades:
		yield elemento

ciudades_devueltas=devuelve_ciudades("madrid","barcelona","bilboa")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
	
###########################

	for elemento in ciudades:
		for subelemento in elemento:
			yield subelemento

ciudades_devueltas=devuelve_ciudades("madrid","barcelona","bilboa")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

###############################

	for elemento in ciudades:
		for subelemento in elemento:
			yield from elemento
ciudades_devueltas=devuelve_ciudades("madrid","barcelona","bilboa")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
