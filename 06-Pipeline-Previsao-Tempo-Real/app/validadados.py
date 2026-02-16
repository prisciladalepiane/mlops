# Importa a classe BaseModel para a validação de dados
from pydantic import BaseModel

# Valida a classe de dados que serão usadas na API
class InputData(BaseModel):
    
    # Define atributos de entrada como um número de ponto flutuante
    feature1: float
    feature2: float
    feature3: float
