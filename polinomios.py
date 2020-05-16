import numpy as np
p = np.poly1d([])
tit="raíces racionales".capitalize()
print(tit.center(50, "="))
n=int(input('Dame el valor del grado de tu polinomio: '))
print("\nIntroduce los valores de tus coeficientes de forma descendente.\n\t\t\t\t\t\t\t".center(80, "!"))
for i in range(0, n+1):
    p[n-i] = input('Coeficiente del término x^['+ str(n-i) +']: ')
print("Tu polinomio es el siguiente:".center(50, "="))
print(p)
print("Las raíces de tu polinomio son:".center(50, "="))
print(p.roots)