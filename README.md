
# APLICAÇÃO PRÁTICA DE TECNOLOGIAS DE BANCO DE DADOS E BIG DATA EM UMA EMPRESA DE COMÉRCIO ELETRÔNICO

### Introdução

A E-Shop Brasil é uma plataforma de comércio eletrônico, oferecendo uma ampla gama de produtos de eletrônicos a itens de moda, e atendendo milhões de clientes em todo o território brasileiro. Com um crescimento significativo desde sua fundação em 2010, a empresa recentemente enfrenta desafios cada vez mais complexos, especialmente relacionados à gestão de dados e à logística. Atualmente, a plataforma processa cerca de 100 mil pedidos diariamente, gerando um volume de informações que precisam ser armazenadas, processadas e analisadas de maneira eficaz.

O aumento do número de transações, junatamente à necessidade de personalização da experiência do cliente impõe a adoção de soluções tecnológicas que garantam não apenas a segurança e a privacidade dos dados, como também a capacidade de análise. Além disso, a diversidade geográfica do Brasil representa um desafio logístico para garantir entregas dentro do prazo e com o menor custo possível em regiões remotas.

Diante desse cenário, este projeto propõe o desenvolvimento de uma solução tecnológica baseada em bancos de dados NoSQL, com foco no uso do MongoDB, integrada a uma interface gráfica desenvolvida com Streamlit. A proposta visa demonstrar, de forma prática, como tecnologias de Big Data e bancos não relacionais podem ser aplicadas para otimizar o gerenciamento de informações, melhorar a personalização da experiência do usuário e apoiar a tomada de decisões nas áreas de vendas, marketing e operações.

O principal objetivo é criar um ambiente escalável, seguro e eficiente, capaz de realizar operações de inserção, manipulação e consulta de dados, oferecendo uma visão clara sobre como essas tecnologias podem contribuir para resolver problemas reais enfrentados pela empresa ficticia E-Shop Brasil.

## Integrando a Big Data

Visando atender aos objetivos de escalabilidade, análise avançada e processamento de grandes volumes de dados, o projeto inclui tecnologias de Big Data básicos, que servem como exemplos de como a empresa E-Shop Brasil poderia aplicar tais tecnologias em seu banco de dados. Os exemplos utilizados neste trabalho podem ser aplicados de forma unida em busca de fornecer suporte completo a big data:

***• Apache Spark***: Para o processamento e a análise distribuída de grandes conjuntos de dados armazenados no MongoDB, permitindo insights mais rápidos e complexos sobre padrões de compra e comportamento dos clientes. Em contrapartida, o uso dessa ferramenta pode acarretar em um****************************** alto consumo de recursos e uma alta complexidade no seu gerenciamento.

***• MinIO (Data Lake)***: Implementado para o armazenamento de grandes volumes de dados históricos, com fácil integração a futuros projetos de Machine Learning e Business Intelligence. Contudo, por possuir uma alta complexidade e falta de funcionalidades avançadas, seu sistema pode vir a ser confuso para pessoas não especializadas na sua utilização.

***• Apache Kafka***: Utilizado para transmissão em tempo real de eventos de venda, possibilitando a construção de análises dinâmicas e sistemas de monitoramento instantâneo. Esta ferramenta possui uma alta complexidade para sua configuração e apresenta dificuldades para permitir o acesso dos seus dados.

Essa arquitetura complementa o MongoDB e a aplicação em Streamlit, formando uma solução robusta, escalável e alinhada aos princípios de Big Data. Mesmo estas sendo as ferramentas mais comuns do mercado, todas apresentam seus próprios pontos fracos que exigem que diversas feramentas trabalhem juntas em busca de uma melhor integração dos dados da E-Shop Brasil.


## Passos Para a Implementação

Este projeto pode ser executado de duas formas: via docker-compose ou manualmente utilizando Dockerfile. A seguir, apresentamos ambas as opções:

1. Utilizando docker-compose (Recomendado)
O método mais prático para subir toda a infraestrutura é utilizando o arquivo docker-compose.yml, que define os serviços necessários (MongoDB e Streamlit).

```bash
# Na raiz do projeto, execute:
    docker-compose up -d
```
Este comando criará os containers e iniciará a aplicação. O MongoDB ficará disponível na porta padrão 27017, e a aplicação Streamlit pelo navegador. Os serviços implementados neste trabalho ficarão disponiveis, normalmente em:

Streamlit em http://localhost:8501

Mongo Express em http://localhost:8081

MinIO Console em http://localhost:9001

Spark Master em http://localhost:8080

2. Utilizando Dockerfile (manual)
Caso prefira construir manualmente o container da aplicação, é possivél a partir da utilizando dos seguintes comandos:

```bash
# Criação da imagem a partir do Dockerfile
    docker build -t streamlit-app .

# Execução do container da aplicação
    docker run -p 8501:8501 streamlit-app
```
Utilizando este comando, o MongoDB deve estar rodando separadamente, seja em outro container ou em uma instância local.

### Executando o Streamlit

Após subir a infraestrutura por meio do comando fornecido anteriormente, a aplicação pode ser acessada diretamente pelo navegador. No terminal, você também pode executar manualmente com o comando:
```bash
streamlit run app.py
```
Certifique-se de que o MongoDB está acessível e que os parâmetros de conexão estejam corretamente configurados no app.py.

**A aplicação Streamlit oferece as seguintes funcionalidades:**

**Inserção de Dados**, permitindo que o usuário insira novos registros em coleções específicas do MongoDB, como:

    • Cadastro de clientes
    • Registro de produtos
    • Inserção de pedidos

A interface contém formulários amigáveis que validam os dados antes do envio ao banco.

**Manipulação de Dados Existentes**, podendo executar comando como:

    • Edição: Os registros existentes podem ser atualizados diretamente pela interface,
     com visualização prévia dos dados.
    • Exclusão: Itens podem ser removidos permanentemente da base de dados com confirmação
     de segurança.

**Concatenação de Dados**, a aplicação permite combinar informações entre diferentes coleções. Por exemplo:

    • Unir dados de clientes e seus respectivos pedidos
    • Associar pedidos a produtos comprados

Essas operações são feitas utilizando consultas com operadores do MongoDB como $lookup, simulando joins em bancos relacionais.

**Consultas e Visualização**, os dados podem ser consultados e visualizados em tempo real por meio de:

    • Tabelas dinâmicas com paginação e ordenação
    • Filtros por campos (ex: busca por nome, ID, faixa de valor)
    • Gráficos interativos, se desejado, utilizando bibliotecas como plotly ou matplotlib
