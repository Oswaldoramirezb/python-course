"""
NETWORKING: SERVIDOR
====================
Crear servidor HTTP simple
"""

print("=" * 50)
print("SERVIDOR HTTP")
print("=" * 50)

from http.server import HTTPServer, BaseHTTPRequestHandler

# Handler personalizado
class MiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Manejar GET requests"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        mensaje = "<h1>Servidor Python</h1><p>¡Hola desde Python!</p>"
        self.wfile.write(mensaje.encode())

print("\nCrear servidor:")
print("  from http.server import HTTPServer, BaseHTTPRequestHandler")
print("")
print("  class MiHandler(BaseHTTPRequestHandler):")
print("      def do_GET(self):")
print("          self.send_response(200)")
print("          self.send_header('Content-type', 'text/html')")
print("          self.end_headers()")
print("          self.wfile.write(b'<h1>Hola</h1>')")
print("")
print("  servidor = HTTPServer(('localhost', 8000), MiHandler)")
print("  servidor.serve_forever()")

print("\nMétodos:")
print("  do_GET() - Manejar GET")
print("  do_POST() - Manejar POST")
print("  send_response() - Enviar código de estado")
print("  send_header() - Enviar header")
print("  wfile.write() - Escribir respuesta")

print("\nEjecutar:")
print("  python servidor.py")
print("  Abrir: http://localhost:8000")

print("\n⚠️  NOTA:")
print("  Este es un servidor básico para desarrollo")
print("  Para producción usar frameworks como Flask o Django")

print("\n" + "=" * 50)
