#son funciones mas cortas  
sumar=lambda a,b : a + b
doblar = lambda n : n * 2
par = lambda n : n % 2 == 0
impar = lambda n : n % 2 != 0
revertir = lambda cadena : cadena[::-1]
 
print(sumar(10,10))
print(doblar(20))
print (par (5))
print (impar(5))
print(revertir('holaaa'))
