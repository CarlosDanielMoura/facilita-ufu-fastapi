from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.disciplina import Disciplina


def get_disciplina(db: Session):
    data = db.query(Disciplina).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Disciplina não encontrado")
    return {"disciplina": data}
