def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    
    palabra_i = palabra[::-1]
    
    if palabra == palabra_i:
        return True
    else:
        return False
#funcion principal
def main():
    palabra = input('ingrese una palabra :')
    
    es_palindromo =palindromo(palabra)
    if  es_palindromo:
        print(f'la palabra {palabra} es palindroma')
    else:
        print(f'la palabra {palabra} no es palindroma')
    pass
#puerta de entrada de la aplicacion
if __name__ == '__main__':
    main()
    #se agrega comentario de practica 
    