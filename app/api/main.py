from fastapi import FastAPI, Depends
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.controller.horario_onibus import get_horario_onibus
from app.controller.edital import get_edital

app = FastAPI()


@app.get("/horario_onibus")
def get_horario_onibus_all(db: Session = Depends(get_db)):
    return get_horario_onibus(db)


@app.get("/edital")
def get_edital_all(db: Session = Depends(get_db())):
    return get_edital(db)
