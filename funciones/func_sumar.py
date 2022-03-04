
#  *args = indeterminados por pocision
# **kwargs = indeterminados por nombres
def sumar (*args, **kwargs):
    suma = 0
    for n in args:
        suma +=n
    return suma, kwargs
   # print (*args)

suma_total ,datos = sumar(1,2,3,4,5,6,nombre= 'ricardo' , edad = 23)
print('la suma totoa es : ',suma_total)
print(datos)


    