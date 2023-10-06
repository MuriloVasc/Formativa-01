import pandas as pd
import requests
from bs4 import BeautifulSoup

link = 'https://caroladeia.github.io/Forncar/#'
response = requests.get(link)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)

site = BeautifulSoup(requisicao.text, 'html.parser')
tables = site.find_all('table')
print(tables)

for i, table in enumerate(tables):
    df = pd.read_html(str(table))
    df[0].to_excel(f'tabela_{i}.xlsx', index=False)