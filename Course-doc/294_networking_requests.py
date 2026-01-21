"""
NETWORKING: REQUESTS
====================
Biblioteca requests para HTTP
"""

print("=" * 50)
print("REQUESTS - HTTP SIMPLIFICADO")
print("=" * 50)

print("\nRequests:")
print("  - Biblioteca popular para HTTP")
print("  - Más simple que urllib")
print("  - Instalar: pip install requests")

print("\nGET request:")
print("  import requests")
print("  response = requests.get('https://api.ejemplo.com')")
print("  print(response.status_code)")
print("  print(response.json())")

print("\nPOST request:")
print("  datos = {'clave': 'valor'}")
print("  response = requests.post('https://api.ejemplo.com', json=datos)")

print("\nCon headers:")
print("  headers = {'Authorization': 'Bearer token'}")
print("  response = requests.get(url, headers=headers)")

print("\nCon parámetros:")
print("  params = {'q': 'python'}")
print("  response = requests.get(url, params=params)")

print("\nMétodos:")
print("  requests.get() - GET request")
print("  requests.post() - POST request")
print("  requests.put() - PUT request")
print("  requests.delete() - DELETE request")

print("\nResponse:")
print("  response.status_code - Código de estado")
print("  response.text - Contenido como texto")
print("  response.json() - Contenido como JSON")
print("  response.headers - Headers de respuesta")

print("\nVentajas:")
print("  ✅ Más simple que urllib")
print("  ✅ Manejo automático de JSON")
print("  ✅ Mejor manejo de errores")
print("  ✅ Sesiones y autenticación")

print("\n" + "=" * 50)
