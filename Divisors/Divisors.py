import numpy as np 
 
num  = int(input("Ingrese un numero para obtener sus divisores: "))
# wait = input("presione enter para continua: ")
array_numeros = np.arange(1,num+1,1)
# print(array_numeros)
divisores = np.ones(1)
for x in array_numeros:
    if num%x==0 and x!=1:
        print(x)
        divisores= np.insert(divisores,len(divisores),x)
print(divisores)