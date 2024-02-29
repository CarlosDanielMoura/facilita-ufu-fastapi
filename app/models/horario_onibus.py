from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text
from app.database.connection import Base

class Horario_Onibus(Base):
    __tablename__ = "horario_onibus"
    id = Column(Integer, primary_key=True, nullable=False)
    horario_partida = Column(String, nullable=False)
    ponto_saida = Column(String, nullable=False)
    tipo_onibus = Column(String, nullable=False)
    destino = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
