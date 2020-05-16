import numpy as np
import math
p = np.poly1d([])
tit="raíces racionales".capitalize()
print(tit.center(50, "="))
n=int(input('Dame el valor del grado de tu polinomio: '))
print("Introduce los valores de tus coeficientes.-\n")
for i in range(0, n+1):
    p[i] = input('Coeficiente del término x^[' + str(i) +']: ')
print("Tu polinomio es el siguiente:".center(50, "="))
print(p)
print("Las raíces de tu polinomio son:".center(50, "="))
print(p.roots)
