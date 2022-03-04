#entreda
valor = float(input('ingrese el consumo :'))
if valor >= 0:

    if valor <= 100:
        #descuento 10%
        datos_descuento = '10%'
        descuento = valor * 0.10
    elif valor > 100 and valor <=200:
        #descuento 20%
        datos_descuento ='20%'
        descuento = valor * 0.20
    elif valor > 200:
        datos_descuento = '30'
        descuento = valor * 0.30
        
    #operacion    
    monto_d = valor - descuento
    igv = monto_d * 0.19
    total_d = igv + monto_d

    #salida
    print('='*30)
    print('----- FACTURA DE CONSUMOS -----')
    print('descuento que se aplica :',datos_descuento)
    print('='*30)
    print('consumo :',valor)
    print('descuento :',monto_d)
    print('inpuesto :',igv)
    print('total a pagar :',total_d)
    print('='*30)

else:
    print('error al ingresar el valor ')