# importar todas las funciones de pylab
#from pylab import *             para trabajar interacivamente

# importar el módulo pyplot
#import matplotlib.pyplot as p      cuando se usan programas

####################################

from pylab import *      # importar todas las funciones de pylab
x = arange(10.)          # array de floats, de 0.0 a 9.0
plot(x)                  # generar el gráfico de la función y=x
show()                   # mostrar el gráfico en pantalla

###################################

#veamos como aser una variable sea una instancia de la grafica
#tener en cuenta que 
#a = [3, 5]
# Así ``a`` es una lista, que contiene dos valores
#a, b = [3, 5]
# Así desempaquetamos los elementos de la lista y a=3 y b=5
# Esto funciona porque pusimos tantas variables como elementos en la lista
#Pero si la lista sólo tiene un elemento ¿cómo desempaquetamos ese elemento?. Veamos:
#a = [3]  # Así, ``a`` es una lista y no el número 3
#a, = [3] # Si añadimos una coma indicamos que queremos meter ese único
         # elemento en una variable, en lugar de usar la lista

#mi_dibujo, = plot(x)

########################

#editando la grafica
#colores
plot(x,'b')
plot(2*x,'g')
plot(3*x,'r')
plot(4*x,'c')
plot(5*x,'m')
plot(6*x,'y')
plot(7*x,'k')
plot(8*x,'w')
show()
#clf()   # Limpiamos toda la figura

######################################

#figuras
plot(x,'b-')
plot(2*x,'g-.')
plot(3*x,'r:')
plot(4*x,'c.')
plot(5*x,'m,')
plot(6*x,'yo')
plot(7*x,'k<')
plot(8*x,'w>')
show()
#cla() no se pa que sirve

#####################################

#varios graficos en una misma ventana
x2=x**2   # definimos el array x2
x3=x**3    # definimos el array x3
# dibujamos tres curvas en el mismo gráfico y figura
plot(x, x,'b.', x, x2,'rd', x, x3,'g^')
xlim(-11,11)     # nuevos límites para el eje OX
ylim(-50,50)
show()

#################################

#cambiando las propiedades una ves creadas
# Hago tres dibujos, capturando sus instancias
# en las variables p1, p2 y p3
p1, p2, p3 = plot(x, x,'b.',x, x2, 'rd', x, x3, 'g^')
show()
p1.set_marker('o')     # Cambio el símbolo de la gráfica 1
p3.set_color('y')      # Cambio el color de la gráfica 3
draw()                 # Hacer los cambios

###########################
print("asdfghj")
#insertano teto en la grafica
x = arange(0, 5, 0.05) #inicio, final , paso
p, = plot(x,log10(x)*sin(x**2))

xlabel('Eje X')        # Etiqueta del eje OX
ylabel('Eje Y')        # Etiqueta del eje OY
title('Mi grafica')    # Título del gráfico
text(1, -0.4, 'Nota')  # Texto en coodenadas (1, -0.4)
show()

#tambien podemos aser formulas en formato latex
t = arange(0.1, 20, 0.1)
y1 = sin(t)/t
y2 = sin(t)*exp(-t)
p1, p2 = plot(t, y1, t, y2,)

# Texto en la gráfica en coordenadas (x,y)
texto1 = text(2, 0.6, r'$\frac{\sin(x)}{x}$', fontsize=20)
texto2 = text(13, 0.2, r'$\sin(x) \cdot e^{-x}$', fontsize=16)

# Añado una malla al gráfico
grid()

title('Representacion de dos funciones')
xlabel('Tiempo / s')
ylabel('Amplitud / cm')

show()
#señalando partes de la grafica

# Punto a señalar en la primera gráfica
#px = 7.5
#py = sin(py)/py

# Pinto las coordenadas con un punto negro
#punto = plot([px], [py], 'bo')

# Hago un señalización con flecha
#nota = plt.annotate(r'$\frac{\sin(7.5)}{\exp(-7.5)} = 0.12$',
#         xy=(px, py), xycoords='data',
#         xytext=(3, 0.4), fontsize=9,
#        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#no me sale bien esta cosa

###################################333

#represenenatcion grafica de funciones
def f1(x):
    y = sin(x)
    return y

def f2(x):
    y = sin(x)+sin(5.0*x)
    return y


def f3(x):
    y = sin(x)*exp(-x/10.)
    return y

# array de valores que quiero representar
x = linspace(0, 10*pi, 800)

p1, p2, p3 = plot(x, f1(x), x, f2(x), x, f3(x))

# Añado leyenda, tamaño de letra 10, en esquina superior derecha
legend(('Funcion 1', 'Funcion 2', 'Funcion 3'),
prop = {'size':10}, loc = 'upper right')

xlabel('Tiempo / s')
ylabel('Amplitud / cm')
title('Representacion de tres funciones')

# Creo una figura (ventana), pero indico el tamaño (x,y) en pulgadas
figure(figsize=(20, 5))

show()

# Plots con label
p1 = plot(x, f1(x), label='Funcion 1')
p2 = plot(x, f2(x), label='Funcion 2')
p3 = plot(x, f3(x), label='Funcion 3')

# Ahora se puede usar legend sin etiqueta, pero indico
# dónde quiero que se coloque
legend(loc='lower right')

show()

############3

#varias ventanas de graficos
p1, = plot(sin(x))       # Crea una figura en una ventana (Figure 1),automaticament es fig 1

figure(2)                # Crea una nueva figura vacía en otra ventana (Figure 2)
p2, = plot(cos(x))       # Dibuja el gráfico en la figura 2
title('Funcion coseno')  # Añade un título a la figura 2

figure(1)                # Activo la figura 1
title('Funcion seno')    # Añade un título a la figura 2
show()

##########################

#varios graficos en una misma figura

# Figura con una fila y tres columnas, activo primer subgráfico
subplot(131)
p1, = plot(x,f1(x),'r-')
# Etiqueta del eje Y, que es común para todas
ylabel('Amplitud / cm')
title('Funcion 1')

# Figura con una fila y tres columnas, activo segundo subgráfico
subplot(132)
p2, = plot(x,f2(x),'b-')
# Etiqueta del eje X, que es común para todas
xlabel('Tiempo / s')
title('Funcion 2')

# Figura con una fila y tres columnas, activo tercer subgráfico
subplot(133)
p3, = plot(x, f3(x),'g-')
title('Funcion 3')

#Al igual que con varias figuras, para dibujar en un gráfico hay que activarlo.
# De esta forma, si acabamos de dibujar el segundo gráfico escribiendo antes 
#subplot(132) y queremos cambiar algo del primero, debemos activarlo con subplot(131) 
#y en ese momento todas funciones de gráficas que hagamos se aplicarán a él.


##################

#guardando graficos
#Después de crear una figura con cualquiera de los procedimientos descritos hasta ahora 
#podemos guardarla con la función savefig() poniendo como parámetro el nombre del fichero 
#con su extensión. El formato de grabado se toma automáticamente de la extensión del nombre.
#Los formatos disponibles en Python son los más usuales: png, pdf, ps, eps y svg.

savefig("p3.eps")           # Guardo la figura en formato eps
savefig("p3.png", dpi=300)  # Guardo la figura en formato png a 300 DPI

savefig("p3.pdf") 

#Si el gráfico se va usar para imprimir, por ejemplo en una publicación científica o 
#en un informe, es recomendable usar un formato vectorial como Postscript (ps) o Postscript 
#encapsulado (eps), pero si es para mostrar por pantalla o en una web, el más adecuado es
#un formato de mapa de bits como png o jpg.


























