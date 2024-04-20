"""Módulo contendo as informações de Filme"""
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from model import Base

# pylint: disable=R0903:too-few-public-methods
class Movie(Base):
    """Classe representando o modelo de um Filme"""
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    image_link = Column(String(255), unique=True, nullable=False)
    year = Column(Integer)
    date_insert = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o filme e o gênero.
    genres = relationship("Genre", secondary="movie_genre", back_populates="movies")

    def __init__(self, name:str,
                 year:int,
                 image_link: str):
        """
        Cria um Filme

        Arguments:
            name: o nome do filme.
            year: o ano de lançamento do filme.
            genre: o gênero do filme.
            date_insert: data de inserção do filme na base de dados.
        """
        self.name = name
        self.year = year
        self.image_link = image_link
