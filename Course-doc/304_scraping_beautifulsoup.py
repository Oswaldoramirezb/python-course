"""
WEB SCRAPING: BEAUTIFULSOUP
===========================
Parsear HTML con BeautifulSoup
"""

print("=" * 50)
print("BEAUTIFULSOUP - PARSEAR HTML")
print("=" * 50)

from bs4 import BeautifulSoup

# HTML de ejemplo
html = """
<html>
<head><title>Ejemplo</title></head>
<body>
    <h1>Título Principal</h1>
    <p class="intro">Este es un párrafo de introducción.</p>
    <div id="contenido">
        <p>Párrafo 1</p>
        <p>Párrafo 2</p>
        <a href="https://ejemplo.com">Enlace</a>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

print("\nParsear HTML:")
print("  from bs4 import BeautifulSoup")
print("  soup = BeautifulSoup(html, 'html.parser')")

# Obtener título
titulo = soup.title.text
print(f"\nObtener título:")
print(f"  soup.title.text = '{titulo}'")

# Obtener por etiqueta
h1 = soup.find('h1')
print(f"\nObtener por etiqueta:")
print(f"  soup.find('h1') = {h1}")
print(f"  soup.find('h1').text = '{h1.text}'")

# Obtener por clase
parrafo = soup.find('p', class_='intro')
print(f"\nObtener por clase:")
print(f"  soup.find('p', class_='intro') = {parrafo}")
print(f"  .text = '{parrafo.text}'")

# Obtener por ID
div = soup.find('div', id='contenido')
print(f"\nObtener por ID:")
print(f"  soup.find('div', id='contenido') = {div}")

# Obtener todos
parrafos = soup.find_all('p')
print(f"\nObtener todos:")
print(f"  soup.find_all('p') = {len(parrafos)} párrafos")
for p in parrafos:
    print(f"    - {p.text}")

# Obtener atributos
enlace = soup.find('a')
print(f"\nObtener atributos:")
print(f"  enlace['href'] = {enlace['href']}")

print("\n" + "=" * 50)
