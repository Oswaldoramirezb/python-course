mi_texto = "Esta es una pruebA."
resultado = mi_texto[2]
print(resultado)
#derecha a izquierda
resultado = mi_texto[0] #para derecha a izquierda o izq derecha es la misma posicion
print(resultado)

resultado = mi_texto[-1]
print(resultado)

resultado = mi_texto[-2]
print(resultado)

resultado = mi_texto.index("una")
print(resultado)

#primero la letra que busca
resultado = mi_texto.index("r")
print(resultado)


#segundo desde que posicion
resultado = mi_texto.index("a",5)
print(resultado)

#tercero hasta que posicion
resultado = mi_texto.index("A", 5, 18)
print(resultado)
