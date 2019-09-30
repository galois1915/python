#vamos usar listas
#las listas de datos que nos permite almacenar gran canridad de 
#	datos equivalenete arrayen otros lenguajes de programacion
#en phyton las listas pueden guardar diferenct e tipos de valores
#	(en otros lenguajes no ocurre esto)

#SINTAXIS Y IMPRESION DE UNA LISTA
#sintaxis e lista :  nombre_lista=[elem1,elem2,elem3,....]
#observaicon : elem1 esta en la posicion cero [0=indíce]
miLista=["Maria", "Pepe", "Marta", "Antonio"] #los textos deben 
#	ir entrecomillados 
#impresion compreta de la lista
print(miLista[:])
#impresion de un elemento en concreto
#se usa el indice
print(miLista[2])  #sale Marta 
print(miLista[-2]) #empiesa desde el final(desde menos uno) , sale marta
#porcion de lista
print(miLista[0:3]) #inclulle el sero ,uno,dos ; asta el ai nomas
print(miLista[:3]) #es lo mismo que de antes
print(miLista[1:3]) #sale: el uno,dos, asta ai nomas
print(miLista[2:]) #imprime desde el dos asta el final

#AGREGANDO ELEMENTOS A MI LISTA
miLista.append("sandra") #agrega elementos al final de nuedtra lista
print(miLista[:])
miLista.insert(2,"lucas") #agrega ´"lucas" en la posicion dos y los demas se corren
print(miLista[:])
miLista.extend(["paco", "angel"]) #agrega mas elementos a mi lista pero al final de dicha lista
print(miLista[:])

#PREGUNTANDO EL INDICE DE UN ELEMENTO 
#preguntar el índice de un elemento de dicha lista
print(miLista.index("angel"))
#se puede repetir los elementos de la lista pero con el comando index solo 
#	mostrara el del primer elemento

#PREGUNTAR SI UN ELEMNTO SE ENCUENTRA EN MI LISTA
#comprobar si un elemento esta en  mi lista
print("angel" in miLista) # si arroja true quiere desir que si esta en la lista
print("pepepep" in miLista) #devuelve false

#USANDO OTROS TIPO DE ELEMENTOS EN MI LISTA
#usando otros tipos e elementos
miLista1=["manuel",5, True ,78.35] #tiene tiene texto , enteros , boleano , decimales , todo sigue funcionando esactamente igual
print(miLista1[3])

#ELIMINANDO ELEMENTOS DE  MI LISTA 
miLista.remove("angel")	#se elimina angel de la lista
print(miLista[:])
#eliminacion de ultimo elemnto de la lista
miLista.pop()
print(miLista[:])

#UNION DE LISTAS
miLista2 = miLista1 + miLista
print(miLista2[:])

#MUTIPLICANDO LISTAS
miLista4=["miguel","juancho"] *3 #triplica la lista
print(miLista4[:])


##TUPLAS

#son lista inmutables de depues de su modificacion
#en las tuplas no se permite añadir , elimar , mover 
#si permite extraer porciones de la tupla; no se modifica la tupla inicial
#si se  permiten index(busqueda), pero si permite comprabar si hay un elemento
#si se extrae un aporcion no modifica ala tupla original , ademas la extraciion es un tupla
#es mas rapido(ejecuión) que un lista ,menos espacio que una lista
#sintaxis::  nombretupla=(elem1,elem2,elem3,....)  	 obs, se ponen en parentesis
mitupla=("angel",13,1,1995)		#se pueden omitir los parentesis
print(mitupla[0])

#PASAR DE UNA LISTA A UNA TUPLA
#crear lista a vase de una tupla
milista=list(mitupla)
print(milista)	#sale en corchetes
print(mitupla)	#sale en parentesis
#observar la diferencia entre parentesis y corchetes
#pasar de una lista a una tupla
milista1=["miguel",2,4]
mitupla1=tuple(milista1)
print(mitupla1)		#sale en aprentesis
print(milista1)		#sale en corchetes

#BUSCANDO UN ELEMNTO EN LA TUPLA
#saber si un elemnto esta en mi tupla
mitupla2=("luis",12,"juan","juan")
print("luis" in mitupla2)	#sale true si esta y false si no

#COTEO EN UN ELEMENTO
#cuantos veses esta un elemento en la tupla
print(mitupla2.count(12))
print(mitupla2.count("juan"))

#LONGITUD DE UNA TUPLA
#numer de elementos en la tupla
print(len(mitupla2))	#imprime 4

#TUPLA UNITARIA
mitupla3=("lucas",) #es necesario la coma para que sea una tupla unitaria
print(len(mitupla3))

#los parentesis se pueden omitir
#sin embargo a veces produce confución
#se denominan "empaquetado de tupla" lo que emos venido asiendo

#desempaquetado de tuplas
nombre,dia,mes,agno=mitupla2		#asigna alas variables los elementos de mi tupla 
print(nombre)
print(dia)
print(mes)
print(agno) 
#si usas index(busqueda) pueda que corra , es debido alas nuevas versiones

#DICCIONARIOS
#son estructturas de datos que nos permiten almacenar valors de diferente tipo
#enteros, cadenas de texto, decimales,,, e incluso listas y otros diccionarios
#la principal caracteristica de los diccionarios es que los datos se almacenan 
#asociados a una clave d tal forma que se crea una asociacion 
# de tipo "clave :valor " para cada elemento almacenado
#los elementos amacenados no estan ordenados .El orden es indifirente ala
#hora d almacenar informacion en un diccionario

#SINTAXIS E IMPRESION DE UN DICCIONARIO
#   "clave":"valor"
#tambiene puede tener elemntos enteros , decimales , etc
midiccionario={"alemania":"berlin","francia":"paris","reino unido":"londres","españa":"madrid"}	#fijate en las llaves
print(midiccionario)
print(midiccionario["francia"]) 
print(midiccionario["españa"])

#AGREGAR UN ELEMENTO A MI DICCIONARIO
#agregando elemento
midiccionario["italia"]="lisboa"
print(midiccionario)
#se puede corregir(modificar) el diccionario
midiccionario["italia"]="roma"	
#en el diccionario no puede aver dos claves iguales
print(midiccionario)#solo se reescribe

#ELIMINANDO ELEMENTOS DE MI DICCIONARIO
del midiccionario["reino unido"]
print(midiccionario)

#USANDO UNA TUPLA PARA ASIGAR LAS CLAVES A LOS DICCIONARIOS 
mitupla=["españa","francia","reino unido","alemania"]
midiccionario2={mitupla[0]:"madrid",mitupla[1]:"paris",mitupla[2]:"londres",mitupla[3]:"berlin"}
print(midiccionario2)
print(midiccionario2["francia"])		#o mitupla[1]

#TUPLAEN UN DICCIONARIO
midiccionario3={23:"jordan","nombre":"michael","equipo":"chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario3)
print(midiccionario3["equipo"])
print(midiccionario3["anillos"])

#DICCIONARIO EN OTRO DICCIONARIO
midiccionario4={23:"jordan","nombre":"michael","equipo":"chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario4)
print(midiccionario4["anillos"])

#como obtener las claves de un diccionario
print(midiccionario4.keys())
#como obtener las valores de un diccionario
print(midiccionario4.values())
#la longitud del diccionario(clave_valor)
print(len(midiccionario4))