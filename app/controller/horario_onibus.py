from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.horario_onibus import Horario_Onibus


def get_horario_onibus(db: Session):
    data = db.query(Horario_Onibus).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Horário de ônibus não encontrado")
    return {"horarios_onibus": data}
