# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#conceptos generales

#me falta 
 

#introduccion a pyplot
#matplotlib.pyplotes una colección de funciones de estilo de comando que hacen 
#que matplotlib funcione como MATLAB. Cada pyplotfunción realiza algún cambio 
#en una figura: por ejemplo, crea una figura, crea un área de trazado en una 
#figura, traza algunas líneas en un área de trazado, decora el trazado 
#con etiquetas, etc.

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])      #proporcionando una llista o matris a comando plot
                                #X=(0,1,2,3) Y=(1,2,3,4)
plt.ylabel('algunos nnumeros')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])#plt.plot(x,y,´colormodelo´,linewidth=2.0(grosor))


#Formateando el estilo de su trama 
#el predeterminado es el 'b-'
#consultar el paquete plot para mas estilos
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')     
                                    
plt.axis([0, 6, 0, 20])     #[xmin, xmax, ymin, ymax]
plt.show()

#Si matplotlib se limitara a trabajar con listas, sería bastante inútil para el
# procesamiento numérico. En general, utilizará matrices numpy .
import numpy as np

#tiempo de muestreo uniforme a intervalos de 200 ms
t = np.arange(0., 5., 0.2)

#guiones rojos, cuadrados azules y triángulos verdes
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

#Trazado con cadenas de palabras clave(fala inevstiguar)
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 50

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

#Trazado con variables categóricas
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

#control de las dimensiones de los cuadros

#matplotlib.pyplot.figure(num=None, figsize=None(dimensiones del cuadro), dpi=None(resolucion)), 
#facecolor=None(color de fuera de los cuadros), edgecolor=None, frameon=True(si es falso suprime el marco),
# FigureClass=<class 'matplotlib.figure.Figure'>,clear=False, **kwargs)

plt.figure(figsize=(9, 3))

#tipos de graficos
plt.subplot(131)
plt.bar(names, values)

plt.subplot(132)
plt.scatter(names, values)

plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()


#Control de propiedades de línea
x = np.arange(0, 5, 0.05) #inicio, final , paso
p,p1,p2 = plt.plot(x,x**2,x,4*x,x,x**3)    


# use keyword args
plt.setp(p2, color='r', linewidth=2.0)

plt.show()

print('#################')

#Trabajando con múltiples figuras y ejes
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
#The subplot() command specifies numrows, numcols,
# plot_number where plot_number ranges from 1 to numrows*numcols.
# The commas in the subplot command are optional if numrows*numcols<10.
# So subplot(211) is identical to subplot(2, 1, 1).
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()      
print('################')

      
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title
#Puede borrar la figura actual con clf() y la figura con cla()
plt.show()
#Si está haciendo muchas figuras, debe tener en cuenta una cosa más: 
#la memoria requerida para una figura no se libera por completo hasta que 
#la figura se cierra explícitamente close(). Eliminar todas las referencias a 
#la figura, y / o usar el administrador de ventanas para eliminar la ventana 
#en la que aparece la figura en la pantalla, no es suficiente, porque pyplot 
#mantiene referencias internas hasta que close() se llama.
#plt.close( fig = Ninguno )
#Ninguno : la cifra actual
#Figure: la Figureinstancia dada
#int: un número de figura
#str: un nombre de figura
#'all': todas las figuras

print('############')
      
#trabajando con texto
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts', fontsize=14, color='r')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
#trabajando con texto
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

#graficando un histograma
n, bins, patches = plt.hist(x, 10, density=1, facecolor='g', alpha=0.75)

plt.xlabel('my data', fontsize=20, color='red')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')        
#Lo ranterior a la cadena del título es importante: significa que la cadena 
#es una cadena sin procesar y no trata las barras diagonales inversas como 
#escapes de Python. matplotlib tiene un analizador de expresiones TeX incorporado 
#y un motor de diseño, y envía sus propias fuentes matemáticas.
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()

#anotando texto

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=4)

#usando el comando plt.annotate
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='r', shrink=0.005),
             )

plt.ylim(-2, 2)
plt.show()


print('###############')
print('esto ya no se pa que me pueda servir, pero esta porciaca')

#Logarítmicos y otros ejes no lineales 
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
     
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()


plt.close('all')














plt.close('all')


