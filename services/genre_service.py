"""Módulo contendo todos os métodos necessários de Gênero"""
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from model import Genre

class GenreService:
    """
        Classe de serviços de Gênero, contendo as operações 
        necessárias como inclusão, atualização, remoção e leitura.
    """
    def __init__(self, session: Session):
        self.session = session

    def create_genre(self, name: str) -> Genre:
        """
        Cria um gênero.

        Arguments:
            name: o nome do gênero.

        Returns:
            O gênero criado.
        """

        genre = Genre(name=name)
        try:
            self.session.add(genre)
            self.session.commit()
        except IntegrityError as exc:
            self.session.rollback()
            raise ValueError(f"Já existe um gênero com o nome '{name}'") from exc

        return genre

    def get_all_genres(self) -> List[Genre]:

        """
        Retorna todos os gêneros existentes na base de dados.        
        
        Returns:
            Todos os gêneros da base de dados.
        """
        genres = self.session.query(Genre).all()
        return genres
