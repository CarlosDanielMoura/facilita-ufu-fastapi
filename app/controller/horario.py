from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.horario import Horario


def get_horario(db: Session):
    data = db.query(Horario).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Horário não encontrado")
    return {"horario": data}
