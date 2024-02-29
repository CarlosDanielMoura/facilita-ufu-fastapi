from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.edital import Edital


def get_edital(db: Session):
    data = db.query(Edital).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Edital não encontrado")
    return {"edital": data}
