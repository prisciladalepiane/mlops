# DOCKER

Docker é uma plataforma que permite criar, empacotar e executar aplicações em ambientes isolados chamados containers.

Documentação: https://docs.docker.com/get-started/get-docker/

## Explorando a Interface:

### _Images_ (Imagem)

Uma **imagem Docker** é um pacote imutável que reúne tudo o que uma aplicação precisa para rodar: sistema base, dependências, bibliotecas, arquivos e configurações. Ela funciona como uma receita pronta: a partir dela o Docker cria containers, que são instâncias em execução dessa imagem. Como a imagem não muda, ela garante que o software rode sempre da mesma forma em qualquer ambiente, seja no seu computador, em um servidor ou na nuvem.

As imagens Docker ficam armazenadas em registries, que são repositórios próprios para distribuir imagens. O mais comum é o [**Docker Hub**](hub.docker.com), que é público e gratuito para a maioria dos usos. Lá encontra-se imagens oficiais como python, ubuntu, postgres e também imagens criadas pela comunidade.
Além do Docker Hub, existem registries privados e de nuvem como GitHub Container Registry, AWS ECR, Google Artifact Registry e Azure Container Registry, onde empresas e desenvolvedores guardam suas próprias imagens. Você também pode criar suas imagens localmente e listá-las com o comando `docker images`.

### _Conteiners_
Um container é um ambiente isolado onde uma aplicação roda com tudo o que ela precisa, sem interferir no sistema operacional principal e sem depender do que está instalado na máquina. Ele é criado a partir de uma imagem e funciona como uma instância leve e rápida, oferecendo isolamento de dependências, reprodutibilidade e portabilidade. Em prática, um container garante que a aplicação rode exatamente igual em qualquer lugar, seja no seu computador, em um servidor ou na nuvem. É por isso que containers são usados em desenvolvimento, deploy, MLOps e microserviços.

### _Builds_

É o processo de **construir uma imagem** a partir de um Dockerfile. Quando você faz um build, o Docker lê cada instrução do Dockerfile, cria as camadas, instala dependências, copia arquivos e monta o ambiente final que será usado nos containers. Em resumo, o build transforma o Dockerfile em uma imagem pronta para rodar.

## Mesmo Container x Container Diferente

### 1. Mesmo container Docker

**Vantagens**:

- Menor overhead de comunicação: Como tudo está em um mesmo container, as operações internas (entre os bancos de dados ou serviços) são mais rápidas, evitando a latência de rede que ocorre entre containers separados.
- Facilidade de gerenciamento: Manter tudo no mesmo container é mais simples, pois você só precisa orquestrar e gerenciar um container, facilitando deploy e manutenção.•Consumo reduzido de recursos: Menos containers significam menos overhead do sistema, como memória e CPU alocados para a infraestrutura do Docker.
- Tempo de inicialização mais rápido: Inicializar um único container tende a ser mais rápido do que inicializar vários.

**Desvantagens**:

- Dificuldade de escalabilidade: Caso você precise escalar um banco específico ou serviço, será necessário escalar o container inteiro, mesmo que apenas uma parte do sistema esteja sobrecarregada.
- Maior acoplamento: Componentes dentro de um mesmo container tendem a ser mais dependentes entre si. Uma falha em um banco pode afetar outros bancos ou o serviço como um todo.•Complexidade no isolamento: Se você precisar de diferentes configurações (versões ou tipos de bancos), o mesmo container pode se tornar complexo e difícil de manter.
- Risco de segurança: Compartilhar o mesmo container pode facilitar que um componente comprometido afete os demais serviços ou bancos de dados.

**Consequências**:
- Menor latência, mas menos flexibilidade para upgrades, escalabilidade e gerenciamento de falhas.
- Pode ser crítico caso um problema em um banco de dados se propague para outros, impactando todo o sistema.

### 2. Containers diferentes

**Vantagens**:

- Melhor isolamento: Cada banco de dados ou serviço roda em seu próprio container, evitando que falhas em um afetem os demais.
- Escalabilidade independente: É possível escalar cada banco de dados separadamente, alocando mais recursos apenas para o container que estiver sobrecarregado.
- Facilidade de manutenção: Atualizar ou modificar configurações de um banco de dados não afeta outros serviços.
- Maior flexibilidade: Permite usar diferentes tecnologias ou versões para bancos de dados, sem conflito.- Segurança aprimorada: Containers isolados oferecem maior segurança, limitando os danos caso um banco ou serviço seja comprometido.

**Desvantagens**:

Aumento da latência: A comunicação entre containers pode introduzir uma pequena latência devido ao uso de rede interna do Docker.
- Maior consumo de recursos: Cada container possui seu próprio overhead de infraestrutura (CPU, memória), o que pode aumentar os custos.
- Complexidade na orquestração: Gerenciar múltiplos containers exige ferramentas adicionais (como Docker Compose ou Kubernetes) e pode aumentar a complexidade de deployment e monitoramento.
- Tempo de inicialização: Inicializar vários containers pode ser mais demorado, especialmente em sistemas com muitos bancos de dados.

**Consequências**:
- Maior flexibilidade e robustez, mas potencialmente maior latência e maior uso de recursos.
- Essencial se o projeto exigir escalabilidade, segurança e isolamento entre bancos de dados.