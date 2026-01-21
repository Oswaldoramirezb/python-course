"""
TIPO DE DATO: STR (CADENAS DE TEXTO)
=====================================
Las cadenas son texto entre comillas: "Hola", 'Mundo'
"""

print("=" * 50)
print("CADENAS DE TEXTO (str)")
print("=" * 50)

# Crear cadenas con comillas dobles
texto1 = "Hola"
print(f"\nCon comillas dobles: {texto1}")

# Crear cadenas con comillas simples
texto2 = 'Mundo'
print(f"Con comillas simples: {texto2}")

# Concatenar (unir) cadenas
saludo = texto1 + " " + texto2
print(f"\nUnir cadenas: '{texto1}' + ' ' + '{texto2}' = '{saludo}'")

# Ver el tipo
print(f"\nEl tipo de '{texto1}' es: {type(texto1).__name__}")

print("\n" + "=" * 50)
