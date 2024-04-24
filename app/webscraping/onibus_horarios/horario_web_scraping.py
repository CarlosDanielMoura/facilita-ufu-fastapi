import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# Configuração do driver do Selenium
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e no PATH
url = "https://mcbusao.fly.dev/"
driver.get(url)

# Clicar no botão de filtro
filtro_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "hour"))
)
filtro_button.click()
filtro_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="1"]'))
)
filtro_button.click()

# Esperar que o conteúdo dinâmico seja carregado
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i-List")))
page_content = driver.page_source

# Parsear o conteúdo HTML com BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# Encontrar e extrair os dados desejados usando BeautifulSoup
conteudo_dinamico = soup.find("div", id="i-List-Content")

elements_spots = conteudo_dinamico.find_all("div", class_="c-List-Spots-Info")

# Estrutura para armazenar os dados
dados = []

# Extrair os textos dos elementos h2, h3 e h5 e armazenar na estrutura de dados
for spot_info in elements_spots:
    h2_text = (
        spot_info.find_previous_sibling("div", class_="c-List-Spots-Time")
        .find("h2")
        .text.strip()
    )
    h3_text = spot_info.find("h3").text.strip()
    h5_texts = [h5.text.strip() for h5 in spot_info.find_all("h5")]
    dados.append(
        {
            "horario_partida": h2_text,
            "ponto_saida": h3_text,
            "tipo_onibus": h5_texts[0],
            "destino": h5_texts[1],
        }
    )

# Fechar o navegador
driver.quit()

# Converter os dados para um DataFrame pandas
df = pd.DataFrame(dados)

# Conectar-se ao banco de dados PostgreSQL (substitua 'user', 'password', 'host' e 'database' pelas suas credenciais)
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Escrever o DataFrame para o banco de dados PostgreSQL
df.to_sql("horario_onibus", engine, if_exists="append", index=False)
