## MLOps e Ciclo de Vida de Modelos de Machine Learning

## 1 - MLOps Stack para otimização de hiperparâmetros com MLflow e Optuna

Este projeto implementa uma stack de MLOps para previsão de demanda baseada em um modelo de regressão **XGBoost**, integrando `Optuna` para otimização automática de hiperparâmetros e `MLflow` para rastreamento de experimentos, métricas, parâmetros, versões de modelos e artefatos. A solução parte de um conjunto de dados sintético com variáveis de contexto como clima, preço, promoções, feriados e histórico de demanda, realizando análise exploratória, visualizações de correlação, avaliação de resíduos e importância de variáveis. O pipeline inclui pré-processamento com `pandas` e `scikit-learn`, treinamento eficiente via `XGBoost DMatrix`, avaliação com **RMSE**, e uso de callbacks do Optuna para monitorar melhorias ao longo dos trials. O MLflow centraliza o gerenciamento do ciclo de vida do modelo, registrando o melhor experimento e salvando os artefatos necessários para inferência, caracterizando uma abordagem completa e reprodutível de MLOps orientada à otimização e governança de modelos.

📁 [01-Otimizacao-Hiperparametros](01-Otimizacao-Hiperparametros)

# 2 - Deploy de App para Análise de Ações em Tempo Real com Agentes de IA, Groq, DeepSeek e AWS 

Projeto de deploy de um aplicativo web para análise de mercado financeiro em tempo real, desenvolvido com `Streamlit`, que integra dados de mercado via Yahoo Finance, visualizações interativas com `Plotly` e um sistema de a**gentes de IA** colaborativos utilizando modelos **DeepSeek** e **LLaMA** executados via Groq. A aplicação permite ao usuário consultar ações da Nasdaq, visualizar séries históricas, gráficos de candlestick, volume e médias móveis, além de receber análises automatizadas, recomendações de analistas e notícias recentes obtidas por agentes especializados em finanças e busca na web. A solução é projetada para apoio a estratégias de day trade, com foco em desempenho, escalabilidade e futura operacionalização em infraestrutura AWS, combinando analytics, IA generativa e engenharia de deploy em um único produto.

📁 [02-Agente-IA-Financeiro](02-Agente-IA-Financeiro)