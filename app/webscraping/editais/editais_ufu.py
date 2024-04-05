import pandas as pd
import requests
from bs4 import BeautifulSoup
import schedule
import time

def web_scraping_and_update():
    url = 'http://www.editais.ufu.br/discente'
    base_url = 'http://www.editais.ufu.br/discente?page='

    # Dataframe vazio para armazenar os dados
    df = pd.DataFrame(columns=['Orgao Responsável', 'Título', 'Link', 'Tipo', 'Data de Publicação', 'Resultado'])

    for pagina in range(1, 59):
        try:
            html = pd.read_html(base_url + str(pagina))
        except TypeError as e: 
            print(str(e))
            continue

        org = html[0]['Orgão Resp.']
        tit = html[0]['Título']
        tip = html[0]['Tipo']
        dat = html[0]['Data de Publicação']
        res = html[0]['Result. do Edital']

        html2 = requests.get(url)
        soup = BeautifulSoup(html2.content, 'html.parser')
        

        if(html2.status_code == 200):
            link = []
            ret = soup.find("table", class_="views-table")
            links_paginas = ret.find_all("a")

            for i in range(0, 5):
                del links_paginas[0]

            for links in links_paginas:
                l = "http://www.editais.ufu.br" + links.get("href")
                link.append(l)

            df_2 = pd.DataFrame({'Orgao Responsável': org, 'Título': tit, 'Link': link, 'Tipo': tip, 'Data de Publicação': dat, 'Resultado': res})
            df = pd.concat([df, df_2], ignore_index=True)

    # Fazer a manipulação necessária dos dados aqui, por exemplo, remover linhas com 'Resultado' igual a 'Publicado'
    df_remove = df.loc[(df['Resultado'] == 'Publicado')]
    df = df.drop(df_remove.index)
    df = df.drop(columns=['Resultado'])
    df = df.reset_index(drop='true')

    # Atualizar o banco de dados
    # conn = sqlite3.connect('editais.db')
    # df.to_sql('editais_ufu', conn, if_exists='replace', index=False)
    # conn.close()

    print("Dados atualizados com sucesso.")

    df.to_csv('editais_ufu.csv', index=False, encoding='utf-8')
    df.to_excel("editais.xlsx")

# Agendar a tarefa para ser executada a cada intervalo de tempo
schedule.every(1).hour.do(web_scraping_and_update)  # Ajuste o intervalo conforme necessário (1 hora neste exemplo)

# Loop para manter o programa em execução
while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto se há tarefas agendadas para serem executadas