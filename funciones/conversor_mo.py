def conversor(valor_dolar,pais):
    cantidad_moneda = float (input(f'ingrese catidad de {pais}:'))
    
    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print(f'tienes ${dolares}')
    
    conversor(4.000, 'pesos colomianos')