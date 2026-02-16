import json
import os
import pickle
from datetime import datetime
import sklearn

# Função para salvar o modelo e gerar metadados
def salva_modelo_e_metadados(model, X_train, y_train, model_dir = "modelo"):

    # Lista todos os arquivos de modelo no diretório especificado
    models = [f for f in os.listdir(model_dir) if f.startswith("modelo_v") and f.endswith(".pkl")]
    
    # Determina a próxima versão do modelo
    current_version = 1 if not models else max([int(m.split("_v")[-1].split(".pkl")[0]) for m in models]) + 1
    
    # Define os caminhos para os arquivos do modelo e dos metadados
    model_file = os.path.join(model_dir, f"modelo_v{current_version}.pkl")
    metadata_file = os.path.join(model_dir, f"metadados_v{current_version}.json")
    
    # Salva o modelo
    with open(model_file, "wb") as f:
        pickle.dump(model, f)
    
    # Calcula o coeficiente R² no conjunto de treino
    r2_train = model.score(X_train, y_train)
    
    # Gera os metadados
    metadata = {
        "version": current_version,
        "timestamp": datetime.now().isoformat(),
        "scikit_learn_version": sklearn.__version__,
        "r2_train": r2_train
    }
    
    # Salva os metadados 
    with open(metadata_file, "w") as f:
        json.dump(metadata, f)
    
    return current_version