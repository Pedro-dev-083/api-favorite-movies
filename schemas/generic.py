"""Módulo contendo todos os schemas genéricos"""

from pydantic import BaseModel

class GenericSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição.
    """
    message: str

class IdSchema(BaseModel):
    """ Define como deve ser inserido a estrutura de um dado por ID
    """
    id: str
