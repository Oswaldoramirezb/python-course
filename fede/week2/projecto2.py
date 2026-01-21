nombre = input ("Ingresa tu nombre: ")
ventas = input ("Ingresa tus ventas: ")
comision = float(ventas) * 0.13
comision = round (comision,2)
print (f"Ok {nombre}, este mes ganaste {comision}")
