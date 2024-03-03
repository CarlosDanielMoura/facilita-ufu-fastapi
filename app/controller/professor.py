from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.professor import Professor


def get_professor(db: Session):
    data = db.query(Professor).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professores não encontrado")
    return {"professor": data}
