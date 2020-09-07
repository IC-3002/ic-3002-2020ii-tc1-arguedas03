#para menor espacio importar la biblioteca math 
#y usar el .factorial
def factorial (entero):
    factorial = 1
    while(entero > 0):
        factorial= factorial*entero
        entero   = entero - 1
    return factorial 

def e_cuadratica(n):
    i = 0
    e = 0
    while(i<=n):
        e += 1/factorial(i)
        i += 1
    return e

def e_lineal(n):
    i = 0
    e = 0
    factorial = 1
    while(i<=n):
        e += 1/factorial
        i += 1
        factorial = factorial*i
    return e
