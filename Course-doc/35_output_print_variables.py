"""
OUTPUT: PRINT CON VARIABLES
===========================
Mostrar el valor de variables
"""

print("=" * 50)
print("PRINT CON VARIABLES")
print("=" * 50)

# Variables
nombre = "Juan"
edad = 25

# Print con variables
print(f"\nPrint con f-string:")
print(f"Mi nombre es {nombre} y tengo {edad} años")

# Print con .format()
print("\nPrint con .format():")
print("Mi nombre es {} y tengo {} años".format(nombre, edad))

# Print con % (estilo antiguo)
print("\nPrint con %:")
print("Mi nombre es %s y tengo %d años" % (nombre, edad))

print("\n" + "=" * 50)
