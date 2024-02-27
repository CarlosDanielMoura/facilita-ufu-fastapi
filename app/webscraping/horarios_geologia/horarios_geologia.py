import pdfplumber
import pandas as pd

horario = []
segunda = []
terca = []
quarta = []
quinta = []
sexta = []

with pdfplumber.open("geologia.pdf") as pdf:
    paginas = pdf.pages[:] 
    for pagina in paginas:
        tabela = pagina.extract_table()[1:]
        for linha in tabela:
            horario.append(linha[0])
            segunda.append(linha[1] if len(linha) > 1 else "")
            terca.append(linha[2] if len(linha) > 2 else "")
            quarta.append(linha[3] if len(linha) > 3 else "")
            quinta.append(linha[4] if len(linha) > 4 else "")
            sexta.append(linha[5] if len(linha) > 5 else "")

# Crie o DataFrame com as colunas "HORÁRIO", "SEGUNDA-FEIRA", "TERÇA-FEIRA", "QUARTA-FEIRA", "QUINTA-FEIRA" e "SEXTA-FEIRA"
df = pd.DataFrame({"HORÁRIO": horario, "SEGUNDA-FEIRA": segunda, "TERÇA-FEIRA": terca, "QUARTA-FEIRA": quarta, "QUINTA-FEIRA": quinta, "SEXTA-FEIRA": sexta})

# Substitua quebras de linha por espaços em todas as colunas do DataFrame
df = df.map(lambda x: x.replace('\n', ' ') if isinstance(x, str) else x)

# Salve o DataFrame em um arquivo CSV
df.to_csv('horarios.csv', index=False, encoding = 'utf-8')
# Salve o DataFrame em um arquivo XLSX
df.to_excel("horariosGeo.xlsx")

# Exiba o DataFrame resultante
print(df)


