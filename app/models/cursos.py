from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from app.database.connection import Base

class Curso(Base):
    __tablename__ = "cursos"
    cod_curso = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
