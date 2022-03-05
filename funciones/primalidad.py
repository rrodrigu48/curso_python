def es_primo(numero):
    com = 0
    
    for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue
        #verifica que la division con los nmeros hasta el numero 
        #ingresado sea igual a 0
        if numero % i == 0:
            com +=1
            
    if com == 0:
        return True
    else:
        return False
             
# fucion principal
def main():
    numero =int(input('ingresa un numero :'))
    
    if es_primo(numero):
        print(f'el numero {numero} es primo ')
    else:
        print(f'el numero {numero} no es primo ')

if __name__ == '__main__':
    main()