"""Módulo contendo todos os schemas relacionados a Filme"""
from typing import List
from pydantic import BaseModel
from model import Movie

class MovieSchema(BaseModel):
    """ Define como um novo filme a ser inserido deve ser representado
    """
    name: str = "A Rede Social"
    year: int = 2010
    img: str = "https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg"
    genre_names: List[str] = ["Documentário", "Animação"]
    
class MovieUpdateSchema(BaseModel):
    """ Define como um filme a ser atualizado deve ser representado
    """
    id: int = 1
    name: str = "A Rede Social"
    year: int = 2010
    img: str = "https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg"
    genre_names: List[str] = ["Documentário", "Animação"]


class MovieViewSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
    """
    id: int = 1
    name: str = "A Rede Social"
    year: int = 2010
    img: str = "https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg"
    genre_names: List[str] = ["Documentário", "Animação"]

def show_movie(movie: Movie):
    """ Retorna uma representação do Filme seguindo o schema definido em
        MovieViewSchema.
    """
    return {
        "id": movie.id,
        "name": movie.name,        
        "year": movie.year,
        "img": movie.image_link,
        "genre": [genre.name for genre in movie.genres]
    }

class ListMoviesSchema(BaseModel):
    """ Define como uma listagem de filmes será retornada.
    """
    movies:List[MovieSchema]

def show_movies(movies: List[Movie]):
    """ Retorna uma representação de uma lista de filmes seguindo o schema definido em
        MovieViewSchema.
    """
    result = []
    for movie in movies:
        result.append({
            "id": movie.id,
            "name": movie.name,
            "year": movie.year,
            "img": movie.image_link,
            "genre": [genre.name for genre in movie.genres]
        })
    return result
