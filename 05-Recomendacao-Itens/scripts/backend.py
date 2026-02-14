# Módulo de Treinamento do Modelo com PySpark 

# Imports
import os                                         
import shutil                                          # remover diretórios e arquivos
from pyspark.sql import SparkSession                   # inicializar uma sessão do Spark
from pyspark.ml.recommendation import ALS              # Algoritmo ALS para recomendação
from pyspark.ml.evaluation import RegressionEvaluator  # Avaliação do modelo

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"

def treina_modelo():
    
    # Inicializa uma sessão Spark com configurações para localhost
    spark = SparkSession.builder \
        .appName("ProjetoRecomendacao") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .config("spark.driver.host", "127.0.0.1") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    ratings = spark.read.csv('dados/dataset.csv', header=True, inferSchema=True)

    ratings = ratings.drop('date')

    (training, test) = ratings.randomSplit([0.8, 0.2])

    # Configura o modelo ALS (Alternating Least Squares) com parâmetros específicos
    als = ALS(maxIter=10,                # Número máximo de iterações
              regParam=0.1,              # Parâmetro de regularização
              userCol="user_id",         # Coluna que representa os IDs de usuários
              itemCol="item_id",         # Coluna que representa os IDs de itens
              ratingCol="rating",        # Coluna que representa as avaliações
              coldStartStrategy="drop")  # Lida com valores ausentes

    # Treina o modelo ALS usando o conjunto de treinamento
    modelo = als.fit(training)

    # Faz previsões no conjunto de teste
    predictions = modelo.transform(test)

    # Inicializa um avaliador para calcular o erro médio quadrático (RMSE)
    evaluator = RegressionEvaluator(metricName="rmse",           # Métrica de avaliação
                                    labelCol="rating",           # Coluna real
                                    predictionCol="prediction")  # Coluna prevista
    
    # Avalia o modelo e calcula o RMSE
    rmse = evaluator.evaluate(predictions)
    
    # Exibe o RMSE do modelo treinado
    print(f"RMSE = {rmse}")

    # Cria o diretório se não existir
    if not os.path.exists('modelos'):
        os.makedirs('modelos')

    model_path = "modelos/modelo_v1"

    # Remove o diretório do modelo, se já existir
    if os.path.exists(model_path):
        shutil.rmtree(model_path)

    # Salva o modelo 
    modelo.save(model_path)
    print(f"Modelo salvo em '{model_path}'.")

    spark.stop() # Encerra a sessão Spark

if __name__ == "__main__":
    treina_modelo()