from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from app.database.connection import Base


class Professor(Base):
    __tablename__ = "professor"
    id_prof = Column(Integer, primary_key=True, nullable=False)
    nome_completo = Column(String, nullable=False)
    email = Column(String, nullable=False)
    sala_professor = Column(String, nullable=False)
    instituicao = Column(String, nullable=False)
    ramal = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
