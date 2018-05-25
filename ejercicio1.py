# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

a= x[2]-x[1]

d1=(fx[1]-fx[0])/a

d2=(fx[2]-fx[1])/a

d3=(fx[3]-fx[2])/a

d4=(fx[4]-fx[3])/a

d5=(fx[5]-fx[4])/a

d6=(fx[6]-fx[5])/a

d7=(fx[7]-fx[6])/a

d8=(fx[8]-fx[9])/a

segunda=[]

d11=d2-d1/a
segunda.append(d11)

d12=d3-d2/a
segunda.append(d12)

d13=d4-d3/a
segunda.append(d13)

d14=d5-d4/a
segunda.append(d14)

d15=d6-d7/a
segunda.append(d15)

d16=d8-d7/a
segunda.append(d16)

x_n=np.linspace(0.4444,1.5555,6)

plt.plot(x_n, segunda)



