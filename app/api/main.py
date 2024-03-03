from fastapi import FastAPI, Depends
from app.database.connection import engine, Base, get_db
from sqlalchemy.orm import Session
from app.controller.horario_onibus import get_horario_onibus
from app.controller.edital import get_edital
from app.controller.professor import get_professor
from app.controller.atividade_academicas import get_atividade_academica
from app.controller.curso import get_cursos
from app.controller.disciplina import get_disciplina
from app.controller.horario import get_horario

Base.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
def startup_event():
    # Isso criará as tabelas, se elas ainda não existirem.
    Base.metadata.create_all(bind=engine)


@app.get("/horario_onibus")
def get_horario_onibus_all(db: Session = Depends(get_db)):
    return get_horario_onibus(db)


@app.get("/edital")
def get_edital_all(db: Session = Depends(get_db)):
    return get_edital(db)


@app.get("/professor")
def get_professor_all(db: Session = Depends(get_db)):
    return get_professor(db)


@app.get("/atividade_academicas")
def get_all_atividade_academica(db: Session = Depends(get_db)):
    return get_atividade_academica(db)


@app.get("/cursos")
def get_all_cursos(db: Session = Depends(get_db)):
    return get_cursos(db)


@app.get("/disciplina")
def get_all_disciplina(db: Session = Depends(get_db)):
    return get_disciplina(db)

@app.get("/horario")
def get_all_horario(db: Session = Depends(get_db)):
    return get_horario(db)
