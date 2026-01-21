"""
BASES DE DATOS: SQLALCHEMY
==========================
ORM (Object-Relational Mapping)
"""

print("=" * 50)
print("SQLALCHEMY - ORM")
print("=" * 50)

print("\nSQLAlchemy:")
print("  - ORM (Object-Relational Mapping)")
print("  - Trabajar con objetos en lugar de SQL")
print("  - Instalar: pip install sqlalchemy")

print("\nVentajas:")
print("  ✅ Código más Pythonico")
print("  ✅ Menos SQL manual")
print("  ✅ Compatible con múltiples bases de datos")

print("\nEjemplo básico:")
print("  from sqlalchemy import create_engine, Column, Integer, String")
print("  from sqlalchemy.ext.declarative import declarative_base")
print("")
print("  Base = declarative_base()")
print("")
print("  class Usuario(Base):")
print("      __tablename__ = 'usuarios'")
print("      id = Column(Integer, primary_key=True)")
print("      nombre = Column(String)")
print("      edad = Column(Integer)")

print("\nCrear tabla:")
print("  engine = create_engine('sqlite:///base.db')")
print("  Base.metadata.create_all(engine)")

print("\nInsertar:")
print("  from sqlalchemy.orm import sessionmaker")
print("  Session = sessionmaker(bind=engine)")
print("  session = Session()")
print("  usuario = Usuario(nombre='Juan', edad=30)")
print("  session.add(usuario)")
print("  session.commit()")

print("\nConsultar:")
print("  usuarios = session.query(Usuario).all()")
print("  usuario = session.query(Usuario).filter_by(nombre='Juan').first()")

print("\nActualizar:")
print("  usuario.edad = 31")
print("  session.commit()")

print("\nEliminar:")
print("  session.delete(usuario)")
print("  session.commit()")

print("\n" + "=" * 50)
