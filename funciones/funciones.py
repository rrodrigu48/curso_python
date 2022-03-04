#crear una fucion
""""
def saludar ():
    global nombre #volver la variabre (nombre)global
    nombre = 'ricardo rodriguez'
    print('holaa desde la funcion saludar')
    
saludar()
print('hola desde fuera de la funcion',nombre)
"""

def saludar(nombre):
    return f'hola,{nombre} desde la funcion saludar'

def sumar (a,b):
    return a + b

def restar (a,b):
    if a== None or b==None:
        print('error:debes de enviar dos numeros a la funcion')
        return
    return a - b
#argumentos de la funcion 1 
saludo = saludar('ricardo')
print(saludo)

suma = sumar(5,5)
print('la suma es:',suma)

resta = restar(a = int(input('digita el numero a ')), b = int(input('digita el numero b ')))
print('la resta es ',resta)






