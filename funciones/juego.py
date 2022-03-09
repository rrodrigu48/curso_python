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

def main():
    while True:
        menu = """
        adivina el numero
            1- nivel facil
            2- nivel intermedio
            3- nivel dificil
            4- salir
        """
        opcion = input (menu)
        
        if opcion =='1':
            jugar(10)
        elif opcion == '2':
            jugar(7)
        elif opcion == '3':
            jugar(5)
        elif opcion == '4':
            print('cerrar secion')
            break
        else:  
            print('opcion incottecta')

 #punto de inicio de la app   
if __name__ == '__main__':
    main()