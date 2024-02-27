#from typing import Optional
from fastapi import FastAPI
import pandas as pd

#Instanciando a API
app = FastAPI()

from pydantic import BaseModel

@app.get("/geo")
def create_item():
    horarios = pd.read_csv("./horariosGeologia.csv",sep=";")
    return horarios


@app.get("/editais")
def get_editais():
    editais = pd.read_csv("./editais_ufu.csv", sep=";")
    return editais