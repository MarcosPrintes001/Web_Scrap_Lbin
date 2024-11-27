# Web Scraping Lbin Imobiliária

Este projeto realiza a extração de informações de empreendimentos imobiliários do site da Lbin utilizando web scraping com Python. As informações extraídas são relacionadas a empreendimentos, como nome, descrição e detalhes como tamanho e número de unidades.

## Funcionalidades

- Extrai informações de vários empreendimentos no site da Lbin.
- Coleta dados como:
  - Nome do empreendimento
  - Descrição do empreendimento
  - Detalhes (exemplo: tamanho, número de unidades, etc.)
- Limpeza e formatação do texto para remoção de espaços extras e quebras de linha.

## Pré-requisitos

Antes de rodar o projeto, você precisa instalar as dependências:

```bash
pip install requests beautifulsoup4
```

## Como Usar

1. Clone este repositório para o seu ambiente local:

```bash
git clone https://https://github.com/MarcosPrintes001/Web_Scrap_Lbin.git

2. Navegue até o diretório do projeto:
```bash
cd web_scrapp_lbin
```

3. Execute o script Python para iniciar o scraping:
```bash
python main.py
```

O script irá fazer a requisição para os sites de empreendimentos e exibir as informações extraídas

## Estrutura do Código

- **`main.py`**: Script principal onde o scraping é realizado.
- **Funções**:
  - `scrape_lbin_info(url)`: Realiza o scraping para uma URL específica.
  - `clean_text(text)`: Limpa o texto removendo excessos de espaços e quebras de linha.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
