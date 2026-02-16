# Imports
import pandas as pd
from fastapi import FastAPI
from app.modelo import InputData
from app.utils import carrega_modelo_e_metadados

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define uma rota para previsão
@app.post("/predict")
def predict(input_data: InputData):

    model, metadata = carrega_modelo_e_metadados()
    
    if model is None:

        return {"error": "Nenhum modelo treinado disponível"}
    
    X = pd.DataFrame([[input_data.feature1, input_data.feature2, input_data.feature3]], 
                     columns = ["feature1", "feature2", "feature3"])
    
    prediction = model.predict(X)[0]
    
    return {"Previsão": prediction, 
            "Versão do Modelo": metadata["version"], 
            "Versão do Scikit-Learn": metadata["scikit_learn_version"], 
            "Coeficiente R2 em Treino": metadata["r2_train"]}