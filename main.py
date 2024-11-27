import requests
from bs4 import BeautifulSoup

# URLs dos empreendimentos
urls = [
    "https://lbin.com.br/empreendimentos/agora825/",
    "https://lbin.com.br/empreendimentos/mediterranee/",
    "https://lbin.com.br/empreendimentos/fitroomtapajos/"
]

# Cabeçalhos para simular uma requisição de navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Função para extrair informações do empreendimento
def scrape_lbin_info(url):
    response = requests.get(url, headers=headers)  # Inclui os cabeçalhos na requisição
    soup = BeautifulSoup(response.content, "html.parser")

    # Extração de informações principais
    data = {
        "nome": soup.find("h1").text.strip() if soup.find("h1") else None,
        "descricao": soup.find("div", class_="content").text.strip() if soup.find("div", class_="content") else None,
        "detalhes": {}
    }
    
    # Extração de detalhes (ajuste o seletor conforme a estrutura do site)
    detalhes_section = soup.find("div", class_="details")  # Exemplo de classe
    if detalhes_section:
        for item in detalhes_section.find_all("li"):
            key_value = item.text.strip().split(":")
            if len(key_value) == 2:
                key, value = key_value
                data["detalhes"][key.strip()] = value.strip()

    return data

# Extraindo dados de cada URL
for url in urls:
    info = scrape_lbin_info(url)
    print(f"Dados do empreendimento ({url}):\n", info)
    print("\n" + "-"*50 + "\n")
