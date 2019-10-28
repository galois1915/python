import matplotlib.pyplot as plt

#Calcule y dibuje el histograma de x .
#El valor de retorno es una tupla ( n , bins , parches ) o 
#([ n0 , n1 , ...], bins , [ patches0 , patches1 , ...]) si la entrada contiene
# datos múltiples.

#Un bin es el intervalo que representa el ancho de una barra del histograma a lo largo del eje X. 
#También puede llamar a esto el intervalo. (Wikipedia define formalmente como «discontinuo categorías».)

#Hay 3 bandejas, para los valores van de 0 a 1 (sin 1.), De 1 a 2 (excl. 2) 
#y de 2 a 3 (incl. 3), respectivamente.

#Los valores de entrada son 1, 2 y 1. Por lo tanto, bin «1 a 2» contiene dos ocurrencias 
#(los dos 1 valores), y bin «2 3» contiene una aparición (la 2). Estos resultados están en el
#primer elemento de la devuelve tupla: array([0, 2, 1]).

plt.hist([1, 2, 1], bins=[0, 1, 2, 3])
#(array([0, 2, 1]), array([0, 1, 2, 3]), <a list of 3 Patch objects>)
plt.show()

import numpy as np

hist, bin_edges = np.histogram([1, 1, 2, 2, 2, 2, 3], bins = range(5))
print(hist)     #A continuación, hist indica que hay 0 artículos en bin #0, 
                    #2 en bin #1, 4 en bin #3, 1 en bin #4.
print (bin_edges)       #bin_edges indica que bin #0 es el intervalo [0,1), 
                            #bin #1 es [1,2), …,bin #3 es [3,4).

plt.show()

print('otrafigura')
print(bin_edges[:-1])
plt.bar(bin_edges[:-1], hist, width = 0.5)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()   

print('otra figura')
arr = np.random.randint(1, 51, 500)
y, x = np.histogram(arr, bins=np.arange(20))
fig, ax = plt.subplots()
ax.plot(x[:-1], y)


fig.show()




















