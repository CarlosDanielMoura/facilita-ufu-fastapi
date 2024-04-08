import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta



url = 'http://www.editais.ufu.br/discente'
base_url = 'http://www.editais.ufu.br/discente?page='
try:
    html = pd.read_html(url)
except TypeError as e: 
    print(str(e))

dados = []

orgao = html[0]['Orgão Resp.']
titulo = html[0]['Título']
tipo = html[0]['Tipo']
data = html[0]['Data de Publicação']
resultado = html[0]['Result. do Edital']


html2 = requests.get(url)
soup = BeautifulSoup(html2.content, 'html.parser')

link = []

if(html2.status_code==200):

    ret = soup.find("table", class_="views-table")

    links_paginas = ret.find_all("a")


    for i in range(0,5):
        del links_paginas[0]

    for links in links_paginas:
         l="http://www.editais.ufu.br"+links.get("href")
         link.append(l)
   
for i in  range(orgao.count()):
    dados.append(
        {
            'orgao_responsavel': orgao[i],
            'titulo': titulo[i],
            'link': link[i],
            'tipo':  tipo[i],
            'data_publicacao': data[i],
            'resultado': resultado[i]
        }
    )




df = pd.DataFrame({'Orgao Responsável':orgao, 'Título':titulo, 'Link': link, 'Tipo':tipo, 'Data de Publicação':data, 'Resultado': resultado})

for pagina in range(1, 59):

    url = base_url + str(pagina)
    html = pd.read_html(url)
    
    try:
        html = pd.read_html(url)
    except TypeError as e: 
        print(str(e))
    
    org = html[0]['Orgão Resp.']
    tit = html[0]['Título']
    tip = html[0]['Tipo']
    dat = html[0]['Data de Publicação']
    res = html[0]['Result. do Edital']
    
    html2 = requests.get(url)
    soup = BeautifulSoup(html2.content, 'html.parser')
    
    if(html2.status_code==200):

        link2 = []

        ret = soup.find("table", class_="views-table")

        links_paginas = ret.find_all("a")


        for i in range(0,5):
            del links_paginas[0]

        for links in links_paginas:
             l="http://www.editais.ufu.br"+links.get("href")
             link2.append(l)
    
        df_2 = pd.DataFrame({'Orgao Responsável':org, 'Título':tit, 'Link': link2, 'Tipo':tip, 'Data de Publicação':dat, 'Resultado': res})
        df = pd.concat([df, df_2], ignore_index=True)

        
    for i in  range(org.count()):
        dados.append(
            {
                'orgao_responsavel': org[i],
                'titulo': tit[i],
                'link': link2[i],
                'tipo':  tip[i],
                'data_publicacao': dat[i],
                'resultado': res[i]
            }
        )
        
    data = df['Data de Publicação'].iloc[-1]
    d,y,a,b = data.split()
    # print(y)
    y = datetime.strptime(y, '%Y-%m-%d')
    current_date = datetime.today()
    past_date = current_date + relativedelta(years=-2)
    if(y<past_date):
        break


test = pd.DataFrame(dados)


test_remove = test.loc[(df['Resultado'] == 'Publicado')]

test = test.drop(test_remove.index)

test = test.drop(columns=['resultado'], axis=1)

test = test.reset_index(drop='true')

test.to_csv('edital_ufu.csv', index=False, encoding='utf-8-sig')


#######################################################################################################

## Conexão banco

import psycopg2
  
# connection establishment
conn = psycopg2.connect(
    user="postgres",
    password="123",
    host="localhost",
    port="5432",
    dbname="pds2"
)
  
conn.autocommit = True
  
# Creating a cursor object
cursor = conn.cursor()
  
# query to import data from given csv
with open('edital_ufu.csv', 'r', encoding='utf-8') as f:
    cursor.copy_expert(sql="COPY EDITAL(ORG_RESP,TITULO, LINK, TIPO, DT_PUBLICACAO) FROM STDIN WITH CSV HEADER", file=f)

# Display the table
cursor.execute('SELECT * FROM edital')
print(cursor.fetchall())

# Closing the connection
conn.close()





