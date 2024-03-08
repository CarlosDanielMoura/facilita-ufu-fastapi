from urllib import response
from fastapi.testclient import TestClient
from app.api.main import app  

client = TestClient(app)

def test_get_horario_onibus_all():
    response = client.get("/horario_onibus")
    assert response.status_code == 200
    data = response.json().get('horarios_onibus')
    assert data
    first_element = data[0]
    expected_keys = ["ponto_saida", "tipo_onibus", "id", "created_at", "horario_partida", "destino"]
    assert all(key in first_element for key in expected_keys)


def test_get_edital_all():
    response = client.get("/edital")
    assert response.status_code == 200
    data = response.json().get('edital') 
    assert data 
    first_element = data[0]
    expected_keys = ["org_resp", "cod_edital", "tipo", "link", "titulo", "dt_publicacao", "created_at"]
    assert all(key in first_element for key in expected_keys)
 

def test_get_professor_all():
    response = client.get("/professor")
    assert response.status_code == 200
    data = response.json().get('professor')
    assert data
    first_element = data[0]
    expected_keys = ["instituicao", "nome_completo", "created_at", "id_prof", "email", "sala_professor", "ramal"]
    assert all(key in first_element for key in expected_keys)
    
def test_get_all_atividade_academica():
    response = client.get("/atividade_academicas")
    assert response.status_code == 200
    data = response.json().get('atividades_academicas')
    assert data
    first_element = data[0]
    expected_keys = ["desc_atividade", "data_fim", "created_at", "semestre_vigente", "data_inicio", "id_atividade_academica"]
    assert all(key in first_element for key in expected_keys)


def test_get_all_cursos():
    response = client.get("/cursos")
    assert response.status_code == 200
    data = response.json().get('cursos')
    assert data
    first_element = data[0]
    expected_keys = ["cod_curso", "nome", "created_at"]
    assert all(key in first_element for key in expected_keys)

def test_get_all_disciplina():
    response = client.get("/disciplina")
    assert response.status_code == 200
    data = response.json().get('disciplina')
    assert data
    first_element = data[0]
    expected_keys = ["nome", "created_at", "cod_disciplina", "curso_id"]
    assert all(key in first_element for key in expected_keys)

def test_get_all_horario():
    response = client.get("/horario")
    assert response.status_code == 200
    data = response.json().get('horario')
    assert data
    first_element = data[0]
    expected_keys = ["hora_aula", "classificacao", "created_at", "cod_disciplina","cod_horario"]
    assert all(key in first_element for key in expected_keys)