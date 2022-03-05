import random

def generar_contrasena():
    mayusculas = ['A','B','C','D','E','F','G']
    minusculas = ['a','b','c','d','e','f','g']
    simbolos = ['#','$','%','&']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    
    caracteres = mayusculas + minusculas + simbolos + numeros
    contra = []
    for i in range(15):
        carecter_random =random.choice(caracteres)
        contra.append(carecter_random)
        #converti lista en cadena de caracter
    contra = "".join(contra)
    return contra
#funcion principal
def main():
    contra = generar_contrasena()
    print('tu nueva contrasenña es :',contra)
        
if __name__ == '__main__':
    main()