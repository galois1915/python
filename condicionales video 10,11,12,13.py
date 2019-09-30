#PARTE 1(uso del if)
print("programa de evaluacion de notas alumnos")
#se usa el input para introducir datos por teclado
#ir a tools , sublime repel , phithon , run file 
#cualquier cosa que introduccamos datos se considera de tipo texto
#para que sea considerado de tipo entero se usa int
#lo normal es variable=input()
#input puede contener mensajes
#valor=input("mensaje")
nota_alumno=input("introduscamos la nota del alumno: ")


def evaluacion(nota): 
	#la variable solo es aceptado dentro del ambito
	valoracion="aprovado"
	#sintaxis de la condicional if
	if nota<5 :  
		valoracion="suspenso"
	return valoracion
#cualquier cosa que introduscamos con input sera considerado como texto strs
#aqui  se usa el int para convertir un valor en tipo entero int(valor)
print(evaluacion(int(nota_alumno)))

#PARTE 2(uso del else)
print("verificaion de acseso")
#preguntado al usuario
edad_usuario=int(input("introduce tu edad por favor: "))
if edad_usuario < 18 :
 	print("no puedes pasar")
 	#puede ir un if sin su else
 	#pero siempre el else va siempre con un if
 	#si  no se cumple el if entonses se ejecuta lo que esta en el else
 	#si se cumple el if , no se ejecuta el else
else :
	print("puedes pasar")

print("el programa a finalisado")
#puede vaver mas else con el mismo if

#CONTRACCION CON EL ELSE
#las instrucciones a continuacion se ejecuta pero tiene contradicciones 
#el motivo es que el else se va acompañado con el if mas cercano
#sin saber nada de los demas if , asi que puede aver eerrores
print("verificaion de acseso")
#prueba con 15 para ver el detalle
edad_usuario=int(input("introduce tu edad por favor: "))
if edad_usuario < 18 :
 	print("no puedes pasar")
if edad_usuario>100:
	print("edad incorrecta")
#este else va a trabajar con el ultimo if
else :
	print("puedes pasar")
print("el programa a finalisado")

#USO DEL ELIF
#para eso se usa "elif"(fucionan igual que el if)
print("verificaion de acseso")
edad_usuario=int(input("introduce tu edad por favor: "))
if edad_usuario < 18 :
 	print("no puedes pasar")
#se ejecuta  si no se cumple el if alterior	
elif edad_usuario>100:
	print("edad incorrecta")
#se acompaña de los dos anterirores
#se ejecuta cuando no se ha cumplido nada de 
#	lo anterior, el if y el elif
else :
	print("puedes pasar")
print("el programa a finalisado")

#mas usos del elif
print("verificacon de acceso")
nota_alumno2=int(input("intrusca su notas, por favor"))
if nota_alumno2<5:	#solo el primero de nustra estructura se pone if
	print("insuficiente")
elif nota_alumno2<6:
	print("suficiente")
elif nota_alumno2<7:
	print("bien")
elif nota_alumno2<9:
	print("notable")
else :
	print("sobresaliente")
# el else  solo se ejecuta si no se cumplen todos los if anteriores



#PARTE 3
#USPO DE OPERADORES DE COMPARCION Y OPERADORES LOGICOS
#en paiyhon no existe switch
#paithon usa concatenacion de opeadores de comparación
#operadores logicos: and or , y el operador in
#para ejecuatr con consola ede forma directa usar: "ctrl + alt +b" 
#	y par cerrara "ctrl +w"
edad=7
#concacetacion de operadores de comparacion :0<edad<100
#lee la concatenacion de opearciones de izquierda a derecha
#se puede usar mas operadores mas operadores de comparacion
if 0<edad<100:
	print("edad es correcta")
else:
	print("edad es incorreta")

#veamos OTRO EJEMPLO
salario_presindente=int(input("introduce salario del presidente: "))
#phyton es fuertemente tipado
# str convierte lo que esta entre parentesis en un strin "" 
print("salario presidente :" + str(salario_presindente) )

salario_director=int(input("introduce salario del directo: "))
print("salario presidente :" + str(salario_director) )

salario_jefe_area=int(input("introduce salario del jefe de area: "))
print("salario presidente :" + str(salario_jefe_area) )

salario_administrativo=int(input("introduce salario del administrador: "))
print("salario presidente :" + str(salario_administrativo) )

#usando operdadores de comparacion
#se deben de cumplir todos las comparciones para que no se cumpla el else
#si no se cumple almenos uno en e if , se ejecutara el else
if salario_administrativo<salario_jefe_area<salario_director<salario_presindente:
	print("todo funcina correctamente")
else:
	print("algo anda mal en esta empresa")

#USO DE LOS OPERADORES ""AND Y "OR"
print("prgrama de becs años 2017")
distanacia_escuela=int(input("introduce la distancia hacia la escuela en km: ") )
print(distanacia_escuela)

numero_hermanos=int(input("introdusca el numero de ermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("introduce salario anual bruto: "))
print(salario_familiar)

#se tiene que cumplir las tres condiciones para que no se cumpla el else
#si no se cumple almenos una condicion  de 
#	comparacion del if , se ejecutara el else
if distanacia_escuela>40 and numero_hermanos>2 and salario_familiar<=2000:
	print("tiene derecho beca")
else:
	print("no tienes derecho a beca")

#asiendo el otorgamiento de la beca mas razonable
#se debe cumplir (..and..) o el (...<...) para que se ejecute el if
#si no se cumple (...and...) y el (...<..) se ejecutara el else
if distanacia_escuela>40 and numero_hermanos>2 or salario_familiar<=2000:
	#l pareser no hay limites del uso de and y or
	print("tiene derecho beca")
else:
	print("no tienes derecho a beca")
#no se conose limite los usos de los and , or , (podemos concatenar cualquier cantidad de tales operadores)

#USO DEL OPERADOR IN:
#veamos otro ejemplo
print("asignaturas optativas del año 2017")
print("asigaturas optativas: informatica gráfica - pruebas de software - usabilidad y accesibilidad")
#no se usa el int() ya que la informacion es de tipo estrin(texto)
#asignatura=input("escribela asigantura escogida")
opcion=input("escribe la asignatura escogida: ")
#phyton es case sensititive: distigue entre mayusculas y minsculas 
asignatura=opcion.lower()	#como uso lower() convierto todo en minusculos
#upper() transforma todo en mayusculas
#puede que intruscamos ej:PruEBA de softWare
#asi que usamos lower que ase que convierte todo el texto en minusculas
#asi que todo lo evalua en minusculas
#lo que ase el in es comparar lo que va en la variable con cada uni de los valores	entre ()
if asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
	#lo de strin va entre comilla, si fueran valores de variables con varios 
	#	valores numericos no van entrecomilados
	#no se usa srt porque el valor en asignado es de tipo strin
	print("asinatura elegida: "+ asignatura)
else:
	print("la asignatura escogida no esta contemplada")
#fin del dodigo
