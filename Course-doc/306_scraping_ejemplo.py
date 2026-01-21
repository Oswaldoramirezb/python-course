"""
WEB SCRAPING: EJEMPLO COMPLETO
===============================
Ejemplo completo de web scraping
"""

print("=" * 50)
print("EJEMPLO COMPLETO")
print("=" * 50)

from bs4 import BeautifulSoup

# HTML de ejemplo (simulando respuesta de requests)
html_ejemplo = """
<html>
<head><title>Tienda Online</title></head>
<body>
    <div class="productos">
        <div class="producto">
            <h2>Laptop</h2>
            <p class="precio">$999.99</p>
            <p class="descripcion">Laptop potente</p>
        </div>
        <div class="producto">
            <h2>Mouse</h2>
            <p class="precio">$29.99</p>
            <p class="descripcion">Mouse inalámbrico</p>
        </div>
        <div class="producto">
            <h2>Teclado</h2>
            <p class="precio">$79.99</p>
            <p class="descripcion">Teclado mecánico</p>
        </div>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_ejemplo, 'html.parser')

print("\nExtraer productos:")
print("  soup = BeautifulSoup(html, 'html.parser')")
print("  productos = soup.find_all('div', class_='producto')")

productos = soup.find_all('div', class_='producto')

print("\nDatos extraídos:")
for producto in productos:
    nombre = producto.find('h2').text
    precio = producto.find('p', class_='precio').text
    descripcion = producto.find('p', class_='descripcion').text
    
    print(f"  Producto: {nombre}")
    print(f"    Precio: {precio}")
    print(f"    Descripción: {descripcion}")

# Convertir a lista de diccionarios
datos = []
for producto in productos:
    datos.append({
        'nombre': producto.find('h2').text,
        'precio': producto.find('p', class_='precio').text,
        'descripcion': producto.find('p', class_='descripcion').text
    })

print(f"\nDatos estructurados:")
print(f"  {datos}")

print("\nProceso completo:")
print("  1. Obtener HTML (requests.get())")
print("  2. Parsear (BeautifulSoup)")
print("  3. Extraer datos (find, find_all)")
print("  4. Procesar y guardar")

print("\n" + "=" * 50)
