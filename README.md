# Robô de Consulta de Preços - Books to Scrape

Este projeto é um web scraper que coleta preços de livros no site [Books to Scrape](http://books.toscrape.com/).  
Ele extrai o nome das obras e preços, no fim salva os dados em um arquivo CSV.

##  Tecnologias Utilizadas
- Python
- BeautifulSoup
- Requests
- Pandas

##  Como Usar
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/robo-consulta-precos.git
   cd robo-consulta-precos# Rob-de-Consulta-de-livros
   
2. Instale:
   ```sh
pip install -r requirements.txt

3. Execute o robô:
   ```sh
python main.py
O arquivo precos_books.csv será salvo na pasta data/.
