# Api-Favorite-Movies

*Back-end* do Projeto chamado **"*Favorite Movies*"**, cujo o objetivo é poder guardar os filmes favoritos.

Esse projeto foi feito utilizando *Python*, com *Flask* sendo o *framework*, o banco está em *SQLite*, e o *ORM* que gerencia é o *SQLAlchemy*.

Esse é um projeto feito por **Pedro Souza de Azevedo** como *MVP* para a disciplina de **Desenvolvimento *Full-Stack* Básico**, do curso de pós-graduação da ***PUC-Rio***.

O *Front-end* desse projeto está aqui: https://github.com/Pedro-dev-083/

## Como configurar o projeto
### Clonagem do projeto:
Para clonar o projeto em sua máquina, é necessário ter o Git instalado, e então, você pode usar o seguinte comando:

    clone
Logo após ao clonar, você pode abrir a pasta, e acessar o terminal dentro dela para seguir os próximos passos.

### Banco de dados:
O projeto utiliza de um banco ***SQLite***, e está configurado para criar um caso não haja, então, configuração de banco não é necessária.

### Versão do *Python*:
Quanto a execução do projeto, é necessário ter instalado *Python* na máquina, sendo de preferência ***Python 3.12.2***, que foi a versão utilizada para o desenvolvimento desse projeto.

### Uso do ambiente virtual:
Também é recomendado a utilização de um ambiente virtual *Python* que pode ser criado e ativado da seguinte forma:

#### No Windows:
Dentro da pasta do projeto, abra o prompt de comando e use o comando :

	python -m venv venv 
Logo após, ative o ambiente usando esse comando:

    venv\Scripts\activate 
 
 #### No Mac ou Linux:
 Dentro da pasta do projeto, abra o terminal e use o comando :

	python3 -m venv venv
Logo após, ative o ambiente usando esse comando:

    source venv/bin/activate


#### Ambos os sistemas:
Ao ativar o *venv* o terminal provavelmente estará assim:

    (venv) PS C:\Users\pedro\Codigos\api-favorite-movies>

Para desativar o ambiente virtual, use esse comando no terminal ou prompt de comando:

    deactivate
### Instalar as dependências:
As dependências estão um arquivo *txt* chamado de ***requirements.txt***, para instalar elas, basta usar o seguinte comando:

    pip install -r requirements.txt
É necessário instalar tudo que está no *requirements.txt*, pois, nele que está tudo o que é necessário para o projeto rodar, como o *Flask* e *SQLAlchemy*, além do *OpenAPI*, que possibilita usar o *Swagger* como documentação para testar.

 Caso dê certo, você receberá uma mensagem como essa:

    Successfully installed Flask-3.0.2 Flask-Cors-3.0.10 Flask-SQLAlchemy-3.1.1 Jinja2-3.1.3 MarkupSafe-2.1.5 SQLAlchemy-2.0.29 SQLAlchemy-Utils-0.41.2 Six-1.16.0 Werkzeug-3.0.2 annotated-types-0.6.0 blinker-1.7.0 click-8.1.7 colorama-0.4.6 flask-openapi3-3.1.0 greenlet-3.0.3 itsdangerous-2.1.2 pydantic-2.6.4 pydantic_core-2.16.3 typing_extensions-4.10.0

#### Atenção:
Caso ocorra algum erro, aqui vai algumas sugestões:

 - **Verifique se sua versão do *Python* é a 3.0.0 ou superior:** Caso não, é recomendável atualizar, pois, como foi dito no começo, esse projeto foi desenvolvido em *Python3*.
 - **Verifique se houve algum problema de conexão:** Certos casos não instala todas as dependências, pois acontece algum problema de conexão, caso seja o caso, execute o comando de instalação novamente.
 - **Atualize as dependências**: Caso futuramente, o projeto não consiga rodar, possivelmente alguma dependência ficou defasada, procure ver qual dependência o terminal está reclamando, atualize a versão dela no *requirements.txt* e tente instalar novamente.

   
 ### Executar o projeto
Tendo seguido todos os passos com sucesso, agora resta executar o projeto, utilizando o seguinte comando:

    python app.py 
Caso tenha funcionado corretamente, você verá uma mensagem como essa:

    Running on http://127.0.0.1:5000                                                                                                                        
Com isso você pode utilizar da *API* dentro de sua máquina, para começar, você pode acessar o link http://localhost:5000/, que leva ao *Swagger*, onde está documentado todas as rotas que você pode usar.

Se não funcionou, verifique os passos anteriores, e tente novamente.

## Utilizando o *Swagger*
Esse projeto foi desenvolvido usando ***OpenAPI***, tendo o *Swagger* como documentação. Com o projeto aberto, você pode acessar o link que o terminal gerou, ou acessando o http://localhost:5000/ .

Lá você irá encontrar todas as rotas que estão disponibilizadas para uso dentro desse projeto. Como por exemplo, a rota http://localhost:5000/movies que irá retornar todos os filmes salvos no banco.
