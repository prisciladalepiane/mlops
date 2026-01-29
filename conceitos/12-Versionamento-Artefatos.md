# Versionamento dos Artefatos 

O versionamento de artefatos é uma prática usual em MLOps para garantir a rastreabilidade, reprodutibilidade e gerenciamento eficiente dos diferentes componentes de um projeto de Machine Learning. Os artefatos em um projeto de ML podem incluir datasets, modelos treinados, configurações de hiperparâmetros, scripts de treinamento, entre outros. 

Passos Para Realizar o Versionamento de Artefatos em MLOps:

## 1. Versionamento de Dados
**DVC (Data Version Control)**: DVC é uma ferramenta popular que integra com Git para versionar datasets. Ela permite rastrear versões de dados, pipelines de processamento e modelos.
Comandos Básicos:

```
dvc init
dvc add data/raw_dataset.csv
git add data/.gitignore data/raw_dataset.csv.dvc
git commit -m "Add raw dataset"
```

Delta Lake: Delta Lake, que roda em cima do Apache Spark, permite o versionamento de dados em grandes volumes, oferecendo ACID transactions e time travel para consultar versões anteriores dos dados.


## 2. Versionamento de Modelos
**MLflow**: MLflow é uma plataforma que oferece ferramentas para rastreamento e versionamento de experimentos, gerando um registro completo dos modelos treinados.

Comandos Básicos:

```python
import mlflow
with mlflow.start_run():
    mlflow.log_param("param1", value1)
    mlflow.log_metric("metric1", value1)
    mlflow.log_artifact("model.pkl")
```

**TensorFlow Model Registry:** Para projetos que usam TensorFlow, o TensorFlow Serving pode ser utilizado para versionar e servir modelos.

Comandos Básicos:

```python
import tensorflow as tf
tf.saved_model.save(model, "path/to/export_dir")
```

## 3. Versionamento de Código e Configurações
**Git**: Usar Git para versionar scripts de treinamento, pipelines e configurações de hiperparâmetros. Cada alteração no código ou nos parâmetros deve ser commitada no repositório Git.

Comandos Básicos:
```bash
git init
git add train.py
git commit -m "Add training script"
```

**Configuração de Hiperparâmetros**: Manter arquivos de configuração (por exemplo, YAML, JSON) versionados no Git para rastrear as diferentes configurações usadas nos experimentos.

## 4. Versionamento de Pipelines
**Kubeflow Pipelines**: Kubeflow Pipelines permite a criação e versionamento de pipelines completos de ML. Cada etapa do pipeline, incluindo preparação de dados, treinamento e validação, pode ser rastreada e versionada.

Comandos Básicos:

```python
import kfp
client = kfp.Client()
client.create_run_from_pipeline_func(pipeline_func, arguments)
```

## 5. Integração e Continuidade
CI/CD para ML: Utilizar ferramentas de CI/CD (Continuous Integration/Continuous Deployment) como Jenkins, GitLab CI, ou GitHub Actions para automatizar o versionamento e deployment de artefatos.


Exemplo de Workflow:

```
name: CI/CD for ML
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run training
      run: python train.py
    - name: Log artifacts
      run: |
        mlflow run . --no-conda
```

## Ferramentas Complementares
**Docker**: Usar Docker para criar contêineres que encapsulam o ambiente de execução, garantindo que o modelo e os scripts rodem de forma consistente em diferentes ambientes.


Comandos Básicos:

```
FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "train.py"]

​
docker build -t ml_model:latest .
docker run ml_model:latest
```
​
> Implementar uma estratégia de versionamento de artefatos em MLOps garante que todas as mudanças nos dados, modelos, códigos e pipelines sejam rastreadas de maneira eficaz, facilitando a reprodutibilidade e a manutenção dos projetos de Machine Learning.

## Controle de Versão e Repositório

Dentro de uma infraestrutura de features para MLOps, o controle de versão e o repositório de features visam garantir a reprodutibilidade e a rastreabilidade dos modelos.

O controle de versão é aplicado tanto aos dados de entrada quanto às features extraídas. Isso permite que qualquer transformação de dados, ajustes ou alterações nas features sejam documentados e versionados de forma adequada, garantindo que versões anteriores possam ser recuperadas para fins de auditoria ou reavaliação de modelos.

O repositório de features, geralmente chamado de Feature Store, atua como um sistema centralizado onde as features são armazenadas e compartilhadas entre equipes.

Cada feature é versionada com base em metadados, como o nome da feature, o tempo de criação e o histórico de transformações. Isso facilita o reuso de features em diferentes modelos e projetos, reduzindo o trabalho duplicado e assegurando consistência entre os experimentos.

O controle de versão também se estende ao pipeline de transformação de features. Ferramentas como **DVC (Data Version Control)** ou Git-LFS são comumente usadas para gerenciar os artefatos gerados durante o pré-processamento, enquanto frameworks como Feast possibilitam o versionamento e a gestão centralizada de features em ambientes de produção.

Com essas práticas, o sistema MLOps pode garantir uma integração fluida entre a criação de features, o monitoramento de mudanças e a rastreabilidade, essencial para a governança e manutenção de modelos em ambientes de produção.