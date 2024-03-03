from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.cursos import Curso


def get_cursos(db: Session):
    data = db.query(Curso).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    return {"cursos": data}
