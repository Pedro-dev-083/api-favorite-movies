"""Módulo de execução de toda aplicação do python"""
import os

from flask_cors import CORS
from flask import Flask, request, redirect
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger
import requests
from dotenv import load_dotenv
from models import ErrorModel
from logger import logger

load_dotenv()

app = Flask(__name__)
api = Api(app)

swagger = Swagger(app)

CORS(app)

app.config['API_KEY'] = os.getenv('API_KEY')

SWAGGER_URL = '/swagger'
API_URL = '/static/api_spec.yml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={'app_name': "API Filmes Favoritos"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.get('/movieById')
def get_movie_by_id():
    """
    Faz a busca do filme pelo ID
    """
    try:
        external_id = request.args.get('externalId')
        logger.debug("Coletando o filme pela API externa ")
        response = requests.get(
            f'https://www.omdbapi.com/?i={external_id}&apikey={app.config["API_KEY"]}', timeout=30)
        data = response.json()
        if data.get('Response') == "True":
            response_data = {
                "title": data.get('Title', 'Unknown Title'),
                "year": data.get('Year', 'Unknown Year'),
                "genre": data.get('Genre', 'Unknown Genre'),
                "plot": data.get('Plot', 'No Plot Available'),
                "poster": data.get('Poster', 'No Poster Available'),
                "rated": data.get('Rated', 'No Rated Available'),                
                "imdbID": external_id
            }
            logger.debug("%s Filme encontrado: ", response_data)
            return response_data, 200

        error = ErrorModel(
            message='Filme não foi encontrado',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400
    # pylint: disable=W0718:broad-exception-caught
    except Exception as ex:
        error = ErrorModel(
            message='Erro ao tentar recuperar filme',
            execption=str(ex)
        )
        logger.error(error)
        return dict(error), 500

@app.get('/movieByName')
def get_movie_by_name():
    """
    Faz a busca do filme pelo nome
    """
    name = request.args.get('name')
    response = requests.get(
        f'https://www.omdbapi.com/?t={name}&apikey={app.config["API_KEY"]}', timeout=30)
    try:
        data = response.json()
        if data.get('Response') == "True":
            response_data = {
                "title": data.get('Title', 'Unknown Title'),
                "year": data.get('Year', 'Unknown Year'),
                "genre": data.get('Genre', 'Unknown Genre'),
                "plot": data.get('Plot', 'No Plot Available'),
                "poster": data.get('Poster', 'No Poster Available'),
                "rated": data.get('Rated', 'No Rated Available'),   
                "imdbID": data.get('imdbID', 'No ImdbID Available')
            }
            logger.debug("%s Filme encontrado: ", response_data)
            return response_data, 200

        error = ErrorModel(
            message='Filme não foi encontrado',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400
    # pylint: disable=W0718:broad-exception-caught
    except Exception as ex:
        error = ErrorModel(
            message='Erro ao tentar recuperar filme',
            execption=str(ex)
        )
        logger.error(error)
        return dict(error), 500

@app.get('/movieOnBase')
def get_movie_on_base():
    """
    Faz a busca do filme pelo id da base
    """
    id_base = request.args.get('id')
    query = '''
        query GetMovie($id: Int!){
            movie(id: $id) {
                id
                name
                external_Id
                favorite
            }
        }
    '''
    variables = {'id': int(id_base)}

    url = 'http://movie-graphql-container:8080/graphql/'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'query': query,
        'variables': variables or {}
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            data_response = response.json()
            logger.debug("%s Filme encontrado: ", data_response)
            return data_response, response.status_code

        error = ErrorModel(
            message='Filme não foi encontrado',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400
    # pylint: disable=W0718:broad-exception-caught
    except Exception as ex:
        error = ErrorModel(
            message='Erro ao tentar recuperar filme',
            execption=str(ex)
        )
        logger.error(error)
        return dict(error), 500

@app.get('/moviesOnBase')
def get_all_movies():
    """
    Faz a busca do filme pelo id da base
    """
    query = '''
        query {
          movies {
            external_Id
            favorite
            id
            name
          }
        }
    '''

    url = 'http://movie-graphql-container:8080/graphql/'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'query': query,
        'variables': {}
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            data_response = response.json()
            logger.debug("%s Filme encontrado: ", data_response)
            return data_response, response.status_code

        error = ErrorModel(
            message='Nenhum filme foi encontrado na base',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400
    # pylint: disable=W0718:broad-exception-caught
    except Exception as ex:
        error = ErrorModel(
            message='Erro ao tentar recuperar filme',
            execption=str(ex)
        )
        logger.error(error)
        return dict(error), 500

@app.post('/movieOnBase')
def post_movie_on_base():
    """
    Insere o filme na base
    """
    data = request.get_json()

    if not data:
        error = ErrorModel(
            message='Nenhuma informação JSON foi especificada',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400

    query = '''
        mutation AddMovie($name: String!, $externalId: String!, $favorite:Boolean){
              addMovie(name: $name, external_Id: $externalId, favorite: $favorite) {
                id
                name
                external_Id
                favorite
            }
        }
    '''
    variables = {
        'name': data.get('name', ''),
        'externalId': data.get('external_Id', ''),
        'favorite': data.get('favorite', '')
    }


    url = 'http://movie-graphql-container:8080/graphql/'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'query': query,
        'variables': variables or {}
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            data_response = response.json()
            logger.debug("%s Filme Adicionado: ", data_response)
            return data_response, response.status_code

        error = ErrorModel(
            message='Algum parâmetro foi entregue errado',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400
    # pylint: disable=W0718:broad-exception-caught
    except Exception as ex:
        error = ErrorModel(
            message='Erro ao tentar recuperar filme',
            execption=str(ex)
        )
        logger.error(error)
        return dict(error), 500

@app.put('/movieOnBase')
def update_movie_on_base():
    """
    Atualiza o filme na base
    """
    data = request.get_json()

    if not data:
        error = ErrorModel(
            message='Nenhuma informação JSON foi especificada',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400

    query = '''
        mutation UpdateMovie($id: Int!, $favorite:Boolean){
              updateMovie(id: $id, favorite: $favorite) {
                id
                name
                external_Id
                favorite
            }
        }
    '''
    variables = {
        'id': data.get('id', ''),
        'favorite': data.get('favorite', '')
    }

    url = 'http://movie-graphql-container:8080/graphql/'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'query': query,
        'variables': variables or {}
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            data_response = response.json()
            logger.debug("%s Filme Atualizado: ", data_response)
            return data_response, response.status_code

        error = ErrorModel(
            message='Algum parâmetro foi entregue errado',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400
    # pylint: disable=W0718:broad-exception-caught
    except Exception as ex:
        error = ErrorModel(
            message='Erro ao tentar recuperar filme',
            execption=str(ex)
        )
        logger.error(error)
        return dict(error), 500

@app.delete('/movieOnBase')
def delete_movie_on_base():
    """
    Deleta o filme na base
    """
    data = request.get_json()

    if not data:
        error = ErrorModel(
            message='Nenhuma informação JSON foi especificada',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400

    query = '''
        mutation RemoveMovie($id: Int!){
            removeMovie(id: $id){
                message
                success
            }
        }
    '''
    variables = {
        'id': data.get('id', ''),
    }

    url = 'http://movie-graphql-container:8080/graphql/'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'query': query,
        'variables': variables or {}
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            data_response = response.json()
            logger.debug("%s Filme Deletado: ", data_response)
            return data_response, response.status_code

        error = ErrorModel(
            message='Algum parâmetro foi entregue errado',
            execption='Não houve exceção'
        )
        logger.error(error)
        return dict(error), 400
    # pylint: disable=W0718:broad-exception-caught
    except Exception as ex:
        error = ErrorModel(
            message='Erro ao tentar recuperar filme',
            execption=str(ex)
        )
        logger.error(error)
        return dict(error), 500


@app.route('/')
def home():
    """Redireciona para /swagger
    """
    return redirect('/swagger')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
