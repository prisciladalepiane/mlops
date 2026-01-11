# Deploy de App Para Day Trade Analytics em Tempo Real com Agentes de IA, Groq, DeepSeek e AWS 

Projeto de deploy de um aplicativo web para análise de mercado financeiro em tempo real, desenvolvido com `Streamlit`, que integra dados de mercado via Yahoo Finance, visualizações interativas com `Plotly` e um sistema de a**gentes de IA** colaborativos utilizando modelos **DeepSeek** e **LLaMA** executados via Groq. A aplicação permite ao usuário consultar ações da Nasdaq, visualizar séries históricas, gráficos de candlestick, volume e médias móveis, além de receber análises automatizadas, recomendações de analistas e notícias recentes obtidas por agentes especializados em finanças e busca na web. A solução é projetada para apoio a estratégias de day trade, com foco em desempenho, escalabilidade e futura operacionalização em infraestrutura AWS, combinando analytics, IA generativa e engenharia de deploy em um único produto.

## Execução Local 

Instale o Anaconda Python no seu computador. Links de download para instalação:

https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Windows-x86_64.exe (Windows)
https://repo.anaconda.com/archive/Anaconda3-2024.10-1-MacOSX-arm64.pkg   (MacOS Apple Silicon)
https://repo.anaconda.com/archive/Anaconda3-2024.10-1-MacOSX-x86_64.pkg  (MacOS Intel)
https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh    (Qualquer Distribuição Linux)

Abra o terminal ou prompt de comando, navegue até a pasta com os arquivos e execute o comando abaixo para criar um ambiente virtual:

```bash
conda create --name mlopsp2 python=3.12
```

Ative o ambiente:

```bash
conda activate mlopsp2 (ou: source activate mlopsp2)
```

Instale o pip e as dependências:

```bash
conda install pip
pip install -r requirements.txt 
```

Execute o comando abaixo e acesse a app pelo navegador.

```bash
python -m streamlit run app.py
```
 Use os comandos abaixo para desativar o ambiente virtual e remover o ambiente (opcional):

```bash
conda deactivate
conda remove --name mlopsp2 --all
```


## Execução na AWS

Crie uma instância EC2 da camada gratuita AWS.

Acesse a instância pelo terminal

Faça o download do Miniconda (Anaconda é muito pesado para a instância EC2 gratuita) com o comando abaixo:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Crie a pasta app e copie os arquivos 

Execute o comando abaixo:

```bash
pip install -r requirements.txt 
```

Inicie a app com um dos comandos abaixo:

```bash
streamlit run app.py
nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &
```

Acesse a app pelo navegador.

Nota: Quando terminar seus testes, desligue a instância EC2.