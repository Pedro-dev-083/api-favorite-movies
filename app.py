"""Módulo de execução de toda aplicação do python"""

from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from sqlalchemy.exc import IntegrityError

from model import Session
from logger import logger
# pylint: disable=W0401:wildcard-import
from schemas import *
from services.movie_service import MovieService
from services.genre_service import GenreService

info = Info(title="API Filmes Favoritos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags

movie_tag = Tag(name="Filmes", description="Rotas para o controle de filmes")
genre_tag = Tag(name="Gêneros", description="Rotas para o controle de gêneros")

@app.get('/movies', tags=[movie_tag],
         responses={"200": ListMoviesSchema, "404": ErrorSchema})
def get_movies():
    """Faz a busca por todos os filmes cadastrados

    Retorna uma representação da listagem dos filmes.
    """
    logger.debug("Coletando todos os filmes ")
    # criando conexão com a base
    session = Session()
    movie_service = MovieService(session)
    movies = movie_service.get_all_movies()


    if not movies:
        # se não há filmes cadastrados
        return {"filmes": []}, 200

    logger.debug("%s Filmes encontrados", len(movies))
    return show_movies(movies), 200

# O correto é fazer a requisição por GET,
# mas quando tento de outra forma, cai em um problema de CORS
@app.post('/movie/id', tags=[movie_tag],
         responses={"200": MovieViewSchema, "404": ErrorSchema})
def get_movie(form: IdSchema):
    """Faz a busca por um filme baseado no Id

    Retorna uma representação da listagem dos filmes.
    """
    logger.debug("Coletando todos os filmes ")
    # criando conexão com a base
    session = Session()
    movie_service = MovieService(session)
    movie = movie_service.get_movie(form.id)


    if not movie:
        # se não há filme
        logger.debug("Não existe filme com esse ID")
        return {"message": "Não existe filme com esse ID"}, 400

    logger.debug("Filme foi encontrado")
    return show_movie(movie), 200

@app.post('/movie', tags=[movie_tag],
         responses={"200": MovieViewSchema, "404": ErrorSchema})
def add_movie(form: MovieSchema):
    """Adiciona um novo Filme à base de dados
    Retorna uma representação do filme.
    """
    logger.debug("Adicionando filme de nome: '%s'", form.name)
    try:
        # criando conexão com a base
        session = Session()
        movie_service = MovieService(session)
        movie = movie_service.create_movie(form.name, form.year, form.img, form.genre_names)
        logger.debug("Adicionado filme de nome: '%s'", movie.name)
        return show_movie(movie), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = e.args[0]
        logger.warning("Erro ao adicionar filme '%s', %s", form.name, error_msg)
        return {"message": error_msg}, 409

    except ValueError as e:
        # caso tente criar um filme com um gênero não existente
        error_msg = e.args[0]
        logger.warning("Erro ao adicionar filme '%s', %s", form.name, error_msg)
        return {"message": error_msg}, 400

    # pylint: disable=W0718:broad-exception-caught
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo filme"
        logger.warning("Erro ao adicionar filme '%s', %s", form.name, e.args[0])
        return {"message": error_msg}, 500

@app.put('/movie', tags=[movie_tag],
         responses={"200": MovieViewSchema, "404": ErrorSchema})
def update_movie(form: MovieUpdateSchema):
    """Atualiza um Filme à base de dados
    Retorna uma representação do filme.
    """
    logger.debug("Atualizando filme de nome: '%s'", form.name)
    try:
        # criando conexão com a base
        session = Session()
        movie_service = MovieService(session)
        movie = movie_service.update_movie(form.id,
                                           form.name, form.year, form.img, form.genre_names)
        logger.debug("Atualizado filme de nome: '%s'", movie.name)
        return show_movie(movie), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = e.args[0]
        logger.warning("Erro ao atualizar filme '%s', %s", form.name, error_msg)
        return {"message": error_msg}, 409

    except ValueError as e:
        # caso tente atualizar um filme com um gênero não existente
        error_msg = e.args[0]
        logger.warning("Erro ao atualizar filme '%s', %s", form.name, error_msg)
        return {"message": error_msg}, 400

    # pylint: disable=W0718:broad-exception-caught
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível atualizar filme"
        logger.warning("Erro ao atualizar filme '%s', %s", form.name, e.args[0])
        return {"message": error_msg}, 500

@app.delete('/movie/id', tags=[movie_tag],
         responses={"200": GenericSchema, "404": ErrorSchema})
def delete_movie(form: IdSchema):
    """Exclui um filme baseado no Id

    Retorna uma confirmação de deleção.
    """
    logger.debug("Começando a deletar o filme ")
    # criando conexão com a base
    try:
        session = Session()
        movie_service = MovieService(session)
        movie_service.delete_movie(form.id)

    except ValueError as e:
        # caso tente criar um filme com um gênero não existente
        error_msg = e.args[0]
        logger.warning("Erro ao adicionar filme '%s', %s", form.name, error_msg)
        return {"message": error_msg}, 400

    # pylint: disable=W0718:broad-exception-caught
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo filme"
        logger.warning("Erro ao adicionar filme '%s', %s", form.name, e.args[0])
        return {"message": error_msg}, 500

    logger.debug("Filme foi deletado")
    return {"message": "Filme foi deletado com sucesso"}, 200

@app.get('/genres', tags=[genre_tag],
         responses={"200": ListGenresSchema, "404": ErrorSchema})
def get_genres():
    """Faz a busca por todos os gêneros cadastrados

    Retorna uma representação da listagem dos gêneros.
    """
    logger.debug("Coletando todos os gêneros ")
    # criando conexão com a base
    session = Session()
    genre_service = GenreService(session)
    genres = genre_service.get_all_genres()


    if not genres:
        # se não há gêneros cadastrados
        return {"Gêneros": []}, 200

    logger.debug("%s Gêneros encontrados", len(genres))
    return show_genres(genres), 200

@app.post('/genre', tags=[genre_tag],
         responses={"200": GenreViewSchema, "404": ErrorSchema})
def add_genre(form: GenreSchema):
    """Adiciona um novo gênero à base de dados
    Retorna uma representação do gênero.
    """
    logger.debug("Adicionando gênero: '%s'", form.name)
    try:
        # criando conexão com a base
        session = Session()
        genre_service = GenreService(session)
        genre = genre_service.create_genre(form.name)
        logger.debug("Adicionado gênero: '%s'", genre.name)
        return show_genre(genre), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = e.args[0]
        logger.warning("Erro ao adicionar gênero '%s', %x", form.name, error_msg)
        return {"message": error_msg}, 409

    except ValueError as e:
        # caso tente criar um filme com um gênero não existente
        error_msg = e.args[0]
        logger.warning("Erro ao adicionar gênero '%s', %x", form.name, error_msg)
        return {"message": error_msg}, 400

    # pylint: disable=W0718:broad-exception-caught
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Erro interno ao tentar salvar um gênero"
        logger.warning("Erro ao adicionar gênero '%s', %x", form.name, error_msg)
        return {"message": error_msg}, 500

@app.route('/')
def home():
    """Redireciona para /swagger
    """
    return redirect('/openapi/swagger')

if __name__ == "__main__":
    app.run(debug=True)
