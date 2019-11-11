#importando librerias
import matplotlib.pyplot as plt
import numpy as np

#definiendo las sucesiones de funciones
def f(x,n,i):
    if i==2 :
        y=n/np.sqrt(np.pi) * np.exp(-n**2 * x**2) #sucesion ii)
    elif i==3 :
        y=n/(np.pi*(1+n**2*x**2))                   #sucesion iii)
    elif i==4 :
        y=np.sin(n*x)/(np.pi*x)                #sucesion iv)
    return y

def g(x,n):
    y=abs(x/x)*n            #susecion i)
    return y

#GRAFICANDO LASUCESION i)
plt.figure(figsize=(20,5))
plt.xlim(-2,2)
plt.ylim(-1,12)

for i in [1,2,3,4,5,6,7,8,9,10]:
    x = np.arange(-1/(2*i),1/(2*i), 0.02)
    plt.plot( x,g(x,i)) 

plt.legend(('n=1','n=2','n=3','n=4','n=5','n=6','n=7','n=8',
            'n=9','n=10'),loc='upper left')
plt.title(r'$y= \frac{1}{n}$')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid()
plt.show()



x = np.arange(-2, 2, 0.02)

#GRAFICANDO LA SUCESION ii)
plt.figure(figsize=(20,5))
plt.ylim(-1,12)
plt.plot(x,f(x,1,2), x,f(x,2,2),  x,f(x,3,2),x,f(x,4,2),  x,f(x,5,2),
         x,f(x,6,2),x,f(x,7,2),  x,f(x,8,2),  x,f(x,9,2), x,f(x,10,2))

plt.legend(('n=1','n=2','n=3','n=4','n=5','n=6','n=7','n=8',
            'n=9','n=10'),loc='upper left')
plt.title(r'$y=\frac{n}{ \sqrt{\pi} } e^{-n^2 x^2}$')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid()

#GRAFICANDO LA SUCESION iii)
plt.figure(figsize=(20,5))
plt.ylim(-1,12)
plt.plot(x,f(x,1,3), x,f(x,2,3),  x,f(x,3,3),x,f(x,4,3),  x,f(x,5,3),
         x,f(x,6,3),x,f(x,7,3),  x,f(x,8,3),  x,f(x,9,3), x,f(x,10,3))

plt.legend(('n=1','n=2','n=3','n=4','n=5','n=6','n=7','n=8',
            'n=9','n=10'),loc='upper left')
plt.title(r'$y=\frac{n}{\pi (1+n^2 x^2)}$')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid()

#GRACICANDO LA SUCESION iv)
plt.figure(figsize=(20,5))
plt.ylim(-1,12)
plt.plot(x,f(x,1,4), x,f(x,2,4),  x,f(x,3,4),x,f(x,4,4),  x,f(x,5,4),
         x,f(x,6,4),x,f(x,7,4),  x,f(x,8,4),  x,f(x,9,4), x,f(x,10,4))

plt.legend(('n=1','n=2','n=3','n=4','n=5','n=6','n=7','n=8',
            'n=9','n=10'),loc='upper left')
plt.title(r'$y=\frac{ \sin{nx} }{ \pi x }$')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid()


plt.show()    


