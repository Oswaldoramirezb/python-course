"""
NETWORKING: SOCKET
==================
Comunicación con sockets
"""

print("=" * 50)
print("SOCKET - COMUNICACIÓN")
print("=" * 50)

import socket

# Crear socket
print("\nCrear socket:")
print("  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")

# Obtener información de host
host = "www.google.com"
try:
    ip = socket.gethostbyname(host)
    print(f"\nResolver hostname:")
    print(f"  socket.gethostbyname('{host}') = {ip}")
except socket.gaierror:
    print(f"  No se pudo resolver {host}")

# Información del socket local
hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)
print(f"\nInformación local:")
print(f"  socket.gethostname() = {hostname}")
print(f"  IP local = {ip_local}")

# Crear socket cliente (ejemplo)
print("\nSocket cliente:")
print("  s = socket.socket()")
print("  s.connect(('host', puerto))")
print("  s.send(b'datos')")
print("  datos = s.recv(1024)")
print("  s.close()")

# Crear socket servidor (ejemplo)
print("\nSocket servidor:")
print("  s = socket.socket()")
print("  s.bind(('localhost', puerto))")
print("  s.listen(5)")
print("  conn, addr = s.accept()")
print("  datos = conn.recv(1024)")

print("\nTipos:")
print("  SOCK_STREAM - TCP (confiable)")
print("  SOCK_DGRAM - UDP (rápido)")

print("\n" + "=" * 50)
