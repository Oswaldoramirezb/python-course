"""
WEB SCRAPING: CONCEPTO
======================
Extraer información de páginas web
"""

print("=" * 50)
print("CONCEPTO DE WEB SCRAPING")
print("=" * 50)

print("\nWeb Scraping:")
print("  - Extraer información de páginas web")
print("  - Automatizar recolección de datos")
print("  - Parsear HTML/XML")

print("\nBibliotecas principales:")
print("  requests - Obtener contenido web")
print("  BeautifulSoup - Parsear HTML")
print("  lxml - Parser rápido")
print("  selenium - Navegador automatizado")

print("\nProceso:")
print("  1. Obtener HTML (requests)")
print("  2. Parsear HTML (BeautifulSoup)")
print("  3. Extraer datos")
print("  4. Procesar y guardar")

print("\nEjemplo básico:")
print("  import requests")
print("  from bs4 import BeautifulSoup")
print("")
print("  response = requests.get('https://ejemplo.com')")
print("  soup = BeautifulSoup(response.text, 'html.parser')")
print("  titulo = soup.find('h1').text")

print("\n⚠️  CONSIDERACIONES:")
print("  - Respetar robots.txt")
print("  - No sobrecargar servidores")
print("  - Verificar términos de servicio")
print("  - Usar delays entre requests")

print("\nUsos:")
print("  ✅ Extraer datos de sitios web")
print("  ✅ Monitoreo de precios")
print("  ✅ Análisis de contenido")
print("  ✅ Automatización")

print("\n" + "=" * 50)
