
# Api-Favorite-Movies

*Back-end* do Projeto chamado **"*Favorite Movies*"**, cujo o objetivo é poder guardar os filmes favoritos.

Versão: 2.0

Esse projeto foi feito utilizando *Python*, com *Flask* sendo o *framework*, possuindo rotas para o *Front-End* em formato ***REST***, e recebendo informações de outros componentes, como a *API* Externa: https://www.omdbapi.com/ e o componente de dados.

Esse é um projeto feito por **Pedro Souza de Azevedo** como *MVP* para a disciplina de **Arquitetura de Software**, do curso de pós-graduação da ***PUC-Rio***.

O componente de dados desse projeto está aqui: https://github.com/Pedro-dev-083/MovieGraphQL

## Como configurar o projeto

### Clonagem do projeto:

Para clonar o projeto em sua máquina, é necessário ter o ***Git*** instalado, e então, você pode usar o seguinte comando:  

    git clone https://github.com/Pedro-dev-083/api-favorite-movies.git

Logo após ao clonar, você pode abrir a pasta, e acessar o terminal dentro dela para seguir os próximos passos.

### Dependência de dados:

O projeto utiliza de um componente externo encontrado nesse repositório: .
É necessário esse componente externo estar instalado na máquina via ***Docker*** para o perfeito funcionamento desse projeto.

### Variável de ambiente:
Esse projeto utiliza de uma *API* externa que possui uma chave secreta, logo na raiz você encontrará um arquivo de ambiente chamado ***.env***, que possivelmente estará assim:

    API_KEY=your_secret_key

 Para o seguimento do projeto você precisa preencher no lugar de ***your_secret_key***, uma chave, que você pode criar no site:
 https://www.omdbapi.com/ 
 Não se preocupe, é necessário apenas um cadastro, que é gratuito, para poder receber a chave e seguir com o projeto.

### Uso do *Docker*:

#### Instalação do *Docker*:
Quanto a execução do projeto, é necessário ter apenas o ***Docker*** instalado na sua máquina, que, caso não tenha, você pode seguir a documentação deles para poder instalar e utilizar em sua máquina.
Link para a documentação de ***Docker***: https://www.docker.com/

#### Ativar o *Docker*:
Para instalar o projeto em sua máquina é necessário primeiro ativar o *Docker*.
##### *Windows* e *Mac*:
Para *Windows* e *Mac*, você pode apenas abrindo o ***Docker Desktop***.
##### *Linux*:
Para *Linux*, você precisa rodar o seguinte comando no **Terminal**:

    sudo systemctl start docker

### Instalação e Execução do Projeto:
Logo após ativar o *Docker*, você deve abrir o terminal do seu sistema operacional na raiz do projeto, onde está localizado o ***Dockerfile***. Depois de estar aberto, você deve utilizar o seguinte comando para montar a imagem do projeto.

    docker build -t api-favorite-movies . 

Em primeira instância é normal demorar um pouco pois o projeto está sendo configurado pela primeira vez no seu *Docker*.
Após terminar de montar a imagem do projeto, você deve rodar o seguinte comando para montar o *container* a partir da imagem que foi criada:

    docker run -d -p 5000:5000 --name api-favorite-movies-container api-favorite-movies

Pronto, agora para garantir se o *container* foi criado e executado corretamente você pode executar um comando que verifica todos os *conteiners* ativos:

    docker ps

Caso tenha funcionado irá aparecer algo como:

    CONTAINER ID   IMAGE                 COMMAND           CREATED          STATUS          PORTS                    NAMES
    7c7a29a01045   api-favorite-movies   "python app.py"   31 seconds ago   Up 31 seconds   0.0.0.0:5000->5000/tcp   api-favorite-movies-container


  Depois, caso queira parar a execução do *container* você pode usar o seguinte comando:
  
    docker stop api-favorite-movies-container

E para ativar novamente, com o seguinte comando:

    docker start api-favorite-movies-container

Como o projeto foi montado pensando na porta 5000, você pode acessar com o *link* http://localhost:5000/ que irá para tela do *Swagger* com todas as rotas disponíveis.

### Comunicação entre containers
Com os dois containers ativos, você irá precisar criar uma rede *Docker* para poder seguir com o processo.
Para criar a rede é necessário o uso do comando:

    docker network create container-network
Logo após isso, precisará adicionar os dois containers a rede com os comandos:

    docker network connect container-network movie-graphql-container
    docker network connect container-network api-favorite-movies-container

## Utilizando o *Swagger*

Esse projeto foi desenvolvido usando ***OpenAPI***, tendo o *Swagger* como documentação. Com o projeto aberto, você pode acessar o ***localhost*** mais a porta utilizada na construção, ou seja acessando o http://localhost:5000/ .

Lá você irá encontrar todas as rotas que estão disponibilizadas para uso dentro desse projeto. Como por exemplo, a rota http://localhost:5000/moviesOnBase que irá retornar todos os filmes salvos no outro componente.

  

## Considerações Finais

Esse projeto foi utilizado apenas o *Python* com *Flask*, tendo como objetivo a construção de uma *API REST*, que pudesse se comunicar com outros componentes, como uma *API* Externa e outro componente externo criado por mim.

Utilizar *Python*, ainda continua um desafio pra mim, porém tem sido interessante aprender novas formas de utilizar ele, como o próprio caso de puxar uma *API* Externa por ele, e montar um *container* para ele. E a questão da comunicação com outro componente por *GraphQL* foi desafiador no começo, mas satisfatório após conseguir concluir esse ponto, pois pude tomar conhecimento dessa outra forma de comunicação.

Quanto ao quesito *Docker*, gostei bastante de fazer comunicações entre projetos de tecnologias diferentes, mostrando o poder dos *containers* e como pode ser possível várias equipes de diferentes *stacks* trabalharem em conjunto para um mesmo proposito.
