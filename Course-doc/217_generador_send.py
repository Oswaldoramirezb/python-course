"""
GENERADOR: SEND
===============
Enviar valores al generador
"""

print("=" * 50)
print("GENERADOR CON SEND()")
print("=" * 50)

# Generador con send()
def contador():
    """Generador que puede recibir valores"""
    valor = 0
    while True:
        recibido = yield valor
        if recibido is not None:
            valor = recibido
        else:
            valor += 1

gen = contador()
print("\nGenerador con send():")
print("  def contador():")
print("      valor = 0")
print("      while True:")
print("          recibido = yield valor")
print("          if recibido is not None:")
print("              valor = recibido")

print("\nUsar generador:")
print(f"  next(gen) = {next(gen)}  # Iniciar generador")
print(f"  gen.send(10) = {gen.send(10)}  # Enviar valor")
print(f"  next(gen) = {next(gen)}  # Continuar")
print(f"  next(gen) = {next(gen)}")

print("\n⚠️  IMPORTANTE:")
print("  - Primero usar next() o send(None) para iniciar")
print("  - send() envía valor y retorna el siguiente yield")

print("\nUso:")
print("  - Comunicación bidireccional")
print("  - Control de estado del generador")
print("  - Corrutinas")

print("\n" + "=" * 50)
