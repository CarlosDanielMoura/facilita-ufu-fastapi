from sqlalchemy import TIMESTAMP, Column, Integer, String, text, ForeignKey
from app.database.connection import Base

class Horario(Base):
    __tablename__ = "horario"
    cod_horario = Column(Integer, primary_key=True, nullable=False)
    hora_aula = Column(String, nullable=False)
    classificacao = Column(String, nullable=False)
    cod_disciplina = Column(ForeignKey("disciplina.cod_disciplina", ondelete="CASCADE"), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
