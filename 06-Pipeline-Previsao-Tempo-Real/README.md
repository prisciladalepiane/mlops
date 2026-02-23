# Construindo e Operacionalizando Pipeline de Previsão em Tempo Real

1- Certifique-se de ter o Docker Desktop instalado e inicializado.

2- Abra um terminal ou prompt de comando, navegue até a pasta com os arquivos e execute o comando abaixo para criar a imagem Docker:

`docker compose build --no-cache`

3- No mesmo terminal ou prompt de comando, execute o comando abaixo para treinar o modelo e salvar os metadados:

`docker compose run --rm app python -m app.treino`

4- Agora abra OUTRO terminal ou prompt de comando, navegue até a pasta com os arquivos e execute o comando abaixo para iniciar o container da API:

`docker compose up --build`

5- Agora abra outro (o terceiro) terminal ou prompt de comando, navegue até a pasta com os arquivos e execute o comando abaixo para consumir a API:

`python cliente.py`




