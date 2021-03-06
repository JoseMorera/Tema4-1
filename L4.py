import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Se definen las variables aleatorias
vaX = stats.norm(0, np.sqrt(15)) 
vaY = stats.norm(0, np.sqrt(15))

# Creación del vector de tiempo para las pruebas
T = 100			
t_final = 10	
t = np.linspace(0, t_final, T)

# Se define el valor de la constante omega
W = np.pi 

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 1000
X_t = np.empty((N, len(t)))

# Creación de las muestras del proceso x(t) (X y Y independientes)
for i in range(N):
	X = vaX.rvs()
	Y = vaY.rvs()
	x_t = X * np.cos(W*t) + Y * np.sin(W*t)
	X_t[i,:] = x_t
	plt.plot(t, x_t) 

# Promedio de las N realizaciones en cada instante (cada punto en t)   
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6, color = 'k', label = 'Promedio de pruebas')

# Graficar el resultado teórico del valor esperado
E = 0*t
plt.plot(t, E, '-.', lw=4, label = 'Valor esperado')

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.legend()
plt.show()

######### Autocorrelación #########

# Se definen de nuevo las N realizaciones
N = 10

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Se define una Nueva figura para la autocorrelación
plt.figure()

# Cálculo de autocorrelación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de autocorrelación
Rxx = 15 * np.cos(W*taus)

# Gráficas de autocorrelación para cada realización y la autocorrelación teórica
plt.plot(taus, Rxx, '-.', lw=4, label='Autocorrelación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()