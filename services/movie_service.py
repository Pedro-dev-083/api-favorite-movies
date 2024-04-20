"""Módulo contendo todos os métodos necessários de Filme"""
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from model import Movie, Genre

class MovieService:
    """
        Classe de serviços de Filme, contendo as operações 
        necessárias como inclusão, atualização, remoção e leitura.
    """
    def __init__(self, session: Session):
        self.session = session

    def create_movie(self, name: str, year: int, img: str, genre_names: List[str]) -> Movie:
        """
        Cria um filme com um gênero existente na base de dados.

        Arguments:
            name: o nome do filme.
            year: o ano de lançamento do filme.
            genre_name: o nome do gênero do filme.
            img: o link da imagem
            date_insert: data de inserção do filme na base de dados.

        Returns:
            O filme criado.
        """
        genres = self.session.query(Genre).filter(Genre.name.in_(genre_names)).all()
        if len(genres) != len(genre_names):
            raise ValueError("Um ou mais gêneros não existem na base de dados.")

        existing_movie = self.session.query(Movie).filter_by(name=name).first()

        if existing_movie is not None:
            raise ValueError(f"Já existe um filme com o nome '{name}' ou com a mesma imagem")

        movie = Movie(name=name, year=year, image_link=img)
        movie.genres.extend(genres)
        try:
            self.session.add(movie)
            self.session.commit()
        except IntegrityError as exc:
            self.session.rollback()
            msg = f"Já existe um filme com o nome '{name}'"
            raise ValueError(msg) from exc

        return movie

    def get_movie(self, id_: str) -> Movie:

        """
        Retorna o filme baseado no Id
        
        Returns:
            O filme baseado no Id.
        """
        movie = self.session.query(Movie).filter_by(id=id_).first()
        if movie is None:
            raise ValueError("Não existe um filme com esse Id")
        return movie

    def get_all_movies(self) -> List[Movie]:

        """
        Retorna todos os filmes existentes na base de dados.        
        
        Returns:
            Todos os filmes da base de dados.
        """
        movies = self.session.query(Movie).all()
        return movies

    def update_movie(self, id_: str, name: str,
                     year: int, img: str, genre_names: List[str]) -> Movie:
        """
        Atualiza um filme com um gênero existente na base de dados.

        Arguments:
            name: o nome do filme.
            year: o ano de lançamento do filme.
            genre_name: o nome do gênero do filme.
            img: o link da imagem
            date_insert: data de inserção do filme na base de dados.

        Returns:
            O filme atualizado.
        """
        genres = self.session.query(Genre).filter(Genre.name.in_(genre_names)).all()
        if len(genres) != len(genre_names):
            raise ValueError("Um ou mais gêneros não existem na base de dados.")

        movie = self.session.query(Movie).filter_by(id=id_).first()

        if movie is None:
            raise ValueError("Não existe um filme com esse Id")
        try:
            movie.name = name
            movie.year = year
            movie.image_link = img
            movie.genres.clear()
            for genre in genres:
                movie.genres.append(genre)
            self.session.commit()
        except IntegrityError as exc:
            self.session.rollback()
            msg = f"Já existe um filme com o nome '{name}'"
            raise ValueError(msg) from exc

        return movie

    def delete_movie(self, id_: str) -> None:

        """
        Deleta o filme baseado no Id
        
        Returns:
            Mensagem de confirmação
        """
        movie = self.session.query(Movie).filter_by(id=id_).first()
        if movie is None:
            raise ValueError("Não existe um filme com esse Id")

        try:
            self.session.delete(movie)
            self.session.commit()
        except IntegrityError as exc:
            self.session.rollback()
            msg = "Não foi possível deletar o filme"
            raise ValueError(msg) from exc
