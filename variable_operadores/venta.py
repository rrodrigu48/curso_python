print('----- REALIZAR UNA VENTA-------')
#entrada de datos 
precio = float(input('ingrese en el precio del ventas :'))

#operaciones
igv = precio * 0.18

pv = precio + igv

#salida de datos
print('='*25)
print('----FACTURA DE VENTA------')
print('='*25)
print ('el precio es :',precio)
print('el inpuesto es :',igv)
print('el precio de venta es :',pv)
print('='*25)