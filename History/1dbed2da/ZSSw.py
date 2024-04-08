from pathlib import Path
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ente(Base):
    __tablename__ = 'entes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(60))
    canal_cobranza = Column(Integer)
    cuit = Column(String(11))
    tipo_ente = Column(Integer)
    cabecera_ticket = Column(String(35))
    nombre_corto = Column(String(20))
    grupo = Column(Integer)
    rubro = Column(Integer)
    componente = Column(String)
    nombre_clase = Column(String)
    habilitado = Column(Integer)
    pie_literal_validez = Column(String(35))
    codigo_sam = Column(String(4))
    codigo_subente_sam = Column(String(4))
    codigo_banco = Column(String(4))

    def __repr__(self):
        return f"<Ente(id={self.id}, nombre='{self.nombre}', cuit='{self.cuit}')>"
