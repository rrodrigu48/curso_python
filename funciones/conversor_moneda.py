
def convertir(valor_dolar,pais):
    cantidad_moneda = float(input('ingrese la cantidad : ',pais))

    dolares = cantidad_moneda / valor_dolar
    dolares = round (dolares,2)
    print('tienes $ ',dolares)

    convertir(3.61,'soles purianos')