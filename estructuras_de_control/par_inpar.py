
n = int(input('ingrese un numero entero :'))
if n != 0:
    if n > 0:
        if n % 2 ==0:
            print(f'el numero {n} es par positivo')
        else:
            print(f'el numero {n} es inpar positivo ')
    else:
        if n % 2 ==0:
            print(f'el numero {n} es par negativo')
        else:
            print(f'el numero {n} es inpar negativo ')
        
else:
    print(f'el numero {n} es neutro')


pass # dejar una tarea para mas tarde 
