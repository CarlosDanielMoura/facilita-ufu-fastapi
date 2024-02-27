import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://www.editais.ufu.br/discente'
base_url = 'http://www.editais.ufu.br/discente?page='
try:
    html = pd.read_html(url)
except TypeError as e: 
    print(str(e))


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

df_remove = df.loc[(df['Resultado'] == 'Publicado')]

df = df.drop(df_remove.index)

df.drop(columns=['Resultado'])

df = df.reset_index(drop='true')

df.to_csv('editais_ufu.csv', index=False, encoding='utf-8')
df.to_excel("editais.xlsx")





