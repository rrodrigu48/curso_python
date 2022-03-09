import random

def jugar(vidas):
    numero_randon = random.randint(1, 100)
    numero_elegido = None
    
    while numero_randon != numero_elegido:
        numero_elegido = int(input('ingrese un numero entre 1 y 100: '))
    
        if numero_randon < numero_elegido:
            print('elige un numero mas pequeño')
            vidas -= 1
        elif numero_randon > numero_elegido:
            print('elige un numero mas grande')
            vidas -= 1
        
        if vidas == 0:
            print('GAME OVER')
            break    
            
        print(f'te quedan {vidas}')
    
    if numero_elegido == numero_randon:
       print('ganaste el juego') 

jugar(10)