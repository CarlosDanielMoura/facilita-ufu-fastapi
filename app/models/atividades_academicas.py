from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from app.database.connection import Base

class Atividade_Academica(Base):
    __tablename__ = "atividade_academica"
    id_atividade_academica = Column(Integer, primary_key=True, nullable=False)
    semestre_vigente = Column(String, nullable=False)
    desc_atividade = Column(String, nullable=False)
    data_fim = Column(String, nullable=False)
    data_inicio = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
