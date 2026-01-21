"""
RESUMEN: WEB SCRAPING
====================
Todas las operaciones de web scraping
"""

print("=" * 50)
print("RESUMEN - WEB SCRAPING")
print("=" * 50)

print("\nBibliotecas:")
print("  requests - Obtener contenido")
print("  BeautifulSoup - Parsear HTML")
print("  selenium - Navegador automatizado")
print("  lxml - Parser rápido")

print("\nProceso básico:")
print("  1. requests.get(url) - Obtener HTML")
print("  2. BeautifulSoup(html) - Parsear")
print("  3. soup.find() / find_all() - Extraer")
print("  4. Procesar y guardar")

print("\nBeautifulSoup:")
print("  soup.find('tag') - Encontrar uno")
print("  soup.find_all('tag') - Encontrar todos")
print("  soup.find('tag', class_='clase') - Por clase")
print("  soup.find('tag', id='id') - Por ID")
print("  elemento.text - Obtener texto")
print("  elemento['atributo'] - Obtener atributo")

print("\nSelenium:")
print("  driver = webdriver.Chrome()")
print("  driver.get(url)")
print("  elemento = driver.find_element(By.ID, 'id')")
print("  elemento.click()")
print("  driver.quit()")

print("\n⚠️  CONSIDERACIONES:")
print("  - Respetar robots.txt")
print("  - Usar delays")
print("  - Verificar términos de servicio")
print("  - No sobrecargar servidores")

print("\nUsos:")
print("  ✅ Extraer datos")
print("  ✅ Monitoreo")
print("  ✅ Análisis")
print("  ✅ Automatización")

print("\n" + "=" * 50)
