# Sistema de recomendação

Um Sistema de Recomendação é uma aplicação de Machine Learning que sugere itens relevantes a usuários com base em seus comportamentos passados, preferências, ou características. Esses sistemas são amplamente utilizados em plataformas como streaming de mídia, e-commerce e redes sociais. Eles podem ser baseados em abordagens como filtragem colaborativa, filtragem baseada em conteúdo ou modelos híbridos.

## Explicação da amostra de dados

Os dados de exemplo usado no projeto deste capítulo fornecem informações essenciais para a construção de um sistema de recomendação. Cada linha representa uma interação entre um usuário e um item, com as seguintes colunas:

- **date**: Data em que a interação ocorreu, no formato AAAA-MM-DD. Útil para análises temporais, como mudanças nas preferências ao longo do tempo.

- **user_id**: Identificador único do usuário. Representa quem realizou a interação.

- **item_id**: Identificador único do item (como um produto, filme ou música). Representa o que foi avaliado pelo usuário.

- **rating**: Avaliação numérica atribuída pelo usuário ao item, geralmente em uma escala contínua ou discreta. Indica o grau de satisfação ou preferência do usuário em relação ao item.

## Algoritmo ALS 

https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.recommendation.ALS.html

O algoritmo ALS (Alternating Least Squares) no MLLib é utilizado para resolver problemas de recomendação, como sistemas de recomendação de filmes, músicas ou produtos. Ele é especialmente eficaz em cenários com dados esparsos, onde muitas interações entre usuários e itens não estão registradas.

O ALS funciona modelando as preferências dos usuários e as características dos itens em um espaço de fatores latentes. A ideia principal é decompor a matriz de interações (como avaliações de usuários para itens) em duas matrizes menores: uma representando os usuários e outra os itens. Essas matrizes menores capturam os padrões latentes nas interações, permitindo prever valores desconhecidos.

A abordagem alterna entre otimizar as representações dos usuários e dos itens. Primeiro, mantém-se fixas as características dos itens para atualizar as representações dos usuários, minimizando o erro quadrático entre as avaliações conhecidas e as predições. Em seguida, as representações dos usuários são fixadas para ajustar as características dos itens. Esse processo continua de forma iterativa até que o modelo consiga convergir ou atinja o número máximo de iterações.

ALS é robusto para lidar com dados esparsos porque se concentra apenas nas interações observadas, ignorando as ausentes. O MLLib do Spark implementa uma versão eficiente do ALS que pode ser paralelizada, permitindo processar grandes volumes de dados em clusters distribuídos. Ele também suporta regularização para evitar overfitting e oferece a possibilidade de trabalhar com diferentes esquemas de ponderação para lidar com a confiabilidade das interações observadas.

## Métrica de Avaliação - RMSE

O RMSE (Root Mean Squared Error) é uma métrica amplamente utilizada para avaliar a precisão de modelos preditivos, especialmente em problemas de regressão e recomendação. Ele mede a diferença entre os valores previstos pelo modelo e os valores reais observados, oferecendo uma visão quantitativa do erro médio cometido.

Para calcular o RMSE, começa-se determinando o erro de cada previsão, ou seja, a diferença entre o valor previsto e o valor real. Esses erros são elevados ao quadrado para eliminar valores negativos e penalizar desvios maiores. Em seguida, calcula-se a média desses erros quadrados. Por fim, extrai-se a raiz quadrada dessa média para trazer o resultado para a mesma escala dos dados originais, facilitando sua interpretação.

O RMSE é especialmente útil porque dá maior peso a erros grandes, tornando-o sensível a outliers. Isso é vantajoso em muitos contextos, mas pode ser uma limitação caso os dados contenham muitos valores extremos não representativos. Um RMSE menor indica um modelo mais preciso, mas ele deve ser analisado em conjunto com o contexto do problema, incluindo a escala dos dados.

Em sistemas de recomendação, como os que utilizam o algoritmo ALS, o RMSE é comumente empregado para avaliar a qualidade das predições das avaliações de usuários. Ele ajuda a comparar diferentes configurações ou modelos, auxiliando na escolha da abordagem que melhor representa as preferências dos usuários.