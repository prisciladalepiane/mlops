# Construindo e Operacionalizando Pipeline de Inferência com Frontend, Backend e API

## Descrição

Projeto que implementa um sistema de recomendação utilizando PySpark para treinamento do modelo, FastAPI para servir a API e Streamlit para a interface web.

## Estrutura

- **dados/**: Dados históricos.
- **modelos/**: Modelo treinado.
- **scripts/**: Scripts Python.
  - **backend.py**: Treina o modelo de recomendação.
  - **api.py**: API para servir o modelo.
  - **frontend.py**: Aplicação web com Streamlit.
- **requirements.txt**: Dependências do projeto.

## Instalação

Crie um ambiente virtual:

```
python -m venv venv5
```

Ative o ambiente virtual:

Windows:
```
venv5\Scripts\activate
```

MacOS/Linux:

```
source venv5/bin/activate
```

Execute as instruções abaixo:

```bash
pip install --upgrade pip

pip install --upgrade cmake 

pip install -r requirements.txt

```

```
python scripts/backend.py
```


Abra outro terminal ou prompt de comando, navegue até a pasta com os arquivos, ative o venv5 e execute:

```bash
python scripts/api.py
```

Abra outro terminal ou prompt de comando, navegue até a pasta com os arquivos, ative o venv5 e execute:

```bash
streamlit run scripts/frontend.py
```