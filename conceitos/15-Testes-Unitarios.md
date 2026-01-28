# Construindo o Módulo de Testes Unitários

Testes unitários são uma técnica de verificação e validação de software usada para testar pequenas partes isoladas de um código, chamadas de "unidades", para garantir que funcionem corretamente. Cada unidade, que geralmente é uma função ou método em um programa, é testada de forma independente para validar se sua lógica interna está correta e produz o resultado esperado para diferentes entradas.

Características Principais dos Testes Unitários:

**Isolamento**: Testes unitários isolam uma parte específica do código para garantir que ela funcione conforme o esperado, sem depender de outras partes do sistema. Isso permite encontrar erros de forma rápida e precisa.

**Automatização**: Eles são geralmente escritos em conjunto com o código de produção e executados automaticamente, sem a necessidade de intervenção humana. Frameworks como JUnit (Java), pytest (Python), e unittest (Python) são comumente usados para automatizar os testes.

**Rapidez**: Testes unitários são rápidos porque testam apenas uma pequena parte do sistema e não envolvem interações com banco de dados, sistemas externos ou interface do usuário.

**Cobertura de Código**: Quando você cria testes unitários para cada função ou método do seu código, aumenta a cobertura dos testes, o que ajuda a identificar rapidamente quando novas mudanças quebram alguma funcionalidade já existente.

**Facilitam a Refatoração**: Uma vez que os testes garantem que o código atual funciona como esperado, é mais seguro modificar, melhorar ou refatorar o código sem introduzir novos bugs, já que os testes identificarão qualquer comportamento inesperado.

## unittest

O unittest é um módulo nativo do Python (biblioteca padrão) usado para criar e executar testes unitários automatizados, garantindo que partes do código (funções/classes) funcionem como esperado. Ele segue uma abordagem orientada a objetos: os testes são estruturados dentro de classes que herdam de unittest.TestCase, com métodos iniciando com test_. 

Exemplo:

```python
import unittest

# Função a ser testada
def soma(a, b):
    return a + b

# Classe de teste
class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)  # Verifica se 2+3 é 5

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```