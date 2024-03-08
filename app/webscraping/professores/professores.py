import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from sqlalchemy import create_engine

url_primeira_pagina = 'https://ufu.br/monte-carmelo/docentes'
base_url = 'https://ufu.br/monte-carmelo/docentes?page='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def extrair_informacoes(soup):
    content = soup.find('div', class_='view-content')
    if not content:
        print(f"Conteúdo não encontrado")
        return []
   
    lista_professores = []
    for info in content.find_all('div', class_='views-row'):
        nome_prof = info.find('div', class_='field-name-title')
        email_prof = info.find('div', class_='field-name-field-email')
        curso_prof = info.find('div', class_='field-name-field-uorg-superior')
        telefone_prof = info.find('div', class_='field-name-field-telefone')
       
        nome = nome_prof.text.strip() if nome_prof else "N/D"
        email = email_prof.text.strip() if email_prof else "N/D"
        curso = curso_prof.text.strip() if curso_prof else "N/D"
        telefone = telefone_prof.text.strip() if telefone_prof else "N/D"
       
        lista_professores.append({'Nome': nome, 'Email': email, 'Curso Superior': curso, 'Telefone': telefone})
   
    return lista_professores

# Conectar-se ao banco de dados PostgreSQL usando SQLAlchemy
engine = create_engine("postgresql://postgres:root@localhost/facilitaufu")

with requests.Session() as session:
    session.headers.update(headers)
    df = pd.DataFrame(columns=['Nome', 'Email', 'Curso Superior', 'Telefone'])
   
    try:
        r = session.get(url_primeira_pagina)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar a página {url_primeira_pagina}: {e}")
    else:
        soup = BeautifulSoup(r.content, 'html.parser')
        df = pd.concat([df, pd.DataFrame(extrair_informacoes(soup))], ignore_index=True)
       
        for pagina in range(2, 11):
            url = base_url + str(pagina)
            print(f"Acessando página {url}")
           
            try:
                r = session.get(url)
                r.raise_for_status()
            except requests.RequestException as e:
                print(f"Erro ao acessar a página {url}: {e}")
                break
            else:
                soup = BeautifulSoup(r.content, 'html.parser')
                df = pd.concat([df, pd.DataFrame(extrair_informacoes(soup))], ignore_index=True)
               
            time.sleep(2)

# Escrever o DataFrame para o banco de dados PostgreSQL
df.to_sql("professores", engine, if_exists="append", index=False)
