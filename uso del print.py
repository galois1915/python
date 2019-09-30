print('Python')  # muestra: Python  
luna = 385000  # asigna valor a variable
print('D.M. Tierra-Luna', luna, 'km')  # D.M. Tierra-Luna 385000 km
print('D.M. Tierra-Luna ' + str(luna)+' km')  
# D.M. Tierra-Luna 385000 km

print('\nHola\npythonisos\n')  # muestra cadena en varias líneas
print('Continuará...', end=' ')  # ejecuta varios print() en misma... 
print('otro día')  # ...línea. Muestra: Continuará... otro día
print()  # inserta una línea en blanco

lu = 'Quito (Ecuador)'  # asigna cadena a variable
la = -0.216979  # asigna número flotante a variable
lo = -78.51627  # asigna número flotante a variable

# concatena con formato de intérprete
co =  repr(lu)+': '+repr(la) + ',' + repr(lo)
print(co)  # 'Quito (Ecuador)': -0.216979,-78.51627

alt = 110  # asigna entero
dis = 550  # asigna entero
edi = 'La Giralda'  # asigna cadena
est = 'Antares'  # asigna cadena
print('{} mide {} metros'.format(edi, alt))
# La Giralda mide 110 metros

print('{1} metros: {0}'.format(edi, alt))  # 110 metros: La Giralda
print('{c}:{p}'.format(c='Lima', p='Perú'))  # Lima:Perú

val1 = 8.56767  # asigna flotante
val2 = 9.45548  # asigna flotante

# muestra redondeo con 2 y 3 decimales
print('{0:.3} {1:.4}'.format(val1, val2))

# rellena con guiones bajos
print('{0:_^30}'.format('Sevilla'))

codpais = 34  # asigna número

# rellena con ceros a la izquierda:
print(str(codpais).zfill(4))  # 0034

valor = 2.34565676  # asigna flotante 

# muestra: Valor aproximado
print('Valor aprox. {0:.3f}'.format(valor))  # 2.346

# inserta salto de línea antes de imprimir
print('\nCódigos Postales')

# declara diccionario
correos = {'SJ' : 300, 'LR': 309, 'B': 310}
for loc, cp in correos.items():  # recorre diccionario
    # muestra lista de pares con formato
    print('{0:5}:{1:4d}'.format(loc, cp))

print('\nTabla de Multiplicar')  # muestra tablas de multiplicar
for x in range(1, 11):  # recorre los números del 1 al 10
    print(repr(x)+':')  # imprime el nº de la tabla actual
    for y in range(1, 11):  # recorre los números del 1 al 10
        print(repr(x).ljust(2),'*',end='')  # muestra operadores y ... 
        print(repr(y).rjust(3),end='')  # … resultado en una línea
        print(' =' + repr(x*y).center(5))

# Utilizando comodines: 
# %s (cadena), %i (entero), %f (número con decimales)
#
# Los datos también se pueden tabular reservando un número
# determinado de caracteres:
# Ejemplo: %10s  reserva 10 posiciones y alinea a la izquierda
#          %-10s reserva 10 posiciones y alinea a la derecha

nombre = 'Claudio'
edad = 35
altura = 1.82

print('Tiene %i años' %edad)  # Tiene 35 años
print('%s tiene %i años y mide %f' %(nombre, edad, altura))
# Claudio tiene 35 años y mide 1.820000

# Tabulando datos:

personas = [('Claudio', 35, 1.826),
            ('Elena', 24, 1.84),
            ('Manuel', 9, 1.449),
            ('Isabel', 34, 1.72)]

for persona in personas:
    nombre = persona[0]
    edad = persona[1]
    altura = persona[2]
    print('%-8s tiene %2i años y mide %1.2f' %(nombre, edad, altura))

# Salida:
# Claudio  tiene 35 años y mide 1.83
# Elena    tiene 24 años y mide 1.84
# Manuel   tiene  9 años y mide 1.45
# Isabel   tiene 34 años y mide 1.72
