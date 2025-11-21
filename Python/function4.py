'''
   script description:
   crea una funcon que al ejecutar el programa genere dos
   numeros enteros aleatorios, los sume y muestre en panalla el resultado
   recomendacion: hacer dos funciones para el mismo proceso
   f1: calc_add1: sin retorno
   f2: calc_add2: con retorno
'''
import random
import time
def calc_add0():
    x = random.randint(1, 1000) 
    y = random.randint(1, 1000)
    add = x + y
    print(f"[F0. basic] Addition is: {add}")

def calc_add1(x, y):
    add = x + y
    print(f"[F1. without return] Addition is: {add}")

def calc_add2(x, y):
    add = x + y
    return add

# main
n1 = random.randint(1, 1000) 
n2 = random.randint(1, 1000)

start = time.perf_counter()
calc_add0()
end = time.perf_counter()

start = time.perf_counter()
calc_add1(n1, n2)
end = time.perf_counter()

start = time.perf_counter()
answer = calc_add2(n1, n2)
print(f"[F2. with return] Addition is: {answer}")
end = time.perf_counter()

print()
print(f"Total time F0: {end - start}")
print(f"Total time F1: {end - start}")
print(f"Total time F2: {end - start}")