"""
RESUMEN: NETWORKING
===================
Todas las operaciones de networking
"""

print("=" * 50)
print("RESUMEN - NETWORKING")
print("=" * 50)

print("\nMódulos:")
print("  socket - Comunicación de bajo nivel")
print("  urllib - URLs y HTTP básico")
print("  requests - HTTP simplificado (pip install requests)")
print("  http.server - Servidor HTTP simple")

print("\nSocket:")
print("  s = socket.socket()")
print("  s.connect(('host', puerto))")
print("  s.send(b'datos')")
print("  datos = s.recv(1024)")

print("\nURLLIB:")
print("  from urllib.request import urlopen")
print("  response = urlopen('https://ejemplo.com')")
print("  contenido = response.read()")

print("\nRequests:")
print("  import requests")
print("  response = requests.get('https://api.com')")
print("  datos = response.json()")

print("\nServidor:")
print("  from http.server import HTTPServer, BaseHTTPRequestHandler")
print("  class MiHandler(BaseHTTPRequestHandler):")
print("      def do_GET(self): ...")

print("\nConceptos:")
print("  Socket - Punto de comunicación")
print("  IP - Dirección de red")
print("  Puerto - Punto de acceso")
print("  Protocolo - Reglas de comunicación")

print("\nUsos:")
print("  ✅ APIs y servicios web")
print("  ✅ Cliente-servidor")
print("  ✅ Transferencia de datos")
print("  ✅ Comunicación distribuida")

print("\n" + "=" * 50)
