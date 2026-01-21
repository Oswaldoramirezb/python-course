"""
NETWORKING: URLLIB
==================
Trabajar con URLs y HTTP
"""

print("=" * 50)
print("URLLIB - URLs Y HTTP")
print("=" * 50)

from urllib.request import urlopen, Request
from urllib.parse import urlparse, urlencode

# Abrir URL
print("\nAbrir URL:")
print("  from urllib.request import urlopen")
print("  response = urlopen('https://www.python.org')")
print("  contenido = response.read()")

# Parsear URL
url = "https://www.ejemplo.com:8080/ruta?param=valor#fragmento"
parsed = urlparse(url)
print(f"\nParsear URL:")
print(f"  url = '{url}'")
print(f"  scheme = {parsed.scheme}")
print(f"  netloc = {parsed.netloc}")
print(f"  path = {parsed.path}")
print(f"  query = {parsed.query}")

# Codificar parámetros
params = {"nombre": "Juan", "edad": 30}
query_string = urlencode(params)
print(f"\nCodificar parámetros:")
print(f"  params = {params}")
print(f"  urlencode(params) = '{query_string}'")

# Request con headers
print("\nRequest con headers:")
print("  from urllib.request import Request")
print("  req = Request(url, headers={'User-Agent': 'Python'})")
print("  response = urlopen(req)")

print("\nFunciones:")
print("  urlopen() - Abrir URL")
print("  urlparse() - Parsear URL")
print("  urlencode() - Codificar parámetros")
print("  Request() - Crear request personalizado")

print("\n" + "=" * 50)
