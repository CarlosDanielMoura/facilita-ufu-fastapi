from sqlalchemy import TIMESTAMP, Column, Integer, String, text, ForeignKey
from app.database.connection import Base

class Disciplina(Base):
    __tablename__ = "disciplina"
    cod_disciplina = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String, nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.cod_curso", ondelete="CASCADE"), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
