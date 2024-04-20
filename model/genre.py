"""Módulo contendo as informações de Gênero"""
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from model import Base

# pylint: disable=R0903:too-few-public-methods
class Genre(Base):
    """Classe representando o modelo de um Gênero"""
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    date_insert = Column(DateTime, default=datetime.now())
    movies = relationship("Movie", secondary="movie_genre", back_populates="genres")

    def __init__(self, name:str):
        """
        Cria um Gênero

        Arguments:
            name: o nome do gênero.
        """
        self.name = name
