from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.atividades_academicas import Atividade_Academica


def get_atividade_academica(db: Session):
    data = db.query(Atividade_Academica).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Atividades acadêmica não encontrada")
    return {"atividades_academicas": data}
