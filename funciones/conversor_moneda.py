
from pickletools import float8
from tkinter import Menu


def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f'ingrese la cantidad de {pais}: ',))

    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print(f'tienes $ {dolares}',)
    
def main():
    while True:
        Menu == """ 
        1- soles peruanos a dolares
        2- pesos mexicanos a dolares
        3- pesos colombianos a dolares
        4- salir
        ingresa una opcion:"""
        opcion = input(Menu)
        
        if opcion == '1':
            convertir(3.61,'soles purianos')
        elif opcion == '2':
            convertir(20,'pesos mexicanos')
        elif opcion == '3':
            convertir(3500,'pesos colombianos')
        elif opcion == '4':
            print('cerrando el conversor')
            break
        else:
            print ('vuelva a ingresar una opcion')
    
 #punto de inicio de la app   
if __name__ == '__main__':
    main()