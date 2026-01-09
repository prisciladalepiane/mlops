## MLOps e Ciclo de Vida de Modelos de Machine Learning


## 1 - MLOps Stack para otimização de hiperparâmetros com MLflow e Optuna

Este projeto implementa uma stack de MLOps para previsão de demanda baseada em um modelo de regressão **XGBoost**, integrando `Optuna` para otimização automática de hiperparâmetros e `MLflow` para rastreamento de experimentos, métricas, parâmetros, versões de modelos e artefatos. A solução parte de um conjunto de dados sintético com variáveis de contexto como clima, preço, promoções, feriados e histórico de demanda, realizando análise exploratória, visualizações de correlação, avaliação de resíduos e importância de variáveis. O pipeline inclui pré-processamento com `pandas` e `scikit-learn`, treinamento eficiente via `XGBoost DMatrix`, avaliação com **RMSE**, e uso de callbacks do Optuna para monitorar melhorias ao longo dos trials. O MLflow centraliza o gerenciamento do ciclo de vida do modelo, registrando o melhor experimento e salvando os artefatos necessários para inferência, caracterizando uma abordagem completa e reprodutível de MLOps orientada à otimização e governança de modelos.

📁 [01-Otimizacao-Hiperparametros](01-Otimizacao-Hiperparametros)
