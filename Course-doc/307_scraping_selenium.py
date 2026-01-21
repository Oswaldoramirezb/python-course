"""
WEB SCRAPING: SELENIUM
======================
Automatizar navegador
"""

print("=" * 50)
print("SELENIUM - NAVEGADOR AUTOMATIZADO")
print("=" * 50)

print("\nSelenium:")
print("  - Automatizar navegador real")
print("  - Útil para JavaScript dinámico")
print("  - Instalar: pip install selenium")
print("  - Requiere driver (Chrome, Firefox, etc.)")

print("\nConfiguración:")
print("  from selenium import webdriver")
print("  from selenium.webdriver.common.by import By")
print("")
print("  driver = webdriver.Chrome()")
print("  driver.get('https://ejemplo.com')")

print("\nBuscar elementos:")
print("  elemento = driver.find_element(By.ID, 'elemento')")
print("  elementos = driver.find_elements(By.CLASS_NAME, 'clase')")
print("  elemento = driver.find_element(By.XPATH, '//div[@id=\"id\"]')")

print("\nInteracciones:")
print("  elemento.click() - Hacer clic")
print("  elemento.send_keys('texto') - Escribir")
print("  elemento.text - Obtener texto")
print("  elemento.get_attribute('href') - Obtener atributo")

print("\nEsperas:")
print("  from selenium.webdriver.support.ui import WebDriverWait")
print("  from selenium.webdriver.support import expected_conditions as EC")
print("")
print("  wait = WebDriverWait(driver, 10)")
print("  elemento = wait.until(EC.presence_of_element_located((By.ID, 'id')))")

print("\nCerrar:")
print("  driver.quit()")

print("\nVentajas:")
print("  ✅ Maneja JavaScript")
print("  ✅ Interacción real")
print("  ✅ Útil para SPAs")

print("\nDesventajas:")
print("  ❌ Más lento")
print("  ❌ Requiere driver")
print("  ❌ Más recursos")

print("\nCuándo usar:")
print("  - Contenido generado por JavaScript")
print("  - Necesitas interactuar con la página")
print("  - BeautifulSoup no es suficiente")

print("\n" + "=" * 50)
