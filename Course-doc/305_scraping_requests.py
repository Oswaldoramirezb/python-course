"""
WEB SCRAPING: REQUESTS
======================
Obtener contenido web
"""

print("=" * 50)
print("REQUESTS - OBTENER CONTENIDO")
print("=" * 50)

print("\nRequests:")
print("  - Obtener contenido de URLs")
print("  - Instalar: pip install requests")
print("  - Más simple que urllib")

print("\nGET request básico:")
print("  import requests")
print("  response = requests.get('https://ejemplo.com')")
print("  print(response.status_code)")
print("  print(response.text)")

print("\nCon headers:")
print("  headers = {")
print("      'User-Agent': 'Mozilla/5.0 ...'")
print("  }")
print("  response = requests.get(url, headers=headers)")

print("\nCon parámetros:")
print("  params = {'q': 'python', 'page': 1}")
print("  response = requests.get(url, params=params)")

print("\nManejo de errores:")
print("  try:")
print("      response = requests.get(url)")
print("      response.raise_for_status()")
print("  except requests.exceptions.RequestException as e:")
print("      print(f'Error: {e}')")

print("\nPropiedades de response:")
print("  response.status_code - Código de estado")
print("  response.text - Contenido como texto")
print("  response.content - Contenido como bytes")
print("  response.headers - Headers de respuesta")
print("  response.url - URL final")

print("\nSesiones:")
print("  session = requests.Session()")
print("  session.get(url)  # Mantiene cookies")

print("\n⚠️  BUENAS PRÁCTICAS:")
print("  - Usar delays entre requests")
print("  - Respetar robots.txt")
print("  - Usar User-Agent apropiado")
print("  - Manejar errores")

print("\n" + "=" * 50)
