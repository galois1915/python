import matplotlib.pyplot as plt
import numpy as np

lista=[1,2,3,4,5,6,7,8,9,10]
x=[1,2,3,4,5,6,7,8,9,10]

for i in lista :
    x[i-1]=2*np.sin(1/(2*i))*i
    print(x[i-1])

plt.plot(lista,x,'bo')
plt.title(r'$ y= 2n \sin{\frac{2}{2n}}  $')
plt.xlabel('eje n')
plt.ylabel('eje y')
plt.grid()
plt.show()

for i in lista :
    x[i-1]=np.exp(-1/(4*i^2))
    print(x[i-1])

plt.plot(lista,x,'bo')
plt.title(r'$y=e^{ \frac{-1}{4 n^2} }$')
plt.xlabel('eje n')
plt.ylabel('eje y')
plt.grid()
plt.show()

for i in lista :
    x[i-1]=np.exp(-1/i)
    print(x[i-1])

plt.plot(lista,x,'bo')
plt.title(r'$y=e^{ \frac{-1}{n}}$')
plt.xlabel('eje n')
plt.ylabel('eje y')
plt.grid()
plt.show()

for i in lista :
    x[i-1]=1
    print(x[i-1])

plt.plot(lista,x,'bo')
plt.title(r'$y=1$')
plt.xlabel('eje n')
plt.ylabel('eje y')
plt.grid()
plt.show()
