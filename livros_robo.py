#HTTP
import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL base do site
URL = "http://books.toscrape.com/"

#Cabeçalho para evitar bloqueios
HEADERS = {"User-Agent": "Mozilla/5.0"}

#Coletando Dados
def coletar_dados():
    response = requests.get(URL, headers=HEADERS)

    if response.status_code != 200:
        print("Erro ao acessar o site")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Lista para armazenar os dados coletados
    livros = []

    # Encontrar todos os livros na página
    for livro in soup.find_all("article", class_="product_pod"):
        titulo = livro.h3.a["title"]
        preco = livro.find("p", class_="price_color").text.strip()

        livros.append({"Título": titulo, "Preço": preco})

    return livros

#Salvando em CSV
def salvar_csv(dados, arquivo="precos_books.csv"):
    df = pd.DataFrame(dados)
    df.to_csv(arquivo, index=False, encoding="utf-8")
    print(f"Dados salvos em {arquivo}")

#Executando
if __name__ == "__main__":
    livros_extraidos = coletar_dados()

    if livros_extraidos:
        salvar_csv(livros_extraidos)
        print("Coleta de preços concluída com sucesso!")

#Automatização
import schedule
import time

schedule.every().day.at("10:00").do(coletar_dados)

while True:
    schedule.run_pending()
    time.sleep(60)  # 1 minuto antes de rodar novamente