import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from app.utils import salva_modelo_e_metadados

# Função principal para treinar o modelo
def treina_modelo(data_path = "dados/dataset.csv"):
    
    # Carrega os dados de um arquivo CSV
    df = pd.read_csv(data_path)
    
    # Separa as features (X) do target (y)
    X = df.drop("target", axis = 1)
    y = df["target"]
    
    # Divide os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    
    # Instancia o modelo de regressão linear
    modelo = LinearRegression()
    
    # Treina o modelo com os dados de treino
    modelo.fit(X_train, y_train)
    
    # Salva o modelo treinado e seus metadados, retornando a versão do modelo
    version = salva_modelo_e_metadados(modelo, X_train, y_train)
    
    # Exibe a versão do modelo treinado
    print(f"\nModelo treinado e salvo com versão {version}\n")

# Executa a função de treinamento caso o script seja executado diretamente
if __name__ == "__main__":
    treina_modelo()