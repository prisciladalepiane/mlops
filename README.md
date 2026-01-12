## MLOps e Ciclo de Vida de Modelos de Machine Learning

## 1 - MLOps Stack para otimização de hiperparâmetros com MLflow e Optuna

Este projeto implementa uma stack de MLOps para previsão de demanda baseada em um modelo de regressão **XGBoost**, integrando `Optuna` para otimização automática de hiperparâmetros e `MLflow` para rastreamento de experimentos, métricas, parâmetros, versões de modelos e artefatos. A solução parte de um conjunto de dados sintético com variáveis de contexto como clima, preço, promoções, feriados e histórico de demanda, realizando análise exploratória, visualizações de correlação, avaliação de resíduos e importância de variáveis. O pipeline inclui pré-processamento com `pandas` e `scikit-learn`, treinamento eficiente via `XGBoost DMatrix`, avaliação com **RMSE**, e uso de callbacks do Optuna para monitorar melhorias ao longo dos trials. O MLflow centraliza o gerenciamento do ciclo de vida do modelo, registrando o melhor experimento e salvando os artefatos necessários para inferência, caracterizando uma abordagem completa e reprodutível de MLOps orientada à otimização e governança de modelos.

📁 [01-Otimizacao-Hiperparametros](01-Otimizacao-Hiperparametros)

## 2 - Deploy de App para Análise de Ações em Tempo Real com Agentes de IA, Groq, DeepSeek e AWS 

Projeto de deploy de um aplicativo web para análise de mercado financeiro em tempo real, desenvolvido com `Streamlit`, que integra dados de mercado via Yahoo Finance, visualizações interativas com `Plotly` e um sistema de a**gentes de IA** colaborativos utilizando modelos **DeepSeek** e **LLaMA** executados via Groq. A aplicação permite ao usuário consultar ações da Nasdaq, visualizar séries históricas, gráficos de candlestick, volume e médias móveis, além de receber análises automatizadas, recomendações de analistas e notícias recentes obtidas por agentes especializados em finanças e busca na web. A solução é projetada para apoio a estratégias de day trade, com foco em desempenho, escalabilidade e futura operacionalização em infraestrutura AWS, combinando analytics, IA generativa e engenharia de deploy em um único produto.

📁 [02-Agente-IA-Financeiro](02-Agente-IA-Financeiro)

## 2 - Sistema LLM RAG

Projeto de MLOps de ponta a ponta para um sistema baseado em **LLM com arquitetura RAG**, que cobre todas as etapas desde a modelagem e ingestão de dados até a orquestração e execução automatizada do pipeline. A solução implementa a criação de um banco de dados relacional em PostgreSQL, com schemas e tabelas normalizadas para clientes, produtos e vendas, além de um pipeline de carga de dados via Python, usando `Pandas` e `SQLAlchemy`. A partir desses dados estruturados, são realizadas consultas analíticas agregadas, cujos resultados alimentam um modelo de linguagem executado localmente via `Ollama`, responsável por gerar insights textuais automatizados sobre padrões de vendas. Todo o fluxo é containerizado com Docker e executado de forma orquestrada por scripts Python, refletindo práticas de **engenharia de dados**, **LLMOps** e **MLOps**, com foco em reprodutibilidade, automação, governança e preparação para deploy em ambientes produtivos.

-----------------------------------------------------------------------------


# 🔗 Outros Projetos

Lista de repositórios externos.

## ⚙️ Machine Learning
- [machine-learning](https://github.com/prisciladalepiane/machine-learning): Estudos e projetos com redes neurais, fundamentos de arquiteturas profundas, treinamento, avaliação e experimentos aplicados.

## 🧠 Deep Learning
- [deep-learning](https://github.com/prisciladalepiane/deep-learning): Estudos e projetos com redes neurais, fundamentos de arquiteturas profundas, treinamento, avaliação e experimentos aplicados.

## 🔬 Ciência de Dados com Python

- [data_sci_py](https://github.com/prisciladalepiane/data_sci_py): Scripts e notebooks de estudos com Python, Pandas, Matplotlib, Scikit-Learn, etc.

## 🧪 Shiny e TCT

- [app_shiny_tct](https://github.com/prisciladalepiane/app_shiny_tct): Aplicativo Shiny para visualização de resultados em Teoria Clássica dos Testes (TCT) usando dados educacionais.

## 🗃️ Banco de Dados

- [banco_de_dados](https://github.com/prisciladalepiane/banco_de_dados): Modelagem e consultas SQL com foco em bancos relacionais. Inclui scripts de criação de tabelas e casos de uso.

## 📚 Artigo Teoria de Resposta ao Item

- [artigo-tri-latex](https://github.com/prisciladalepiane/artigo-tri-latex): Repositório da monografia sobre TRI, com código LaTeX e referências.

---

**Priscila Gonçalves Dalepiane**
Estatística | Engenharia de Software | Pós em Machine Learning e MLOps  

[LinkedIn](https://www.linkedin.com/in/priscila-gon%C3%A7alves-dalepiane-947b65b2/) | [Rpubs](https://rpubs.com/prisciladalepiane) | [GitHub](https://github.com/prisciladalepiane)