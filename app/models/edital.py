from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from app.database.connection import Base

class Edital(Base):
    __tablename__ = "edital"
    cod_edital = Column(Integer, primary_key=True, nullable=False)
    org_resp = Column(String, nullable=False)
    titulo = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    dt_publicacao = Column(String, nullable=False)
    link = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
