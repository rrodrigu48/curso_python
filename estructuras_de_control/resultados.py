import random

par =[]
inpar = []
numeros = (1,2,3,4,5,6,7,8,9)
for n in numeros:
    numero_random = random.randint(1,100)
    resultado = n * numero_random
     
    if resultado % 2 == 0:
        print(f'{n} x {numero_random} = {resultado}')
        par.append(resultado)
    else:
        print(f'{n} x {numero_random} = {resultado}')
        inpar.append(resultado)
        
print ('Lista de pares :',par)
print ('lista de inpares :',inpar)

