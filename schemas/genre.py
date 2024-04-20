"""Módulo contendo todos os schemas relacionados a Gênero"""
from typing import List
from pydantic import BaseModel
from model import Genre

class GenreSchema(BaseModel):
    """ Define como um novo filme a ser inserido deve ser representado
    """
    name: str = "Documentário"

class GenreViewSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
    """
    id: int = 1
    nome: str = "Documentário"

def show_genre(genre: Genre):
    """ Retorna uma representação do Gênero seguindo o schema definido em
        GenreViewSchema.
    """
    return {
        "id": genre.id,
        "nome": genre.name,
    }

class ListGenresSchema(BaseModel):
    """ Define como uma listagem de gêneros será retornada.
    """
    genres:List[GenreSchema]


def show_genres(genres: List[Genre]):
    """ Retorna uma representação de uma lista de gêneros seguindo o schema definido em
        GenreViewSchema.
    """
    result = []
    for genre in genres:
        result.append({
            "id": genre.id,
            "nome": genre.name            
        })

    return {"genres": result}
